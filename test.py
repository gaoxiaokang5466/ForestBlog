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


if __name__ == "__main__":
    unittest.main()
