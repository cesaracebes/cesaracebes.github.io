(function () {
  var root = document.documentElement;

  // Day / night toggle ------------------------------------------------------
  var btn = document.querySelector(".theme-toggle");
  function paint() {
    if (!btn) return;
    var night = root.getAttribute("data-theme") !== "day";
    btn.textContent = night ? btn.dataset.toDay : btn.dataset.toNight;
    btn.setAttribute("aria-label", night ? btn.dataset.toDayLabel : btn.dataset.toNightLabel);
  }
  if (btn) {
    btn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "day" ? "night" : "day";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (_) {}
      paint();
    });
  }
  paint();

  // Case filters ------------------------------------------------------------
  var grid = document.querySelector("[data-filterable]");
  var chips = document.querySelectorAll(".chip[data-filter]");
  if (grid && chips.length) {
    var tiles = grid.querySelectorAll(".tile");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var f = chip.dataset.filter;
        chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
        tiles.forEach(function (tile) {
          var show = f === "all" || tile.dataset.spec === f;
          tile.hidden = !show;
          tile.classList.toggle("big", f === "all" && tile === tiles[0]);
        });
      });
    });
  }
})();
