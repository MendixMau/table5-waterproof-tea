
(function(){
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- hero: sencha cooling loop ---------- */
  var OPEN = 80, CLOSE = 70, TMAX = 100, TMIN = 60;
  var cx = 230, cy = 200, R = 160;
  /* 100\u00a0°C sits left (angle pi), 60\u00a0°C right (angle 0) */
  function xy(t, r){ var a = Math.PI - (TMAX - t) / (TMAX - TMIN) * Math.PI; return [cx + (r||R) * Math.cos(a), cy - (r||R) * Math.sin(a)]; }
  var w = document.getElementById("hWindow");
  var p1 = xy(OPEN), p2 = xy(CLOSE);
  w.setAttribute("d", "M" + p1[0].toFixed(1) + " " + p1[1].toFixed(1) + " A" + R + " " + R + " 0 0 1 " + p2[0].toFixed(1) + " " + p2[1].toFixed(1));
  var ticks = document.getElementById("hTicks"), ns = "http://www.w3.org/2000/svg";
  [100, 80, 70, 60].forEach(function(t){
    var q = xy(t, R + 22), tx = document.createElementNS(ns, "text");
    tx.setAttribute("x", q[0].toFixed(1)); tx.setAttribute("y", (q[1] + 4).toFixed(1));
    tx.textContent = t + "°"; if (t === 80 || t === 70) tx.setAttribute("fill", "#D9C46B");
    ticks.appendChild(tx);
  });
  var needle = document.getElementById("hNeedle"), tTxt = document.getElementById("hTemp"), sTxt = document.getElementById("hState");
  var liquor = document.getElementById("hLiquor"), bloom = document.getElementById("hBloom");
  var bagShape = document.getElementById("hBagShape"), seam = document.getElementById("hSeam"), steam = document.getElementById("hSteam");
  var leaves = document.getElementById("hLeaves");
  var AMBER = "#F2A33A", MID = "#D9C46B", JADE = "#3DBA9B";

  function render(temp, brew, tsec){
    var n = xy(temp); needle.setAttribute("cx", n[0].toFixed(1)); needle.setAttribute("cy", n[1].toFixed(1));
    tTxt.textContent = Math.round(temp) + "°";
    var state, col, dash;
    if (temp > OPEN) { state = "SEALED · TOO HOT"; col = AMBER; dash = "0"; }
    else if (temp >= CLOSE) { state = "OPEN · BREWING"; col = MID; dash = "7 6"; }
    else { state = "SEALED · SCENT KEPT"; col = JADE; dash = "0"; }
    sTxt.textContent = state; sTxt.setAttribute("fill", col);
    needle.setAttribute("fill", temp > OPEN ? "#F3EEE6" : col);
    bagShape.setAttribute("stroke", col); bagShape.setAttribute("stroke-dasharray", dash);
    seam.setAttribute("stroke", col); seam.setAttribute("stroke-dasharray", dash === "0" ? "0" : "3 5");
    liquor.setAttribute("opacity", (brew * 0.62).toFixed(3));
    var open = temp <= OPEN && temp >= CLOSE;
    var pulse = open ? (0.55 + 0.25 * Math.sin(tsec * 3)) : 0;
    bloom.setAttribute("opacity", pulse.toFixed(2));
    bloom.setAttribute("r", (open ? 60 + 40 * brew : 10).toFixed(1));
    leaves.setAttribute("transform", open ? "translate(0 " + (Math.sin(tsec * 2) * 2).toFixed(2) + ")" : "");
    steam.setAttribute("opacity", (0.08 + 0.3 * (temp - TMIN) / (TMAX - TMIN)).toFixed(2));
    steam.setAttribute("transform", "translate(0 " + (-((tsec * 8) % 8)).toFixed(1) + ")");
  }

  if (reduce) { render(75, 0.6, 0); }
  else {
    var CYCLE = 11; /* seconds */
    var start = null;
    var tempAt = function(s){
      if (s < 0.8) return 96;
      var k = (s - 0.8) / (CYCLE - 2.6);
      if (k > 1) return TMIN + 2;
      return TMIN + 2 + (96 - TMIN - 2) * Math.pow(1 - k, 1.35);
    };
    var step = function(ts){
      if (start === null) start = ts;
      var s = ((ts - start) / 1000) % CYCLE;
      var temp = tempAt(s);
      /* brew grows only while open */
      var t80 = null, t70 = null;
      for (var x = 0; x <= CYCLE; x += 0.05) { var v = tempAt(x); if (t80 === null && v <= OPEN) t80 = x; if (t70 === null && v < CLOSE) { t70 = x; break; } }
      var brew = s < t80 ? 0 : Math.min(1, (s - t80) / (t70 - t80));
      if (s > CYCLE - 0.6) brew *= Math.max(0, (CYCLE - s) / 0.6);
      render(temp, brew, ts / 1000);
      requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* ---------- slider ---------- */
  var sl = document.getElementById("tSlider"), rd = document.getElementById("tRead"), st = document.getElementById("tState"), ds = document.getElementById("tDesc");
  function upd(){
    var v = 160 - Number(sl.value); /* left = hot */
    rd.innerHTML = v + "<small>°C</small>";
    if (v > OPEN) { st.textContent = "Sealed · too hot"; st.style.color = AMBER; ds.textContent = "The bag waits. Nothing brews until the water cools to 80\u00a0°C."; }
    else if (v >= CLOSE) { st.textContent = "Open · brewing"; st.style.color = MID; ds.textContent = "Sencha’s window. The bag is open and the leaf brews at its own temperature."; }
    else { st.textContent = "Sealed · scent kept"; st.style.color = JADE; ds.textContent = "Below 70\u00a0°C the bag closes. The steep stops itself and the scent stays in for the next cup."; }
  }
  sl.value = 160 - 92; sl.addEventListener("input", upd); upd();

  /* ---------- waitlist (no backend) ---------- */
  var f = document.getElementById("wl"), em = document.getElementById("wlEmail"), msg = document.getElementById("wlMsg");
  f.addEventListener("submit", function(e){
    e.preventDefault();
    var v = (em.value || "").trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { msg.style.color = "#F2A33A"; msg.textContent = "Please add an email address we could write to."; em.focus(); return; }
    msg.style.color = "#3DBA9B"; msg.textContent = "Welcome, Keeper. You are on the list for the first Ritual box.";
    em.value = "";
  });

})();
