# Scode-Studio - QRcode Printer

A simple and efficient tool to generate and print QR codes to various outputs including files, console, and physical printers.

## Features

- **Generate QR Codes**: Create QR codes from any text or URL
- **Multiple Output Formats**: Save to image files (PNG), print to console, or send to physical printer
- **Styling Options**: Choose between standard or rounded QR code styles
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Command-Line Interface**: Easy to use CLI with comprehensive options

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ahmedseko/Scode-Studio.git
cd Scode-Studio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Examples

Generate a QR code and save to file:
```bash
python qrcode_printer.py -d "https://example.com" -o qrcode.png
```

Print QR code to console:
```bash
python qrcode_printer.py -d "Hello World" -c
```

Send QR code to default printer:
```bash
python qrcode_printer.py -d "https://example.com" -p
```

Generate QR code with rounded style:
```bash
python qrcode_printer.py -d "https://example.com" -o qrcode.png -s rounded
```

Send to specific printer:
```bash
python qrcode_printer.py -d "https://example.com" -p -n "PrinterName"
```

### Command-Line Options

```
-d, --data          Data to encode in the QR code (required)
-o, --output        Output file path for the QR code image
-c, --console       Print QR code to console
-p, --print         Send QR code to printer
-n, --printer-name  Name of the printer to use
-s, --style         Style of the QR code (standard or rounded)
```

### Advanced Usage

You can combine multiple output options:
```bash
# Save to file AND print to console
python qrcode_printer.py -d "https://example.com" -o qrcode.png -c

# Save to file AND send to printer
python qrcode_printer.py -d "https://example.com" -o qrcode.png -p
```

## Printer Support

The tool supports sending QR codes to physical printers on:
- **Windows**: Uses default Windows print functionality
- **macOS/Linux**: Uses `lpr` command (requires CUPS or similar print system)

Make sure your printer is properly configured in your operating system before using the print feature.

## Requirements

- Python 3.7 or higher
- qrcode[pil]>=7.4.2
- Pillow>=10.0.0

## Examples

### Generate QR Code for URL
```bash
python qrcode_printer.py -d "https://github.com/Ahmedseko/Scode-Studio" -o github.png
```

### Create WiFi QR Code
```bash
python qrcode_printer.py -d "WIFI:T:WPA;S:MyNetwork;P:MyPassword;;" -o wifi.png
```

### Generate Contact Information
```bash
python qrcode_printer.py -d "BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1234567890
EMAIL:john@example.com
END:VCARD" -o contact.png
```

## License

MIT License - feel free to use this project for any purpose.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
