// Mobile nav toggle — the only script the site needs.
(function () {
  var nav = document.querySelector(".ef-nav");
  var btn = nav && nav.querySelector(".ef-nav-toggle");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
})();
