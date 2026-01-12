#!/usr/bin/env python3
"""
Example script demonstrating various uses of the QRcode Printer
"""

import sys
import os

# Add parent directory to path to import qrcode_printer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qrcode_printer import QRCodePrinter

def main():
    printer = QRCodePrinter()
    
    # Create examples directory if it doesn't exist
    os.makedirs('examples', exist_ok=True)
    
    print("Generating example QR codes...")
    print("-" * 50)
    
    # Example 1: Simple URL
    print("\n1. Generating QR code for URL...")
    printer.generate_qrcode(
        "https://github.com/Ahmedseko/Scode-Studio",
        "examples/github_url.png"
    )
    
    # Example 2: WiFi credentials
    print("\n2. Generating WiFi QR code...")
    wifi_data = "WIFI:T:WPA;S:MyNetwork;P:MyPassword123;;"
    printer.generate_qrcode(wifi_data, "examples/wifi_credentials.png")
    
    # Example 3: Contact information (vCard)
    print("\n3. Generating contact vCard QR code...")
    vcard_data = """BEGIN:VCARD
VERSION:3.0
FN:John Doe
ORG:Scode Studio
TEL:+1234567890
EMAIL:john.doe@example.com
URL:https://example.com
END:VCARD"""
    printer.generate_qrcode(vcard_data, "examples/contact_card.png")
    
    # Example 4: Simple text
    print("\n4. Generating text QR code...")
    printer.generate_qrcode(
        "Hello from Scode Studio QR Code Printer!",
        "examples/hello_text.png"
    )
    
    # Example 5: Rounded style QR code
    print("\n5. Generating rounded style QR code...")
    printer.generate_qrcode(
        "https://example.com",
        "examples/rounded_style.png",
        style='rounded'
    )
    
    # Example 6: Print to console
    print("\n6. Printing QR code to console...")
    print("Console QR Code for: 'Test'")
    printer.print_to_console("Test")
    
    print("\n" + "-" * 50)
    print("All examples generated successfully!")
    print("Check the 'examples' directory for the generated QR codes.")

if __name__ == '__main__':
    main()
