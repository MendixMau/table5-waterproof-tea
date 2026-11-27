/* OSME play: start and stop every OSME motion inside one element (a slide, a section). No dependencies.
   osmePlay(slideEl)   restarts inline SVG pieces (arc-sweep, logo-reveal, three-bubbles, hero-alive),
                       replays .steep entrances and runs osmeCount (count-up.js) if it is loaded.
   osmePause(slideEl)  stops them at their first frame and hides .steep entrances until osmePlay
                       (call it for every slide that is not showing).
   Typical deck hook: on load, osmePause each slide; on slide change, osmePause(old); osmePlay(new).
   Inline the SVG markup in the page (ids are prefixed per piece). As <img> the SVGs play once on load only. */
(function () {
  function svgs(root) {
    return [].filter.call(root.querySelectorAll("svg"), function (s) {
      return s.setCurrentTime && s.querySelector("animate,animateMotion,animateTransform,set");
    });
  }
  window.osmePlay = function (root) {
    root = root || document;
    svgs(root).forEach(function (s) { s.setCurrentTime(0); s.unpauseAnimations(); });
    [].forEach.call(root.querySelectorAll(".steep"), function (el) {
      el.style.animation = "none";
      void el.offsetWidth; // reflow, so the animation starts again
      el.style.animation = "";
      el.style.opacity = "";
    });
    if (window.osmeCount) window.osmeCount(root);
  };
  window.osmePause = function (root) {
    root = root || document;
    svgs(root).forEach(function (s) { s.pauseAnimations(); s.setCurrentTime(0); });
    [].forEach.call(root.querySelectorAll(".steep"), function (el) {
      el.style.animation = "none"; // hold entrances back until osmePlay
      el.style.opacity = "0";
    });
    if (window.osmeCount) window.osmeCount(root, { at: 0 });
  };
})();
