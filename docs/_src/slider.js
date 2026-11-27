if (document.getElementById("tSlider")) {
  var OPEN = 80, CLOSE = 70, AMBER = "#F2A33A", MID = "#D9C46B", JADE = "#3DBA9B";
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

}
