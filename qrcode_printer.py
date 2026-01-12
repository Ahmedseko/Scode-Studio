#!/usr/bin/env python3
"""
QRcode Printer - Generate and print QR codes
"""

import argparse
import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image


class QRCodePrinter:
    """Class to handle QR code generation and printing"""
    
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    
    def generate_qrcode(self, data, output_file=None, style='standard'):
        """
        Generate a QR code from the given data
        
        Args:
            data (str): The data to encode in the QR code
            output_file (str): Optional file path to save the QR code image
            style (str): Style of QR code ('standard' or 'rounded')
            
        Returns:
            PIL.Image: The generated QR code image
        """
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        if style == 'rounded':
            img = self.qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer()
            )
        else:
            img = self.qr.make_image(fill_color="black", back_color="white")
        
        if output_file:
            img.save(output_file)
            print(f"QR code saved to: {output_file}")
        
        return img
    
    def print_to_console(self, data):
        """
        Print QR code to console using ASCII characters
        
        Args:
            data (str): The data to encode in the QR code
        """
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        # Print to console
        matrix = self.qr.get_matrix()
        for row in matrix:
            line = ""
            for cell in row:
                line += "██" if cell else "  "
            print(line)
    
    def send_to_printer(self, data, printer_name=None):
        """
        Send QR code to a physical printer
        
        Args:
            data (str): The data to encode in the QR code
            printer_name (str): Optional printer name
            
        Note:
            This creates a temporary image and uses system print commands.
            Actual printer integration depends on the operating system.
        """
        import tempfile
        import os
        import platform
        
        # Generate QR code to temporary file
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            self.generate_qrcode(data, tmp_path)
            
            # Platform-specific printing
            system = platform.system()
            
            if system == 'Windows':
                # Windows printing
                import subprocess
                if printer_name:
                    subprocess.run(['mspaint', '/pt', tmp_path, printer_name])
                else:
                    os.startfile(tmp_path, 'print')
                print(f"Sending QR code to printer...")
                
            elif system == 'Darwin':  # macOS
                import subprocess
                cmd = ['lpr']
                if printer_name:
                    cmd.extend(['-P', printer_name])
                cmd.append(tmp_path)
                subprocess.run(cmd, check=True)
                print(f"Sending QR code to printer...")
                
            elif system == 'Linux':
                import subprocess
                cmd = ['lpr']
                if printer_name:
                    cmd.extend(['-P', printer_name])
                cmd.append(tmp_path)
                subprocess.run(cmd, check=True)
                print(f"Sending QR code to printer...")
                
            else:
                print(f"Printing not supported on {system}. Please save the QR code as a file and print manually.")
                print(f"QR code saved to: {tmp_path}")
                return
                
        except Exception as e:
            print(f"Error sending to printer: {e}")
            print(f"QR code saved to: {tmp_path}")


def main():
    """Main function to handle command-line interface"""
    parser = argparse.ArgumentParser(
        description='QRcode Printer - Generate and print QR codes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate QR code and save to file
  python qrcode_printer.py -d "https://example.com" -o qrcode.png
  
  # Print QR code to console
  python qrcode_printer.py -d "Hello World" -c
  
  # Send QR code to printer
  python qrcode_printer.py -d "https://example.com" -p
  
  # Generate rounded style QR code
  python qrcode_printer.py -d "https://example.com" -o qrcode.png -s rounded
        """
    )
    
    parser.add_argument(
        '-d', '--data',
        required=True,
        help='Data to encode in the QR code'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file path for the QR code image'
    )
    
    parser.add_argument(
        '-c', '--console',
        action='store_true',
        help='Print QR code to console'
    )
    
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Send QR code to printer'
    )
    
    parser.add_argument(
        '-n', '--printer-name',
        help='Name of the printer to use'
    )
    
    parser.add_argument(
        '-s', '--style',
        choices=['standard', 'rounded'],
        default='standard',
        help='Style of the QR code (default: standard)'
    )
    
    args = parser.parse_args()
    
    # Create QRCodePrinter instance
    printer = QRCodePrinter()
    
    try:
        # Handle different output modes
        if args.console:
            printer.print_to_console(args.data)
        
        if args.output:
            printer.generate_qrcode(args.data, args.output, args.style)
        
        if args.print:
            printer.send_to_printer(args.data, args.printer_name)
        
        # If no output mode specified, default to saving to file
        if not args.console and not args.output and not args.print:
            output_file = 'qrcode.png'
            printer.generate_qrcode(args.data, output_file, args.style)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
