# @author Daniel McCoy Stephenson
"""Build the browser version of Mimicking Animation: web/index.html and web/game.zip.

The game runs unmodified in the browser under tak's console runtime
(https://github.com/Stephenson-Software/tak, tak.web.console): its prompts and
output go to a terminal on the page, and any file it writes is kept in the
browser. Needs tak installed (see .github/workflows/browser.yml). Serve the
result cross-origin isolated, e.g. with arcade or tak.web.serve:

    python3 web/build_zip.py
    python3 -c "from tak.web.serve import main; main(root='.', title='Mimicking Animation')"
"""

import os

from tak.web.bundle import build
from tak.web.console import page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "web", "index.html"), "w", encoding="utf-8") as out:
    out.write(
        page(
            title='Mimicking Animation',
            tagline='An ASCII stick figure walks across the screen (2017)',
            entry='mimickingAnimation.py',
            idbName='mimicking-animation-files',
            footer='More by Daniel Stephenson &rarr; <a href="https://danielstephenson.dev/play">danielstephenson.dev/play</a>',
        )
    )

build(root=ROOT, sourceDirectories=(), extraFiles=('mimickingAnimation.py', 'version.txt'))
