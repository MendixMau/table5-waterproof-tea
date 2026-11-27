/* OSME count-up. No dependencies.
   <span data-count="8.3" data-prefix="$" data-suffix=" m">$8.3 m</span>
   osmeCount(slideEl)            counts every [data-count] inside slideEl (or slideEl itself)
   osmeCount(slideEl, {at: 0.6}) renders the state at 0.6 s without animating (for stills)
   Options per element: data-duration (ms, default 1400), data-from (default 0).
   Decimals follow data-count: "8.3" -> one decimal, "640" -> none. Thousands get commas. */
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function ease(t) { return 1 - Math.pow(1 - t, 4); } // quartic ease-out: fast start, soft landing

  function fmt(el, v) {
    var dec = (el.dataset.count.split(".")[1] || "").length;
    var s = v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec });
    return (el.dataset.prefix || "") + s + (el.dataset.suffix || "");
  }

  function one(el, at) {
    var to = parseFloat(el.dataset.count), from = parseFloat(el.dataset.from || "0");
    var dur = parseFloat(el.dataset.duration || "1400");
    el.style.fontVariantNumeric = "tabular-nums";
    el.style.whiteSpace = "nowrap";
    if (el._osmeRaf) cancelAnimationFrame(el._osmeRaf);
    function paint(ms) {
      var t = Math.min(1, Math.max(0, ms / dur));
      el.textContent = fmt(el, from + (to - from) * ease(t));
      return t;
    }
    if (reduce) { paint(dur); return; }
    if (at != null) { paint(at * 1000); return; }
    var t0 = null;
    function step(now) {
      if (t0 === null) t0 = now;
      if (paint(now - t0) < 1) el._osmeRaf = requestAnimationFrame(step);
    }
    paint(0);
    el._osmeRaf = requestAnimationFrame(step);
  }

  window.osmeCount = function (root, opts) {
    root = root || document;
    var at = opts && opts.at;
    var list = [].slice.call(root.querySelectorAll("[data-count]"));
    if (root.dataset && root.dataset.count) list.unshift(root);
    list.forEach(function (el) { one(el, at); });
    return list.length;
  };
})();
