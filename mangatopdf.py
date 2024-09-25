import os
import re
from PIL import Image
from tkinter import (
    Tk,
    Label,
    Button,
    filedialog,
    messagebox,
    StringVar,
    IntVar,
    Entry,
    Radiobutton,
)
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


def convert_all_chapters_to_pdf(
    main_folder, output_pdf, split_by, split_value, progress_bar
):
    """
    Combines all images from chapter folders into one or more PDFs, ensuring correct order.
    Optionally splits the output into multiple PDFs either by number of pages or number of chapters.

    Parameters:
        main_folder (str): The path to the main folder containing chapter subfolders.
        output_pdf (str): The base name for the output PDF file.
        split_by (str): Either 'pages' or 'chapters' depending on user choice.
        split_value (int): Max pages or chapters per PDF depending on the chosen split type.
        progress_bar (ttk.Progressbar): The progress bar to update during the process.
    """
    all_images = []
    total_images = 0
    total_chapters = 0
    pdf_part = 1  # Track PDF parts if splitting is needed

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

        total_chapters += 1

        if split_by == "chapters" and total_chapters % split_value == 0:
            save_pdf(all_images, f"{output_pdf}_part{pdf_part}.pdf", progress_bar)
            all_images = []  # Reset for the next set of chapters
            pdf_part += 1

    # Handle any remaining images if splitting by chapters or pages
    if all_images:
        pdf_filename = (
            f"{output_pdf}_part{pdf_part}.pdf" if pdf_part > 1 else f"{output_pdf}.pdf"
        )
        save_pdf(all_images, pdf_filename, progress_bar)

    # If splitting by pages
    if split_by == "pages" and total_images > 0:
        for start_idx in range(0, total_images, split_value):
            end_idx = min(start_idx + split_value, total_images)
            part_images = all_images[start_idx:end_idx]
            pdf_filename = (
                f"{output_pdf}_part{pdf_part}.pdf"
                if split_value > 0
                else f"{output_pdf}.pdf"
            )
            save_pdf(part_images, pdf_filename, progress_bar)
            pdf_part += 1

    if total_images == 0:
        messagebox.showerror("Error", "No images found in the provided folders.")
    else:
        messagebox.showinfo("Success", "PDF(s) created successfully.")


def save_pdf(images, pdf_filename, progress_bar):
    """Helper function to save the images as PDF and update the progress bar."""
    try:
        images[0].save(pdf_filename, save_all=True, append_images=images[1:])
        print(f"PDF created: {pdf_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create {pdf_filename}: {e}")
        return
    progress_bar["value"] += len(images)
    progress_bar.update()


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


def start_conversion(progress_bar, split_type_var, split_value_var):
    """Start the conversion process based on user input."""
    main_folder = select_main_folder()
    if main_folder:
        output_pdf = ask_output_pdf()
        if output_pdf:
            try:
                split_value = int(split_value_var.get())
                if split_value < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid number for split value (positive integer).",
                )
                return
            convert_all_chapters_to_pdf(
                main_folder, output_pdf, split_type_var.get(), split_value, progress_bar
            )


# Set up the GUI
def create_gui():
    root = Tk()
    root.title("Manga to PDF Converter")
    root.geometry("500x350")
    root.resizable(False, False)

    title_label = Label(
        root, text="Manga to PDF Converter", font=("Helvetica", 18, "bold")
    )
    title_label.pack(pady=10)

    # Frame for split options
    split_frame = ttk.Frame(root)
    split_frame.pack(pady=10)

    split_type_var = StringVar(
        value="pages"
    )  # Use StringVar instead of IntVar for string values
    Radiobutton(
        split_frame, text="Split by Pages", variable=split_type_var, value="pages"
    ).grid(row=0, column=0, padx=10)
    Radiobutton(
        split_frame, text="Split by Chapters", variable=split_type_var, value="chapters"
    ).grid(row=0, column=1, padx=10)

    split_label = Label(split_frame, text="Enter max pages/chapters per PDF:")
    split_label.grid(row=1, column=0, padx=10)

    split_value_var = IntVar(value=0)
    split_entry = Entry(
        split_frame, textvariable=split_value_var, font=("Helvetica", 12), width=10
    )
    split_entry.grid(row=1, column=1, padx=10)

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
        command=lambda: start_conversion(progress_bar, split_type_var, split_value_var),
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
