✨ **Overview**

The Manga to PDF Converter is a simple yet powerful tool designed to turn your manga chapters (organized as images) into PDF files. You can merge all chapters into one big PDF or split them into multiple PDFs based on your preference for pages or chapters.

🌟 **Key Features:**

- 📑 **Merge Chapters:** Combine all images into a single PDF.
- ✂️ **Split Options:** 
  - **Split Pages:** Option to split the output into multiple PDFs after a set number of pages.
  - **Split Chapters:** Option to create separate PDFs for each chapter.
- 🗂 **Automatic Sorting:** Images and chapters are ordered correctly, even if the file names restart within each chapter.
- ⏳ **Progress Tracking:** Watch your progress with a handy progress bar!

🛠 **How to Use**

1. 🖱 **Launch the Application:**
   - Double-click the executable (MangaToPDFConverter.exe) to start the application.

2. 📏 **Set Max Pages per PDF:**
   - Enter the number of pages you want per PDF.
   - If you want a single PDF, enter 0 (all pages combined).
   - Choose whether to split by pages or by chapters using the provided toggle option.

3. 📂 **Select the Manga Folder:**
   - Click "Select Folder and Convert" to choose the folder containing all your chapter subfolders. The subfolders should be named in a consistent format (e.g., c131, c132, etc.).

4. 📝 **Name Your Output PDFs:**
   - After selecting the folder, you’ll be asked to name your output PDF(s).
   - If you set a page limit, multiple PDFs will be created with numbered parts (e.g., MyManga_part1.pdf, MyManga_part2.pdf, etc.).
   - If no page limit is set, only one PDF will be generated (e.g., MyManga.pdf).

5. 📊 **Progress Bar:**
   - The progress bar shows the conversion status.
   - Once done, you’ll see a confirmation message!

🗂 **Folder and Image Naming Convention**

For the best experience, make sure your manga folder structure and image naming are organized as follows:
main/ ├── c131/ │ ├── 001.jpg │ ├── 002.jpg │ └── ... ├── c132/ │ ├── 001.jpg │ └── ... └── c133/ ├── 001.jpg ├── 002.jpg └── ...

### ✅ Folder Structure:
- Each **chapter** should be inside its own subfolder (e.g., `c131`, `c132`, `c133`, etc.).

### ✅ Image Naming:
- Inside each chapter, **image files** should be named numerically, starting with `001.jpg`, `002.jpg`, etc.
- Supported image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.tiff`.

---

## 💻 System Requirements

- **OS**: Windows 10 or later.
- **Python**: Not required, everything is bundled in the executable.
- **RAM**: Sufficient memory is needed for large image collections.

---

## 🛠 Troubleshooting

1. **❌ No Images Found**:
   - Ensure that your chapter folders contain images in supported formats.
   - Double-check that your folder names follow the `cXXX` format, and image files are named sequentially.

2. **❌ PDF Creation Failed**:
   - Ensure you have write permissions in the output folder.
   - If splitting PDFs, verify you have enough disk space for multiple files.

---

## 📜 License

This tool is provided **as-is**, with no warranty. Feel free to share it with others!

---

## 📧 Contact

If you run into any issues or have feature requests, feel free to reach out! 🎉
