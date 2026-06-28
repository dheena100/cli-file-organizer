# 📂 CLI File Organizer with Decorators

A professional Python command-line application that organizes files by **extension**, **size**, or **last modified date**. It supports **dry-run mode**, **undo functionality**, **execution logging**, and **type-safe code**.

---

## 🚀 Features

- 📁 Organize files by extension
- 📏 Organize files by size
- 📅 Organize files by last modified year
- 👀 Dry-run mode (preview changes without moving files)
- ↩️ Undo the last sorting operation
- 📝 Execution logging with a custom decorator
- 📊 Sorting summary statistics
- 🛡️ Error handling
- 🧪 Unit tests with pytest
- ✅ Type hints compatible with mypy

---

## 📂 Project Structure

```text
cli-file-organizer/
│
├── organizer/
│   ├── __init__.py
│   ├── cli.py
│   ├── sorter.py
│   ├── logger.py
│   ├── undo.py
│   ├── models.py
│   └── utils.py
│
├── logs/
│
├── sample_files/
│
├── tests/
│
├── requirements.txt
├── pytest.ini
├── mypy.ini
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

- Python 3.12+
- Click
- pathlib
- shutil
- JSON
- pytest
- mypy
- Git
- GitHub Actions

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cli-file-organizer.git
```

Move into the project:

```bash
cd cli-file-organizer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Sort by Extension

```bash
python -m organizer.cli sort --by extension
```

### Sort by Size

```bash
python -m organizer.cli sort --by size
```

### Sort by Date

```bash
python -m organizer.cli sort --by date
```

### Preview Without Moving Files

```bash
python -m organizer.cli sort --by extension --dry-run
```

### Undo Last Operation

```bash
python -m organizer.cli undo
```

---

## 📸 Example Output

```text
Moved report.pdf -> Documents/
Moved photo.jpg -> Images/
Moved song.mp3 -> Music/

========== Summary ==========
Moved Files : 3
Images      : 1
Documents   : 1
Music       : 1
Videos      : 0
Others      : 0
=============================
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🔍 Type Checking

```bash
mypy organizer --strict
```

---

## 🚀 Continuous Integration

GitHub Actions automatically:

- Runs unit tests
- Performs static type checking with mypy

---

## 📌 Future Improvements

- Configuration file support
- Custom sorting rules
- Recursive directory traversal
- Progress bar
- File duplicate detection
- ZIP archive organization

---

## 👨‍💻 Author

**Dheena G**

Python Developer | Backend Developer

LinkedIn: https://www.linkedin.com/in/your-profile

GitHub: https://github.com/your-username
