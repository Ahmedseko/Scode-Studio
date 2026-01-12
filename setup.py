from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scode-qrcode-printer",
    version="1.0.0",
    author="Scode Studio",
    description="A tool to generate and print QR codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ahmedseko/Scode-Studio",
    py_modules=["qrcode_printer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "qrcode[pil]>=7.4.2",
        "Pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "qrcode-printer=qrcode_printer:main",
        ],
    },
)
