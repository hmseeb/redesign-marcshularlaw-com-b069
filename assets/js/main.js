/* Marc Shular Law — site interactions
   - mobile navigation + services dropdown
   - sticky header shadow
   - lead forms: set _page, AJAX submit to LeadrVision, inline confirmation
   - ?submitted=1 confirmation for plain (no-JS) submissions
*/
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    /* ---- _page hidden field: current URL ---- */
    var pageFields = document.querySelectorAll('input[name="_page"]');
    for (var i = 0; i < pageFields.length; i++) {
      pageFields[i].value = window.location.href;
    }

    /* ---- Sticky header shadow ---- */
    var header = document.querySelector(".site-header");
    if (header) {
      var onScroll = function () {
        if (window.scrollY > 8) header.classList.add("scrolled");
        else header.classList.remove("scrolled");
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }

    /* ---- Mobile nav toggle ---- */
    var toggle = document.querySelector(".nav-toggle");
    var navLinks = document.getElementById("primary-nav");
    if (toggle && navLinks) {
      toggle.addEventListener("click", function () {
        var open = navLinks.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    /* ---- Mobile dropdown toggle ---- */
    var ddButtons = document.querySelectorAll(".has-dropdown > button");
    for (var d = 0; d < ddButtons.length; d++) {
      ddButtons[d].addEventListener("click", function (e) {
        if (window.matchMedia("(max-width: 860px)").matches) {
          e.preventDefault();
          var li = this.parentElement;
          li.classList.toggle("open");
          this.setAttribute("aria-expanded", li.classList.contains("open") ? "true" : "false");
        }
      });
    }

    /* ---- Plain-submission confirmation (?submitted=1) ---- */
    var params = new URLSearchParams(window.location.search);
    if (params.get("submitted") === "1") {
      showAllConfirmations();
      var first = document.querySelector(".cta-band, #contact");
      if (first && first.scrollIntoView) {
        window.setTimeout(function () { first.scrollIntoView({ behavior: "smooth", block: "start" }); }, 200);
      }
    }

    /* ---- AJAX lead form submissions ---- */
    var forms = document.querySelectorAll("form.lead-form");
    for (var f = 0; f < forms.length; f++) {
      forms[f].addEventListener("submit", handleSubmit);
    }

    function showAllConfirmations() {
      var statuses = document.querySelectorAll(".form-status");
      for (var s = 0; s < statuses.length; s++) statuses[s].classList.add("show");
    }

    function handleSubmit(e) {
      var form = e.target;
      if (!window.fetch || !window.FormData) return; /* fall back to native POST */
      e.preventDefault();

      var status = form.querySelector(".form-status");
      var error = form.querySelector(".form-error");
      if (error) error.classList.remove("show");

      var data = new FormData(form);
      /* ensure _page is current even if set later */
      data.set("_page", window.location.href);

      fetch(form.getAttribute("action"), {
        method: "POST",
        body: data,
        headers: { "Accept": "application/json" }
      })
        .then(function (res) {
          return res.json().catch(function () { return { ok: res.ok }; });
        })
        .then(function (json) {
          if (json && json.ok) {
            if (status) status.classList.add("show");
            form.reset();
            var pf = form.querySelector('input[name="_page"]');
            if (pf) pf.value = window.location.href;
          } else {
            if (error) error.classList.add("show");
          }
        })
        .catch(function () {
          if (error) error.classList.add("show");
        });
    }
  });
})();
