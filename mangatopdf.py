import os
import re
from PIL import Image
from tkinter import Tk, Label, Button, filedialog, messagebox, IntVar, Entry
from tkinter.simpledialog import askstring
from tkinter import ttk


def extract_chapter_number(folder_name):
    """
    Extracts the numerical part from a chapter folder name.
    Example: 'c131' -> 131
    """
    match = re.search(r"\d+", folder_name)
    return (
        int(match.group()) if match else float("inf")
    )  # Non-matching folders are sorted last


def extract_image_number(file_name):
    """
    Extracts the numerical part from an image file name.
    Example: '001.jpg' -> 1
    """
    match = re.search(r"\d+", os.path.splitext(file_name)[0])
    return (
        int(match.group()) if match else float("inf")
    )  # Non-matching files are sorted last


def convert_all_chapters_to_pdf(main_folder, output_pdf, pages_per_pdf, progress_bar):
    """
    Combines all images from all chapter folders into one or more PDFs,
    ensuring correct order even if image filenames restart from '1' in each chapter.

    Parameters:
        main_folder (str): The path to the main folder containing chapter subfolders.
        output_pdf (str): The base name for the output PDF file.
        pages_per_pdf (int): The maximum number of pages per PDF.
        progress_bar (ttk.Progressbar): The progress bar to update during the process.
    """
    all_images = []
    total_images = 0

    # Get all chapter folders and sort them numerically
    chapter_folders = [
        f
        for f in os.listdir(main_folder)
        if os.path.isdir(os.path.join(main_folder, f))
    ]
    chapter_folders.sort(key=extract_chapter_number)

    # Collect all image paths sorted correctly
    for chapter_folder in chapter_folders:
        chapter_path = os.path.join(main_folder, chapter_folder)

        # Get all image files from the chapter folder
        image_files = [
            f
            for f in os.listdir(chapter_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))
        ]

        # Sort image files by their numeric filename to ensure correct order
        image_files.sort(key=extract_image_number)

        # Append full paths
        image_files_full = [os.path.join(chapter_path, f) for f in image_files]

        # Open images and add to the list
        for img_path in image_files_full:
            try:
                img = Image.open(img_path).convert("RGB")
                all_images.append(img)
                total_images += 1
            except Exception as e:
                print(f"Error opening {img_path}: {e}")

    if total_images > 0:
        # Set up progress bar
        progress_bar["maximum"] = total_images
        progress_bar["value"] = 0

        # Handle splitting into multiple PDFs based on pages_per_pdf
        pdf_part = 1
        for start_idx in range(
            0, total_images, pages_per_pdf if pages_per_pdf > 0 else total_images
        ):
            end_idx = start_idx + (pages_per_pdf if pages_per_pdf > 0 else total_images)
            part_images = all_images[start_idx:end_idx]

            # Determine the output PDF filename
            if pages_per_pdf > 0:
                pdf_filename = f"{output_pdf}_part{pdf_part}.pdf"
            else:
                pdf_filename = f"{output_pdf}.pdf"

            # Save the PDF
            try:
                part_images[0].save(
                    pdf_filename, save_all=True, append_images=part_images[1:]
                )
                print(f"PDF part {pdf_part} created: {pdf_filename}")
                pdf_part += 1
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create {pdf_filename}: {e}")
                return

            # Update progress bar
            progress_bar["value"] += len(part_images)
            progress_bar.update()

        messagebox.showinfo("Success", "PDF(s) created successfully.")
    else:
        messagebox.showerror("Error", "No images found in the provided folders.")


def select_main_folder():
    """Open a file dialog to select the main folder containing chapter subfolders."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        return folder_path
    else:
        messagebox.showerror("Error", "Please select a valid folder.")
        return None


def ask_output_pdf():
    """Prompt the user to specify the output PDF filename."""
    output_pdf = askstring(
        "Output PDF", "Enter the base name for the output PDF (without extension):"
    )
    if output_pdf:
        return output_pdf
    else:
        messagebox.showerror("Error", "Please enter a valid PDF name.")
        return None


def start_conversion(progress_bar, pages_per_pdf_var):
    """Start the conversion process."""
    main_folder = select_main_folder()
    if main_folder:
        output_pdf = ask_output_pdf()
        if output_pdf:
            try:
                pages_per_pdf = int(pages_per_pdf_var.get())
                if pages_per_pdf < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid number for pages per PDF (0 or positive integer).",
                )
                return
            convert_all_chapters_to_pdf(
                main_folder, output_pdf, pages_per_pdf, progress_bar
            )


# Set up the GUI
def create_gui():
    root = Tk()
    root.title("Manga to PDF Converter")
    root.geometry("500x300")
    root.resizable(False, False)

    title_label = Label(
        root, text="Manga to PDF Converter", font=("Helvetica", 18, "bold")
    )
    title_label.pack(pady=10)

    # Frame for pages per PDF
    input_frame = ttk.Frame(root)
    input_frame.pack(pady=10)

    pages_label = Label(
        input_frame, text="Max Pages per PDF (0 = No Split):", font=("Helvetica", 12)
    )
    pages_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    pages_per_pdf_var = IntVar(value=0)
    pages_entry = Entry(
        input_frame, textvariable=pages_per_pdf_var, font=("Helvetica", 12), width=10
    )
    pages_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Progress Bar
    progress_label = Label(root, text="Progress:", font=("Helvetica", 12))
    progress_label.pack(pady=5)

    progress_bar = ttk.Progressbar(
        root, orient="horizontal", length=400, mode="determinate"
    )
    progress_bar.pack(pady=5)

    # Convert Button
    convert_button = Button(
        root,
        text="Select Folder and Convert",
        command=lambda: start_conversion(progress_bar, pages_per_pdf_var),
        font=("Helvetica", 14),
        bg="#4CAF50",
        fg="white",
    )
    convert_button.pack(pady=20)

    # Footer
    footer_label = Label(root, text="© 2024 Manga Converter", font=("Helvetica", 10))
    footer_label.pack(side="bottom", pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
