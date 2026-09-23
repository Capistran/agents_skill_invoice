import json
import tempfile
import unittest
from pathlib import Path

from tools.fiscal_changes import compare_source, content_hash


class FiscalChangesTests(unittest.TestCase):
    def test_content_hash_is_stable(self):
        self.assertEqual(content_hash(b"same"), content_hash(b"same"))
        self.assertNotEqual(content_hash(b"same"), content_hash(b"different"))

    def test_fixture_is_new_then_unchanged_then_changed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixtures = root / "fixtures"
            state = root / "state"
            fixtures.mkdir()
            source = {"id": "example", "url": "https://example.invalid", "title": "Example"}
            fixture = fixtures / "example.html"
            fixture.write_text("one", encoding="utf-8")

            first = compare_source(source, state, fixtures)
            second = compare_source(source, state, fixtures)
            fixture.write_text("two", encoding="utf-8")
            third = compare_source(source, state, fixtures)

            self.assertEqual(first.status, "new")
            self.assertEqual(second.status, "unchanged")
            self.assertEqual(third.status, "changed")
            saved = json.loads((state / "example.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["content_hash"], content_hash(b"two"))


if __name__ == "__main__":
    unittest.main()