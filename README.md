# PDFMerger

## Motivation

In many enterprise environments, employees often rely on **online PDF merging tools** to combine documents. While convenient, this poses a serious **security risk**, especially when dealing with **confidential files** such as internal reports, legal contracts, or sensitive documentation. Uploading these files to third-party servers can lead to **data leakage** or **unauthorized access**.

This tool was created to offer a **secure, offline alternative** for merging PDF files, ensuring that your documents never leave your device.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pnasis/PDFMerger.git
cd PDFMerger
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pypdf
```

Note: On some Linux systems, you may need to install tkinter separately:
```bash
sudo pacman -S tk  # for Arch/Manjaro
sudo apt install python3-tk  # for Debian/Ubuntu
```

---

## Usage

Run the script:
```bash
python PDFMerger.py
```

Use the GUI to:

* Select PDF files to merge.

* **Drag and drop** to reorder them.

* Click **"Merge PDFs"** to generate a merged file.

All processing is done locally on your machine. No file is uploaded anywhere.

---

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Pull requests are welcome! If you have ideas to improve the security, UI, or features (e.g., encryption support or file preview), feel free to contribute.
