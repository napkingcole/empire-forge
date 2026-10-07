# Empire Forge website

The public site for [AOE2: Empire Forge](https://github.com/napkingcole/aoe2-empire-forge):
https://napkingcole.github.io/empire-forge/

Jekyll, published by GitHub Pages from `main`. The look is the app's plaster theme
(`aoe2civbuilder/static/css/plaster.css`), carried into `assets/css/site.css`.

## Preview locally

    bundle install
    bundle exec jekyll serve --baseurl /empire-forge

then open http://127.0.0.1:4000/empire-forge/

## When the app ships a release

The Changelog page reads `_data/changelog.json`, copied from the app's `CHANGELOG`
in `aoe2civbuilder/app.py` (the same notes the in-app "what's new" shows):

    python3 _scripts/sync_changelog.py ../aoe2civbuilder

Commit and push; Pages rebuilds in a minute or two.

## When the Microsoft Store listing goes live

Set `store_url` in `_config.yml`. The Download page swaps "coming soon" for the Store button.
