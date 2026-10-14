# SDEV-1001 Student Workbook

This workbook is a playground for learning the fundamentals of programming with Python in **SDEV-1001: Programming Fundamentals**.

Use it to follow along with in-class examples, try ideas, and practise independently. Topics include variables and data structures, decisions and loops, functions and modules, file handling, objects and classes, and external libraries. Along the way, practise debugging, validating your code, and using version control.

**Work in this repository is for practice, not for marks.** Complete graded assignments and labs in their designated locations, following your instructor's directions.

Experiment, make mistakes, and keep notes about what you learn!

## Install your tools

We'll use **Python 3**, **Visual Studio Code**, and **Git** on your computer. Docker is not required. Use the Python version specified by your instructor so that everyone can follow the same examples.

### 1. Install Python

- **Windows:** Follow the [Python for Windows installation guide](https://docs.python.org/3/using/windows.html). Install Python using the download from [python.org](https://www.python.org/downloads/), and ensure the course's Python version is installed if you use the Python Install Manager.
- **macOS:** Download and run the macOS installer for the course's Python version from [python.org](https://www.python.org/downloads/). Use this installation for the workbook.
- **Linux:** Use your distribution's package manager to install Python 3, pip, and virtual-environment support. On Ubuntu/Debian, the packages are `python3`, `python3-pip`, and `python3-venv`. Check that the version meets your instructor's directions.

Close and reopen your terminal after installation. In PowerShell on Windows, check:

```powershell
py --version
py -m pip --version
py -m venv --help
```

On macOS/Linux, check:

```sh
python3 --version
python3 -m pip --version
python3 -m venv --help
```

You should see a Python 3 version, a pip version, and help for creating virtual environments. If a command is missing or selects a different Python version, resolve that with your instructor before proceeding. Use `python` instead only if that command selects your course's Python 3 installation.

### 2. Install VS Code and Python support

Install [Visual Studio Code](https://code.visualstudio.com/download). Open its **Extensions** view and install **Python** by Microsoft (`ms-python.python`). Also confirm that **Pylance** (`ms-python.vscode-pylance`) and **Python Debugger** (`ms-python.debugpy`) are installed; we'll use these for code assistance and breakpoints.

Open your workbook folder using **File > Open Folder**. Open the Command Palette (**Ctrl+Shift+P** on Windows/Linux or **Cmd+Shift+P** on macOS), choose **Python: Select Interpreter**, and select your course's Python installation. Installing an editor extension does not install Python itself. See the [VS Code Python setup guide](https://code.visualstudio.com/docs/python/python-tutorial) if you need help.

### 3. Install and configure Git

Follow the [Git installation instructions](https://git-scm.com/install/) for your operating system. Open a new terminal and check:

```sh
git --version
```

Before your first commit, set your author name and email. Replace the example values below with the identity your instructor asks you to use. These commands set defaults for all repositories on this computer:

```sh
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Follow your instructor's directions to clone your own workbook repository. Open that clone in VS Code; a downloaded ZIP does not include the Git history needed for the version-control activities.

### 4. Try the first starter

In VS Code, open **Terminal > New Terminal**. From the workbook root, run:

```sh
cd inclass/01-introduction-to-programming
```

Run `py main.py` on Windows or `python3 main.py` on macOS/Linux. You should see `My first workbook program`. You're ready to open that topic's README and begin.

For the early topics, no third-party packages are needed. When we reach the package activities, follow their README instructions to create a local `.venv` and install dependencies with pip. Select that environment in VS Code for that activity. Python's [virtual-environment guide](https://docs.python.org/3/library/venv.html) explains how environments keep project packages separate.

## Starter kits

- [In-class activities](inclass/README.md): guided practice to explore together.
- [Homework activities](homework/README.md): independent, ungraded practice on matching topics.

Each track has 15 numbered topic folders, including four package introductions and optional extra topics. Read each topic README for directions and success checks, then complete its starter files.

## Tool notes

- [VS Code, EditorConfig, and line endings](docs/editor-settings.md): what the configuration files do, why some settings overlap, and how to fix CRLF warnings.
