#!/usr/bin/env python3
"""Copy the app's release notes into _data/changelog.json for the Changelog page.

The app's CHANGELOG dict (aoe2civbuilder/app.py) is the single source of truth:
it already drives the in-app "what's new" modal.  This reads it with ast (no
Flask import needed) and adds each release's publish date from GitHub.

    python3 _scripts/sync_changelog.py [path/to/aoe2civbuilder]
"""
import ast
import json
import sys
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
APP = Path(sys.argv[1]) if len(sys.argv) > 1 else SITE.parent / "aoe2civbuilder"
REPO = "napkingcole/aoe2-empire-forge"

tree = ast.parse((APP / "app.py").read_text(encoding="utf-8"))
notes = None
for node in tree.body:
    target = getattr(node, "target", None) or (node.targets[0] if isinstance(node, ast.Assign) else None)
    if getattr(target, "id", None) == "CHANGELOG":
        notes = ast.literal_eval(node.value)
        break
if notes is None:
    sys.exit("CHANGELOG not found in app.py")

dates = {}
try:
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/releases?per_page=100",
                                 headers={"User-Agent": "empire-forge-site"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        for r in json.loads(resp.read().decode("utf-8")):
            dates[r["tag_name"].lstrip("vV")] = r["published_at"][:10]
except OSError as e:
    print(f"warning: no release dates ({e})")

releases = [{"version": v, "date": dates.get(v, ""), "notes": items} for v, items in notes.items()]
out = SITE / "_data" / "changelog.json"
out.write_text(json.dumps(releases, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {len(releases)} releases to {out.relative_to(SITE)}")
