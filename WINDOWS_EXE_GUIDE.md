# Windows Executable Creation Guide

This guide provides detailed steps for creating a Windows executable (.exe) file for the Flight Reservation Desktop App. This is especially useful for distributing the application to users who don't have Python installed.

## Prerequisites

- Windows operating system (for creating Windows executables)
- Python 3.x installed
- All project dependencies installed (`pip install -r requirements.txt`)

## Step 1: Install PyInstaller

PyInstaller is a popular tool for converting Python applications into standalone executables.

```bash
pip install pyinstaller
```

## Step 2: Basic Executable Creation

For a simple executable that includes all dependencies:

```bash
pyinstaller --onefile --windowed main.py
```

- `--onefile`: Creates a single executable file instead of a directory with many files
- `--windowed`: Prevents a console window from appearing when the application runs

## Step 3: Advanced Options

### Customizing the Executable Name

```bash
pyinstaller --onefile --windowed --name FlightReservation main.py
```

### Adding an Icon (Optional)

If you want to add a custom icon to your executable:

1. Prepare an .ico file (must be in Windows .ico format)
2. Use the `--icon` flag:

```bash
pyinstaller --onefile --windowed --icon=YOUR_ICON.ico main.py
```

### Cleaning Up Build Files

```bash
pyinstaller --onefile --windowed --clean main.py
```

## Step 4: Locating the Executable

After successful compilation, your executable will be in the `dist` directory.

## Troubleshooting Common Issues

### Missing Modules

If your executable fails with "ModuleNotFoundError", create a `.spec` file first:

```bash
pyi-makespec --onefile --windowed main.py
```

Then edit the `main.spec` file to add hidden imports:

```python
# Add this to the Analysis section
hiddenimports=['PIL._tkinter_finder'],
```

Then build using the spec file:

```bash
pyinstaller main.spec
```

### Missing SQLite Database

If your application requires a database file, include it with the `--add-data` flag:

```bash
pyinstaller --onefile --windowed --add-data "flights.db;." main.py
```

### Antivirus Detection

Some antivirus software may flag PyInstaller executables as potential threats (false positives). If this happens:

1. Add the executable to your antivirus exceptions
2. Use a trusted code signing certificate
3. Try building with `--noupx` to avoid compression that might trigger antivirus alerts:

```bash
pyinstaller --onefile --windowed --noupx main.py
```

### Tkinter Issues

If Tkinter doesn't work correctly in the executable:

```bash
pyinstaller --onefile --windowed --hidden-import tkinter --hidden-import PIL._tkinter_finder main.py
```

## Testing Your Executable

Always test your executable on a clean system (without Python installed) to ensure all dependencies are properly included.
