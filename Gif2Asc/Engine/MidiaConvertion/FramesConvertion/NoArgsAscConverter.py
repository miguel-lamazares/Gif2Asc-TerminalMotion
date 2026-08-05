#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "TermForge"))

from TermForge.termforge.Terminal import confirm
from AscConverter import _wizard, render, CFG_PATH


if __name__ == "__main__":
    if (
        CFG_PATH.exists()
        and "--force-wizard" not in sys.argv
        and confirm("\nUse existing configuration?")
    ):
        cfg = json.loads(CFG_PATH.read_text())

        if confirm("\nRender frames now with these settings?"):
            render(cfg)

        cfg = _wizard()
        sys.exit(0)

    

    