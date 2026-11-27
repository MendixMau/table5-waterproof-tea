/* ================= OSME shop: cart, waitlist, menu ================= */

/* WAITLIST: the one setting to change when the team picks a service.
   kind: ""           -> no service yet: saved on this device, success shown.
         "api"        -> our own API (site-api/ on Vercel): endpoint "https://<project>.vercel.app/api/waitlist",
                         countUrl "https://<project>.vercel.app/api/count". If the API is down, the email is saved on this device.
         "formspree"  -> endpoint "https://formspree.io/f/<id>"
         "formsubmit" -> endpoint "https://formsubmit.co/ajax/<email-or-token>"
         "google"     -> endpoint "https://docs.google.com/forms/d/e/<id>/formResponse", emailField "entry.<n>", cartField "entry.<n>"
   countUrl: optional published-sheet CSV URL (Google): the Keeper count is its row count minus the header. */
var WAITLIST = { kind: "", endpoint: "", emailField: "", cartField: "", countUrl: "" };

var TEA_NAMES = { gyokuro: "Gyokuro", sencha: "Sencha", longjing: "Longjing", tieguanyin: "Tieguanyin", puerh: "Pu-erh", "english-breakfast": "English Breakfast", ritual: "The Ritual" };
var PRICES = { tin: §TIN_N§, bag: §BAG_N§, ritual: §RITUAL_N§ }; /* set in build.py */
var KIND_LABEL = { tin: "Tin of 12 bags", bag: "Single bag", ritual: "Subscription · 16 bags from 3-4 origins a month" };
var CART_KEY = "osme-cart-v1", WL_KEY = "osme-waitlist-v1";

function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || "null"); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
function fmt(n) { return "$" + (n % 1 || n < 10 ? n.toFixed(2) : String(n)); }
function cart() { return store(CART_KEY) || []; }
function saveCart(c) { store(CART_KEY, c); renderCart(); }

function addToCart(id, kind, qty) {
  qty = qty || 1;
  var c = cart(), hit = null;
  if (kind === "ritual") { id = "ritual"; }
  c.forEach(function (it) { if (it.id === id && it.kind === kind) hit = it; });
  if (hit) { hit.qty = kind === "ritual" ? 1 : hit.qty + qty; } else { c.push({ id: id, kind: kind, qty: kind === "ritual" ? 1 : qty }); }
  saveCart(c);
  openCart();
}

function renderCart() {
  var c = cart(), n = 0, total = 0, bags = 0, monthly = 0;
  c.forEach(function (it) { n += it.qty; var p = PRICES[it.kind] * it.qty; if (it.kind === "ritual") monthly += p; else total += p; bags += it.kind === "tin" ? 12 * it.qty : it.kind === "bag" ? it.qty : 16; });
  document.querySelectorAll("[data-cart-n]").forEach(function (el) { el.textContent = n; el.classList.toggle("on", n > 0); });
  var box = document.querySelector("[data-cart-items]");
  if (!box) return;
  if (!c.length) {
    box.innerHTML = '<div class="empty"><p>Your cart is empty.</p><a class="btn sm" href="shop.html">Shop the teas</a> <a class="btn sm" href="ritual.html">The Ritual</a></div>';
  } else {
    box.innerHTML = c.map(function (it, i) {
      return '<div class="ci"><div><b>' + (TEA_NAMES[it.id] || it.id) + '</b><small>' + KIND_LABEL[it.kind] + '</small></div>' +
        (it.kind === "ritual" ? '<span class="ci-q">1</span>' : '<div class="qty sm"><button type="button" data-ci="' + i + '" data-d="-1" aria-label="Less">−</button><span>' + it.qty + '</span><button type="button" data-ci="' + i + '" data-d="1" aria-label="More">+</button></div>') +
        '<em>' + fmt(PRICES[it.kind] * it.qty) + (it.kind === "ritual" ? "/mo" : "") + '</em><button type="button" class="rm" data-rm="' + i + '" aria-label="Remove">×</button></div>';
    }).join("");
  }
  var t = document.querySelector("[data-cart-total]");
  if (t) t.textContent = (total ? fmt(total) : (monthly ? "" : "$0")) + (total && monthly ? " + " : "") + (monthly ? fmt(monthly) + "/month" : "");
  var pc = document.querySelector("[data-cart-percup]");
  if (pc) pc.textContent = bags ? (bags + (bags === 1 ? " bag" : " bags") + " · up to " + bags * 3 + " cups · about §CUP§ a cup") : "";
  var pre = document.querySelector("[data-preorder]");
  if (pre) pre.style.display = c.length ? "" : "none";
}

function openCart() { document.body.classList.add("cart-open"); var d = document.querySelector(".drawer"); if (d) d.setAttribute("aria-hidden", "false"); }
function closeCart() { document.body.classList.remove("cart-open"); var d = document.querySelector(".drawer"); if (d) d.setAttribute("aria-hidden", "true"); }

var toastT;
function toast(msg) { var el = document.querySelector("[data-toast]"); if (!el) return; el.textContent = msg; el.classList.add("on"); clearTimeout(toastT); toastT = setTimeout(function () { el.classList.remove("on"); }, 2200); }

document.addEventListener("click", function (e) {
  var t = e.target.closest("[data-add],[data-add-opt],[data-open-cart],[data-close-cart],[data-rm],[data-ci],[data-q],[data-menu],[data-filter],[data-view-btn]");
  if (!t) return;
  if (t.hasAttribute("data-add")) { var a = t.getAttribute("data-add").split(":"); addToCart(a[0], a[1], 1); }
  else if (t.hasAttribute("data-add-opt")) {
    var opt = (document.querySelector('input[name="opt"]:checked') || {}).value || "tin";
    var q = parseInt((document.querySelector("[data-qv]") || {}).textContent || "1", 10);
    addToCart(t.getAttribute("data-add-opt"), opt, q);
  }
  else if (t.hasAttribute("data-open-cart")) openCart();
  else if (t.hasAttribute("data-close-cart")) closeCart();
  else if (t.hasAttribute("data-rm")) { var c = cart(); c.splice(+t.getAttribute("data-rm"), 1); saveCart(c); }
  else if (t.hasAttribute("data-ci")) { var c2 = cart(), it = c2[+t.getAttribute("data-ci")]; it.qty = Math.max(1, it.qty + +t.getAttribute("data-d")); saveCart(c2); }
  else if (t.hasAttribute("data-q")) { var qv = document.querySelector("[data-qv]"); qv.textContent = Math.max(1, Math.min(24, +qv.textContent + +t.getAttribute("data-q"))); }
  else if (t.hasAttribute("data-view-btn")) {
    var v = t.getAttribute("data-view-btn"), art = document.querySelector("[data-view]");
    if (art) art.setAttribute("data-view", v);
    document.querySelectorAll("[data-view-btn]").forEach(function (b) { b.classList.toggle("on", b === t); });
  }
  else if (t.hasAttribute("data-menu")) document.body.classList.toggle("menu-open");
  else if (t.hasAttribute("data-filter")) {
    var f = t.getAttribute("data-filter");
    document.querySelectorAll("[data-filter]").forEach(function (b) { b.classList.toggle("on", b === t); });
    document.querySelectorAll("[data-tea-grid] .tea-card").forEach(function (card) { card.style.display = (f === "all" || card.getAttribute("data-country") === f) ? "" : "none"; });
  }
});
document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeCart(); document.body.classList.remove("menu-open"); } });

/* shop filter from the URL hash (#Japan, #China, #Britain) */
(function () { var h = decodeURIComponent(location.hash.slice(1)); var b = h && document.querySelector('[data-filter="' + h + '"]'); if (b) b.click(); })();

/* ---------- waitlist ---------- */
function cartSummary() { return cart().map(function (it) { return (TEA_NAMES[it.id] || it.id) + " " + it.kind + " x" + it.qty; }).join("; "); }

function saveLocal(payload) { var list = store(WL_KEY) || []; list.push(payload); store(WL_KEY, list); return { local: true }; }

function sendWaitlist(email, source) {
  var payload = { email: email, cart: cartSummary(), source: source, page: location.pathname.split("/").pop() || "index.html", at: new Date().toISOString() };
  if (!WAITLIST.kind || !WAITLIST.endpoint) return Promise.resolve(saveLocal(payload));
  if (WAITLIST.kind === "api") {
    return fetch(WAITLIST.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) })
      .then(function (r) { if (r.status === 400) throw new Error("email"); if (!r.ok) throw new Error("status " + r.status); return r.json(); })
      .catch(function (e) { if (e.message === "email") throw e; return saveLocal(payload); });
  }
  if (WAITLIST.kind === "google") {
    var body = new URLSearchParams(); body.append(WAITLIST.emailField, email); if (WAITLIST.cartField) body.append(WAITLIST.cartField, payload.cart);
    return fetch(WAITLIST.endpoint, { method: "POST", mode: "no-cors", body: body }).then(function () { return {}; });
  }
  return fetch(WAITLIST.endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(payload) })
    .then(function (r) { if (!r.ok) throw new Error("status " + r.status); return {}; });
}

function keeperCount() {
  var els = document.querySelectorAll("[data-keeper-count]");
  if (!els.length || !WAITLIST.countUrl) return;
  fetch(WAITLIST.countUrl, { cache: "no-store" }).then(function (r) { return r.text(); }).then(function (txt) {
    var n = WAITLIST.kind === "api" ? (JSON.parse(txt).count || 0) : txt.trim().split(/\r?\n/).length - 1;
    if (n > 0) els.forEach(function (el) { el.hidden = false; el.innerHTML = "<b>" + n.toLocaleString("en-US") + "</b> " + (n === 1 ? "Keeper" : "Keepers") + " on the waitlist"; });
  }).catch(function () {});
}
keeperCount();
document.querySelectorAll("[data-wl-note]").forEach(function (el) { el.textContent = WAITLIST.endpoint ? "We only use your email to write about OSME." : "Pre-launch: your email is saved on this device until our waitlist service is connected."; });

document.querySelectorAll("form[data-waitlist]").forEach(function (f) {
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    var input = f.querySelector('input[type="email"]'), msg = f.parentNode.querySelector(".wl-msg"), btn = f.querySelector("button");
    var v = (input.value || "").trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { msg.style.color = "#F2A33A"; msg.textContent = "Please add an email address we could write to."; input.focus(); return; }
    btn.disabled = true;
    sendWaitlist(v, f.getAttribute("data-waitlist")).then(function () {
      msg.style.color = "#3DBA9B";
      msg.textContent = f.getAttribute("data-waitlist") === "cart" ? "Welcome, Keeper. Your pre-order is saved; we write when your first box is ready." : "Welcome, Keeper. You are on the list for the first Ritual box.";
      input.value = ""; f.classList.add("done"); keeperCount();
    }).catch(function () {
      msg.style.color = "#F2A33A"; msg.textContent = "That did not go through. Please try again in a moment.";
    }).then(function () { btn.disabled = false; });
  });
});

renderCart();

/* v2 Capsule 3D frame (srcdoc, same origin): grow it to the page inside, so nothing is cut off on a phone */
document.querySelectorAll(".cap3d iframe").forEach(function (f) {
  var base = 0;
  function fit() {
    try {
      f.style.height = ""; base = f.getBoundingClientRect().height;
      var h = f.contentDocument.documentElement.scrollHeight;
      if (h > base) f.style.height = (h + 2) + "px";
    } catch (e) {}
  }
  f.addEventListener("load", function () { fit(); setTimeout(fit, 800); });
  var t; addEventListener("resize", function () { clearTimeout(t); t = setTimeout(fit, 200); });
});
