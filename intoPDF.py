import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import os
from PIL import Image

SUPPORTED_EXTENSIONS = [("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("PSD files", "*.psd")]

def convert_images_to_pdf(input_files, output_folder):
    total_files = len(input_files)
    progress_bar['maximum'] = total_files
    
    for idx, file_path in enumerate(input_files, start=1):
        _, ext = os.path.splitext(file_path)
        if ext.lower() == ".psd":
            im = Image.open(file_path)
            pdf_path = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + ".pdf")
            im.save(pdf_path, "PDF", resolution=100.0, save_all=True)
        else:
            im = Image.open(file_path)
            pdf_path = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + ".pdf")
            im.save(pdf_path, "PDF", resolution=100.0)
        
        progress_bar['value'] = idx
        progress_label.config(text=f"Converting {idx}/{total_files} images...")
        root.update_idletasks()

    progress_label.config(text="Conversion completed!")

def browse_files():
    files = filedialog.askopenfilenames(filetypes=SUPPORTED_EXTENSIONS)
    files_listbox.delete(0, tk.END)
    for file_path in files:
        files_listbox.insert(tk.END, file_path)

def browse_output_folder():
    folder_path.set(filedialog.askdirectory())

def convert_button_clicked():
    input_files = files_listbox.get(0, tk.END)
    output_folder = folder_path.get()
    convert_images_to_pdf(input_files, output_folder)

# Create GUI
root = tk.Tk()
root.title("Image to PDF Converter")

files_frame = tk.Frame(root)
files_frame.pack(fill=tk.BOTH, expand=True)

files_label = tk.Label(files_frame, text="Select image files:")
files_label.pack()

files_listbox = tk.Listbox(files_frame, selectmode=tk.MULTIPLE)
files_listbox.pack(fill=tk.BOTH, expand=True)

files_scrollbar = tk.Scrollbar(files_frame, orient=tk.VERTICAL)
files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
files_listbox.config(yscrollcommand=files_scrollbar.set)
files_scrollbar.config(command=files_listbox.yview)

files_browse_button = tk.Button(files_frame, text="Browse", command=browse_files)
files_browse_button.pack()

output_folder_label = tk.Label(root, text="Select output folder:")
output_folder_label.pack()

folder_path = tk.StringVar()

output_entry = tk.Entry(root, textvariable=folder_path)
output_entry.pack()

output_browse_button = tk.Button(root, text="Browse", command=browse_output_folder)
output_browse_button.pack()

convert_button = tk.Button(root, text="Convert to PDF", command=convert_button_clicked)
convert_button.pack()

progress_label = tk.Label(root, text="")
progress_label.pack()

progress_bar = Progressbar(root, length=200, mode='determinate')
progress_bar.pack()

root.mainloop()
