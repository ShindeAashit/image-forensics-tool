# 🕵️ Automated Image Forensics Tool

This Python-based tool scans images for signs of manipulation using:
- 🔍 Error Level Analysis (ELA)
- 🧠 Metadata inspection
- 🧮 Perceptual hashing

## 📦 Features
- Detect tampered or edited images
- Extract EXIF metadata
- Generate ELA visualizations
- Display results in a GUI
- Save forensic reports

## 🛠 Installation

```bash
git clone https://github.com/ShindeAashit/image-forensics-tool.git
cd image-forensics-tool
pip install pillow piexif imagehash opencv-python

## 📂 Usage

Run the GUI:

python forensics.py

Select an image file (JPG, PNG)
View hash, metadata, and ELA result
Click “Open ELA Image” to inspect tampering

## 🧪 Techniques Used

ELA: Highlights compression artifacts to detect edits.
EXIF Metadata: Reveals camera info, timestamps, and software used.
Perceptual Hashing: Detects duplicates or subtle changes.

## 🔐 Security Use Cases

Validate authenticity of legal or journalistic images.
Detect fake uploads in enterprise systems.
Forensic analysis for cybersecurity teams.

## 📄 License

MIT License