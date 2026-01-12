#!/usr/bin/env python3
"""
Unit tests for QRcode Printer
"""

import unittest
import os
import tempfile
from qrcode_printer import QRCodePrinter


class TestQRCodePrinter(unittest.TestCase):
    """Test cases for QRCodePrinter class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.printer = QRCodePrinter()
        self.test_data = "https://github.com/Ahmedseko/Scode-Studio"
        
    def test_generate_qrcode_creates_file(self):
        """Test that QR code generation creates a file"""
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            self.printer.generate_qrcode(self.test_data, tmp_path)
            self.assertTrue(os.path.exists(tmp_path))
            self.assertGreater(os.path.getsize(tmp_path), 0)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_generate_qrcode_standard_style(self):
        """Test QR code generation with standard style"""
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            img = self.printer.generate_qrcode(self.test_data, tmp_path, style='standard')
            self.assertIsNotNone(img)
            self.assertTrue(os.path.exists(tmp_path))
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_generate_qrcode_rounded_style(self):
        """Test QR code generation with rounded style"""
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            img = self.printer.generate_qrcode(self.test_data, tmp_path, style='rounded')
            self.assertIsNotNone(img)
            self.assertTrue(os.path.exists(tmp_path))
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_generate_qrcode_without_output_file(self):
        """Test QR code generation without saving to file"""
        img = self.printer.generate_qrcode(self.test_data)
        self.assertIsNotNone(img)
    
    def test_print_to_console(self):
        """Test console printing doesn't raise exceptions"""
        try:
            self.printer.print_to_console("Test Data")
        except Exception as e:
            self.fail(f"print_to_console raised {type(e).__name__} unexpectedly!")
    
    def test_qrcode_with_special_characters(self):
        """Test QR code generation with special characters"""
        special_data = "Hello! @#$%^&*() 你好 🚀"
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            img = self.printer.generate_qrcode(special_data, tmp_path)
            self.assertIsNotNone(img)
            self.assertTrue(os.path.exists(tmp_path))
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_qrcode_with_long_text(self):
        """Test QR code generation with long text"""
        long_data = "A" * 1000
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            img = self.printer.generate_qrcode(long_data, tmp_path)
            self.assertIsNotNone(img)
            self.assertTrue(os.path.exists(tmp_path))
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


if __name__ == '__main__':
    unittest.main()
