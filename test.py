#!/usr/bin/env python3
"""Smoke tests for the ForestBlog repository layout.

Run with: python3 test.py
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class RepositoryLayoutTest(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue((ROOT / "README.md").is_file())

    def test_maven_project_exists(self):
        self.assertTrue((ROOT / "ForestBlog" / "pom.xml").is_file())

    def test_source_tree_exists(self):
        self.assertTrue((ROOT / "ForestBlog" / "src").is_dir())

    def test_database_dump_exists(self):
        dump = ROOT / "forest_blog.sql"
        self.assertTrue(dump.is_file())
        self.assertGreater(dump.stat().st_size, 0)

    def test_uploaded_images_exist(self):
        uploads = ROOT / "uploads"
        self.assertTrue(uploads.is_dir())
        self.assertTrue(any(uploads.glob("*.png")))


if __name__ == "__main__":
    unittest.main()
