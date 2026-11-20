# cesaracebes.github.io

Personal portfolio of César Acebes Pinilla, in English, Spanish and Catalan, with a day/night mode.
It is a static site with no dependencies: Python 3 and the standard library are enough.

## Structure

```
_source/content.py          ← all the content (texts in 3 languages, cases, publications, videos)
_source/build.py            ← generates the pages from content.py
_source/check-overflow.html ← checks that no text overflows or breaks (all pages, 5 widths)
assets/css/style.css        ← design (night = acid, day = coral)
assets/js/site.js           ← day/night button and case filters
assets/img/                 ← images (put the papers' figures and case photos here)
en/ es/ ca/                 ← generated pages (don't edit them by hand)
```

## Edit content

1. Change `_source/content.py`. A text with `{"en": …, "es": …, "ca": …}` is translated; a plain text is the same in all three languages.
2. Rebuild:

   ```
   python3 _source/build.py
   ```

### Add a video or a 3D model (YouTube, Vimeo, Sketchfab)

In `content.py`, find the case and fill in its `video`:

```python
{"spec": "thoracic",   "video": {"provider": "youtube",   "id": "stNos5ewD_0"}, ...}
{"spec": "colorectal", "video": {"provider": "vimeo",     "id": "123456789"}, ...}
{"spec": "endocrine",  "video": {"provider": "sketchfab", "id": "fe41334f6b334e5c872a4d837e4ae0ad"}, ...}
```

- **YouTube** (upload as *Unlisted*): the `id` is what follows `youtu.be/`. It plays silently on a loop, with no controls.
- **Sketchfab**: the `id` is the 32 characters at the end of the model's URL. The tile shows the model's
  thumbnail with a play button and loads the interactive viewer on click (keeps the page light).
- The title appears when the mouse hovers over the tile. If the `id` is empty, the site shows a "Video coming soon" tile.

The same `{"provider", "id"}` works in `PLANNING["reel"]` (summary video), `PLANNING["twin_uses"]`
(digital twin) and, wrapped as `{"video": {...}}`, in the third element of each `DEVICES["gallery"]` item.

Cases: the first tile is the big one on /planning and the first 6 fill the home mosaic. `"wide": True`
makes a tile double width (used for the last two so the grid closes in full rows).

### Add an image

Copy it to `assets/img/…` (JPEG, ~1400 px wide, no metadata) and point to it with `"image": "assets/img/…"`:
in a case (instead of a video), in `PUBLICATIONS` (thumbnails on the AI page), in `AI["hero_media"]`,
or as `{"image": …}` in a `DEVICES["gallery"]` item. Paper figures are shown whole on a white plate.

Never publish images with patient identifiers (names, record numbers, dates, case IDs burned into the render).

### Printers and flags

- `DEVICES["printers"]`: one card per printing process with a schematic diagram drawn in `build.py` (`PRINTER_SVG`).
- `REGULATORY["framework"]`: `(jurisdiction, key, text)`; each jurisdiction (`eu`, `es`, `cat`) opens with a
  schematic flag (`FLAG_SVG` in `build.py`). Both use the theme colours, so they follow day/night.

## Preview locally

```
python3 -m http.server 8765
```

and open http://localhost:8765/es/ (add `?theme=day` or `?theme=night` to force a mode).

To check that no text overflows, open http://localhost:8765/_source/check-overflow.html: when it finishes it shows `NO OVERFLOW` or a list of problems
(the only accepted one is "custom-made" breaking at its own hyphen at 390 px).

## Publish on GitHub Pages

1. On GitHub, create an **empty public** repository named exactly `cesaracebes.github.io`.
2. From this folder:

   ```
   git add -A
   git commit -m "Portfolio"
   git remote add origin https://github.com/cesaracebes/cesaracebes.github.io.git
   git push -u origin main
   ```

3. In the repository: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`**.
4. In a minute it will be at https://cesaracebes.github.io

For each later change: `python3 _source/build.py`, then `git add -A && git commit -m "…" && git push`.
