# 📂 Automated Download Folder Organizer

An intelligent Python utility that keeps your Downloads folder organized by automatically sorting new files into categorized subfolders in real-time.

## ✨ Features

- **Real-Time Monitoring:** Uses the `watchdog` library to monitor your Downloads folder for new files.
- **Instant Organization:** Moves files into predefined subfolders (e.g., DOCUMENTS, IMAGES, CODE) as soon as downloads complete.
- **Smart Categorization:** Sorts files based on their extensions.
- **Duplicate Handling:** Renames duplicates using a sequential naming convention (e.g., `image.png`, `image(1).png`).
- **Seamless Workflow:** Ignores temporary or in-progress downloads, processing only completed files.
- **Cross-Platform:** Works on Windows, macOS, and Linux using standard Python libraries.

## 💡 Problem

Downloads folders quickly become cluttered, making it hard to find files and wasting time.

## 🚀 Solution

This organizer acts as a digital assistant, automatically sorting new files into structured categories for a tidy and efficient Downloads folder.

## 🛠️ Technical Approach

| Component              | Purpose                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------|
| `watchdog` Library     | Real-time event handling; observes file creation in the monitored directory.              |
| `os` & `shutil`        | File and folder management, including moving files and creating folders.                  |
| Custom Naming Logic    | Prevents overwriting by renaming duplicates.                                              |
| Temporary File Filter  | Ignores incomplete or temporary files for seamless operation.                             |

## ⚙️ Installation & Usage

### Prerequisites

- Python 3.x

### Install Dependencies

```bash
pip install watchdog
```

### Clone the Repository

```bash
git clone https://github.com/your-username/automated-download-organizer.git
cd automated-download-organizer
```

### Configure (Optional)

Edit the file extension-to-folder mapping in the script to customize categorization.

### Run the Script

```bash
python organizer_script_name.py
```

To stop, press `Ctrl+C` in the terminal.

## 🤝 Contributing

Feedback, bug reports, and contributions are welcome! Open an issue or submit a pull request.
