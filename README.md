# Manga to PDF Converter

## Overview

The **Manga to PDF Converter** is a simple tool designed to convert chapters of manga (each containing images) into PDF files. The program supports combining all chapters into one large PDF or splitting the output into multiple PDFs based on the number of pages specified by the user.

### Key Features:
- Combines all chapter images into a single PDF.
- Supports splitting the output into multiple PDFs after a specified number of pages.
- Automatically sorts images and chapters in the correct order, even if the filenames reset within each chapter.
- Visual progress bar to track the conversion process.

---

## How to Use

1. **Launch the Application**:
   - Simply double-click the executable (`MangaToPDFConverter.exe`) to open the application.

2. **Max Pages per PDF**:
   - Enter the number of pages you want per PDF file. 
   - Enter `0` if you want to create a single PDF with all pages combined.

3. **Select the Manga Folder**:
   - Click the "Select Folder and Convert" button.
   - Choose the folder containing all your chapter subfolders. The chapter folders should be named in a consistent format (e.g., `c131`, `c132`, etc.).
   
4. **Enter Output PDF Name**:
   - After selecting the folder, you will be prompted to enter a base name for the output PDF(s).
   - If you specify a page limit (i.e., a number greater than 0), the program will split the output into multiple parts (e.g., `MyManga_part1.pdf`, `MyManga_part2.pdf`, etc.).
   - If no page limit is specified (i.e., 0 pages), a single PDF will be created (e.g., `MyManga.pdf`).

5. **Progress Bar**:
   - A progress bar will show you the progress of the conversion.
   - Once the process is complete, you’ll get a confirmation message.

---

## Folder and Image Naming Convention

### Folder Structure:
Ensure that your manga chapters are stored in a structured format like this:

  main/
  ├── c131/
  │    ├── 001.jpg
  │    ├── 002.jpg
  │    └── ...
  ├── c132/
  │    ├── 001.jpg
  │    └── ...
  └── c133/
       ├── 001.jpg
       ├── 002.jpg
       └── ...

### Image Naming:
- Each image file in a chapter folder should be named numerically, starting from 001, 002, etc.
- Supported image formats include `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.tiff`.

---

## System Requirements

- **Operating System**: Windows 10 or later.
- **Python**: Not required (all dependencies are bundled in the executable).
- **RAM**: The application may require significant memory for large image collections.

---

## Troubleshooting

1. **No Images Found**:
   - Ensure that your chapter folders contain images in supported formats.
   - Double-check that your folder names follow the `cXXX` format, and image files are named numerically.

2. **Output PDF Creation Failed**:
   - Ensure you have write permissions in the folder where you are saving the PDFs.
   - If splitting the PDF, make sure there’s enough disk space for multiple output files.

---

## License

This tool is provided as-is, without any warranty. Feel free to share it with friends!

---

## Contact

If you encounter any issues or have feature requests, feel free to reach out!
