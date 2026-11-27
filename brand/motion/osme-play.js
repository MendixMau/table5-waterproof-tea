/* OSME play: restart every OSME motion inside one element (a slide, a section). No dependencies.
   osmePlay(slideEl)  restarts inline SVG pieces (arc-sweep, logo-reveal, three-bubbles, hero-alive),
                      replays .steep entrances and runs osmeCount (count-up.js) if it is loaded.
   Inline the SVG markup in the page (ids are prefixed per piece, so several can share a page).
   As <img> the SVGs still play once on load, but cannot be restarted reliably. */
(function () {
  window.osmePlay = function (root) {
    root = root || document;
    [].forEach.call(root.querySelectorAll("svg"), function (s) {
      if (s.setCurrentTime && s.querySelector("animate,animateMotion,animateTransform,set")) {
        s.setCurrentTime(0);
        s.unpauseAnimations();
      }
    });
    [].forEach.call(root.querySelectorAll(".steep"), function (el) {
      el.style.animation = "none";
      void el.offsetWidth; // reflow, so the animation starts again
      el.style.animation = "";
    });
    if (window.osmeCount) window.osmeCount(root);
  };
})();
