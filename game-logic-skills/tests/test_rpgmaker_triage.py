"""Synthetic RPG Maker MV/MZ triage fixtures: no proprietary game assets required."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "analyze-game-logic/scripts/rpgmaker_triage.py"
spec = importlib.util.spec_from_file_location("rpgmaker_triage", SCRIPT)
triage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(triage)


class RPGMakerTriageTest(unittest.TestCase):
    def fixture(self, inner=""):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        p = Path(temp.name) / inner
        (p / "js").mkdir(parents=True, exist_ok=True)
        (p / "data").mkdir(exist_ok=True)
        return Path(temp.name), p

    def test_mz_under_www(self):
        root, p = self.fixture("www")
        (p / "js/rmmz_core.js").write_text("// MZ")
        (p / "data/System.json").write_text("{}")
        (p / "js/plugins.js").write_text(
            'var $plugins = [{"name":"A","status":true,"parameters":{}},'
            '{"name":"B","status":false,"parameters":{}}];')
        (p / "js/plugins").mkdir()
        (p / "js/plugins/A.js").write_text("Game_Action.prototype.apply = function() {};")
        (p / "data/Map001.json").write_text(
            '{"events":[null,{"id":1,"pages":[{"list":'
            '[{"code":357,"parameters":["A","set","Label",{"x":"42"}]}]}]}]}')
        report = triage.triage(root, with_events=True, with_hooks=True)
        self.assertEqual(report["engine"], "MZ")
        self.assertEqual(report["confidence"], "high")
        self.assertEqual([p["enabled"] for p in report["plugins"]], [True, False])
        self.assertEqual(report["event_inventory"]["code_counts"]["mz_plugin_command"], 1)
        self.assertEqual(report["hook_inventory"]["indicators"][0]["method"], "apply")

    def test_mv_plugin_command(self):
        root, p = self.fixture()
        (p / "js/rpg_core.js").write_text("// MV")
        (p / "data/System.json").write_text("{}")
        (p / "data/CommonEvents.json").write_text(
            '[null,{"id":1,"list":[{"code":356,"parameters":["Foo bar"]}]}]')
        report = triage.triage(root, with_events=True)
        self.assertEqual(report["engine"], "MV")
        self.assertEqual(report["event_inventory"]["code_counts"]["mv_plugin_command"], 1)

    def test_generic_web_is_not_rpgmaker(self):
        root, p = self.fixture()
        (p / "index.html").write_text('<script src="game.js"></script>')
        (p / "data/System.json").write_text("{}")
        self.assertEqual(triage.triage(root)["engine"], "unknown")

    def test_mixed_cores_remains_ambiguous(self):
        root, p = self.fixture()
        (p / "js/rpg_core.js").write_text("// MV")
        (p / "js/rmmz_core.js").write_text("// MZ")
        (p / "data/System.json").write_text("{}")
        self.assertEqual(triage.triage(root)["engine"], "ambiguous")

    def test_conflicting_project_markers_remain_ambiguous(self):
        root, p = self.fixture()
        (p / "js/rpg_core.js").write_text("// MV")
        (p / "Game.rmmzproject").write_text("")
        (p / "data/System.json").write_text("{}")
        self.assertEqual(triage.triage(root)["engine"], "ambiguous")

    def test_does_not_execute_javascript_manifest(self):
        root, p = self.fixture()
        (p / "js/rmmz_core.js").write_text("// MZ")
        (p / "data/System.json").write_text("{}")
        (p / "js/plugins.js").write_text("var $plugins = [getPluginFromUntrustedCode()];")
        report = triage.triage(root)
        self.assertEqual(report["plugins"], [])
        self.assertTrue(any("Cannot parse" in w for w in report["warnings"]))

    def test_unsafe_plugin_name_does_not_escape_plugin_folder(self):
        root, p = self.fixture()
        (p / "js/rmmz_core.js").write_text("// MZ")
        (p / "data/System.json").write_text("{}")
        (p / "js/plugins.js").write_text(
            'var $plugins = [{"name":"../outside","status":true,"parameters":{}}];')
        report = triage.triage(root, with_hooks=True)
        self.assertEqual(report["hook_inventory"]["indicators"], [])
        self.assertTrue(any("unsafe plugin name" in w for w in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
