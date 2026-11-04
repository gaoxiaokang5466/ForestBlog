#!/usr/bin/env python3
"""Smoke tests for the ForestBlog repository layout.

Run with: python3 test.py
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif"}


class RepositoryLayoutTest(unittest.TestCase):
    def test_readme_exists(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file())
        self.assertGreater(readme.stat().st_size, 0)

    def test_maven_project_exists(self):
        pom = ROOT / "ForestBlog" / "pom.xml"
        self.assertTrue(pom.is_file())
        self.assertIn("<artifactId>ForestBlog</artifactId>", pom.read_text(encoding="utf-8"))

    def test_source_tree_exists(self):
        src = ROOT / "ForestBlog" / "src"
        self.assertTrue(src.is_dir())
        for relative in ("main/java", "main/resources", "main/webapp", "test/java"):
            with self.subTest(relative=relative):
                self.assertTrue((src / relative).is_dir())

    def test_database_dump_exists(self):
        dump = ROOT / "forest_blog.sql"
        self.assertTrue(dump.is_file())
        self.assertGreater(dump.stat().st_size, 0)
        with dump.open(encoding="utf-8", errors="ignore") as sql_file:
            self.assertIn("CREATE TABLE", sql_file.read(4096))

    def test_uploaded_images_exist(self):
        uploads = ROOT / "uploads"
        self.assertTrue(uploads.is_dir())
        images = [path for path in uploads.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES]
        self.assertGreater(len(images), 0)


if __name__ == "__main__":
    unittest.main()
