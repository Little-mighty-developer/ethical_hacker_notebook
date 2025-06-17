import unittest
from pathlib import Path
import tempfile
import shutil
import os
from update_toc import extract_title_from_md

class TestUpdateTOC(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.eng_mgmt_dir = Path(self.test_dir) / "engineering_management"
        self.eng_mgmt_dir.mkdir()

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_extract_title_from_md(self):
        # Test cases for title extraction
        test_cases = [
            ("# Simple Title", "Simple Title"),
            ("# Title with Emoji 📚", "Title with Emoji 📚"),
            ("Text before\n# Title Here\nText after", "Title Here"),
            ("No title here", None),
            ("## Secondary heading", None),
        ]

        for content, expected_title in test_cases:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                f.write(content)
            
            result = extract_title_from_md(f.name)
            os.unlink(f.name)  # Clean up temp file
            
            self.assertEqual(result, expected_title)

    def test_file_with_no_read_permission(self):
        # Test handling of files that can't be read
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Test Title")
        
        os.chmod(f.name, 0o000)  # Remove read permissions
        result = extract_title_from_md(f.name)
        os.chmod(f.name, 0o666)  # Restore permissions for cleanup
        os.unlink(f.name)
        
        self.assertIsNone(result)

    def test_with_sample_files(self):
        # Create some test markdown files
        files_content = {
            "1_CALMS.md": "# 📘 Lesson 1: CALMS Framework\nContent here",
            "2_DevOps.md": "# Lesson 2: DevOps Practices\nMore content",
            "no_title.md": "Just some content\nNo title here",
        }

        for filename, content in files_content.items():
            file_path = self.eng_mgmt_dir / filename
            with open(file_path, 'w') as f:
                f.write(content)

        # Test each file
        self.assertEqual(
            extract_title_from_md(self.eng_mgmt_dir / "1_CALMS.md"),
            "📘 Lesson 1: CALMS Framework"
        )
        self.assertEqual(
            extract_title_from_md(self.eng_mgmt_dir / "2_DevOps.md"),
            "Lesson 2: DevOps Practices"
        )
        self.assertIsNone(
            extract_title_from_md(self.eng_mgmt_dir / "no_title.md")
        )

if __name__ == '__main__':
    unittest.main() 