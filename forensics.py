import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageChops
import piexif
import imagehash
import os
import webbrowser

DEFAULT_IMAGE_DIR = "E:/vsc/python projects/image-forensics-tool/input_images"

def perform_ela(image_path, quality=90):
    original = Image.open(image_path).convert('RGB')
    temp_path = image_path.replace('.jpg', '_temp.jpg')
    original.save(temp_path, 'JPEG', quality=quality)
    compressed = Image.open(temp_path)
    ela_image = ImageChops.difference(original, compressed)
    ela_image = ela_image.point(lambda p: p * 10)
    ela_path = image_path.replace('.jpg', '_ela.jpg')
    ela_image.save(ela_path)
    os.remove(temp_path)
    return ela_path

def extract_metadata(image_path):
    try:
        exif_data = piexif.load(image_path)
        return {k.decode(): str(v) for k, v in exif_data['0th'].items()}
    except Exception:
        return {"Error": "No metadata found or unsupported format."}

def compute_hash(image_path):
    try:
        return str(imagehash.average_hash(Image.open(image_path)))
    except Exception:
        return "Error computing hash."

def analyze_image():
    file_path = filedialog.askopenfilename(initialdir=DEFAULT_IMAGE_DIR,
                                           title="Select Image",
                                           filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    ela_path = perform_ela(file_path)
    metadata = extract_metadata(file_path)
    hash_val = compute_hash(file_path)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"📁 File: {file_path}\n\n")
    result_text.insert(tk.END, f"🔍 Hash: {hash_val}\n\n")
    result_text.insert(tk.END, "📜 Metadata:\n")
    for k, v in metadata.items():
        result_text.insert(tk.END, f"{k}: {v}\n")

    def open_ela():
        webbrowser.open(ela_path)

    open_button.config(command=open_ela)
    open_button.pack(pady=5)

# 🖼️ GUI Setup
root = tk.Tk()
root.title("🕵️ Image Forensics Tool")
root.geometry("600x500")

title = tk.Label(root, text="Automated Image Forensics", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

analyze_button = tk.Button(root, text="Select Image & Analyze", command=analyze_image,
                           bg="#4CAF50", fg="white", font=("Helvetica", 12))
analyze_button.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, font=("Courier", 10))
result_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

open_button = tk.Button(root, text="Open ELA Image", bg="#2196F3", fg="white", font=("Helvetica", 12))

root.mainloop()