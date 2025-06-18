"""
Unit tests for the table of contents generator script.
Tests the functionality of extracting titles from markdown files and handling various edge cases.
"""

import unittest
from pathlib import Path
import tempfile
import shutil
import os
from .update_toc import extract_title_from_md


class TestUpdateTOC(unittest.TestCase):
    """Test suite for the table of contents generator."""

    def setUp(self):
        """Create a temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
        self.eng_mgmt_dir = Path(self.test_dir) / "engineering_management"
        self.eng_mgmt_dir.mkdir()

    def tearDown(self):
        """Clean up temporary directory after tests."""
        shutil.rmtree(self.test_dir)

    def test_extract_title_from_md(self):
        """Test title extraction from markdown files with various formats."""
        test_cases = [
            ("# Simple Title", "Simple Title"),
            ("# Title with Emoji 📚", "Title with Emoji 📚"),
            ("Text before\n# Title Here\nText after", "Title Here"),
            ("No title here", None),
            ("## Secondary heading", None),
        ]

        for content, expected_title in test_cases:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".md", delete=False
            ) as temp_file:
                temp_file.write(content)

            result = extract_title_from_md(temp_file.name)
            os.unlink(temp_file.name)  # Clean up temp file

            self.assertEqual(result, expected_title)

    def test_file_with_no_read_permission(self):
        """Test handling of files without read permissions."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False
        ) as temp_file:
            temp_file.write("# Test Title")

        os.chmod(temp_file.name, 0o000)  # Remove read permissions
        result = extract_title_from_md(temp_file.name)
        os.chmod(temp_file.name, 0o666)  # Restore permissions for cleanup
        os.unlink(temp_file.name)

        self.assertIsNone(result)

    def test_with_sample_files(self):
        """Test title extraction with a set of sample markdown files."""
        files_content = {
            "1_CALMS.md": "# 📘 Lesson 1: CALMS Framework\nContent here",
            "2_DevOps.md": "# Lesson 2: DevOps Practices\nMore content",
            "no_title.md": "Just some content\nNo title here",
        }

        for filename, content in files_content.items():
            file_path = self.eng_mgmt_dir / filename
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

        # Test each file
        self.assertEqual(
            extract_title_from_md(self.eng_mgmt_dir / "1_CALMS.md"),
            "📘 Lesson 1: CALMS Framework",
        )
        self.assertEqual(
            extract_title_from_md(self.eng_mgmt_dir / "2_DevOps.md"),
            "Lesson 2: DevOps Practices",
        )
        self.assertIsNone(extract_title_from_md(self.eng_mgmt_dir / "no_title.md"))


if __name__ == "__main__":
    unittest.main()
