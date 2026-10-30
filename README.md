# Mimicking Animation

[![View on danielstephenson.dev](https://img.shields.io/badge/View%20on-danielstephenson.dev-2ea44f)](https://danielstephenson.dev/projects/mimicking-animation)

An ASCII stick figure walks across the terminal, one frame every 0.2 seconds, by printing blank lines and shifting the figure one space each frame. It alternates between two poses:
```
  O
 /|\
 / \

  \O/
   |_
   \
```

Written by Daniel McCoy Stephenson in April 2017, as one of his first programs. It is part of the "First Programs" collection on [danielstephenson.dev/play](https://danielstephenson.dev/play).

## Running it
```
python3 mimickingAnimation.py
```
It also still runs under Python 2 (`python2 mimickingAnimation.py`), which it was written for. The figure needs a terminal about 80 columns wide; on a phone, turn it sideways.

## Play in your browser
The program runs in a browser tab under [tak](https://github.com/Stephenson-Software/tak)'s console runtime (Python via Pyodide): https://mimicking-animation.play.danielstephenson.dev, listed with the rest at [danielstephenson.dev/play](https://danielstephenson.dev/play).

The only changes made for this were turning its Python 2 `print` statements into `print(...)` calls and writing the figure's `\O/` as `\\O/` (Python 3 warns about the unescaped backslash). Both print the same text under Python 2 and Python 3. To build and serve it locally, install `tak` at the commit CI pins, then build and serve:
```
pip install "tak @ git+https://github.com/Stephenson-Software/tak@9b539d8760e2c02cc262a7dcff6d0c541572ab71"
python3 web/build_zip.py
python3 -c "from tak.web.serve import main; main(root='.', title='Mimicking Animation')"
```
Every pull request runs the program under Python 3 and builds the bundle. Pushes to `master` deploy it to [arcade](https://github.com/Stephenson-Software/arcade) once the org variable `ARCADE_ENABLED` is `true`, and it can also be deployed by hand from the Actions tab (`.github/workflows/browser.yml`).
