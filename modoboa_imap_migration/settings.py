"""Default app settings."""

import os

PLUGIN_BASE_DIR = os.path.dirname(__file__)

STATS_FILE = os.path.join(
    PLUGIN_BASE_DIR, "static/modoboa_imap_migration/webpack-stats.json")


def apply(settings):
    """Modify settings."""
    DEBUG = settings["DEBUG"]
    if "webpack_loader" not in settings["INSTALLED_APPS"]:
        settings["INSTALLED_APPS"] += ("webpack_loader", )
    wpl_config = {
        "IMAP_MIGRATION": {
            "CACHE": not DEBUG,
            "BUNDLE_DIR_NAME": "modoboa_imap_migration/",
            "STATS_FILE": STATS_FILE,
            "IGNORE": [r".+\.hot-update.js", r".+\.map"]
        }
    }
    if "WEBPACK_LOADER" in settings:
        settings["WEBPACK_LOADER"].update(wpl_config)
    else:
        settings["WEBPACK_LOADER"] = wpl_config
