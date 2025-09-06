# Windows EXE Troubleshooting Guide

This document provides solutions for common issues encountered when creating or running the Windows executable (.exe) file for the Flight Reservation App.

## Common Issues and Solutions

### 1. "Failed to execute script 'main'" Error

**Symptoms**: The application starts to launch but immediately closes with an error message.

**Solutions**:
- Run the executable from the command prompt to see the error message:
  ```
  cd path\to\executable
  main.exe
  ```
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Rebuild with hidden imports:
  ```
  pyinstaller --onefile --windowed --hidden-import tkinter --hidden-import PIL._tkinter_finder main.py
  ```

### 2. Missing Database File

**Symptoms**: The application starts but can't find the database file.

**Solutions**:
- Include the database in the executable:
  ```
  pyinstaller --onefile --windowed --add-data "flights.db;." main.py
  ```
- If you're using a relative path to access the database, modify your code to use:
  ```python
  import sys
  import os
  
  # Determine if application is a script file or frozen exe
  if getattr(sys, 'frozen', False):
      application_path = os.path.dirname(sys.executable)
  else:
      application_path = os.path.dirname(os.path.abspath(__file__))
      
  database_path = os.path.join(application_path, 'flights.db')
  ```

### 3. Antivirus False Positives

**Symptoms**: Windows Defender or antivirus software flags the .exe as malicious.

**Solutions**:
- Build without UPX compression: `pyinstaller --onefile --windowed --noupx main.py`
- Add an exclusion in your antivirus software
- Use a trusted code signing certificate to sign your executable

### 4. Missing DLL Errors

**Symptoms**: Error about missing DLLs when launching the executable.

**Solutions**:
- Install the Visual C++ Redistributable for Visual Studio
- Try building with the `--onedir` option instead of `--onefile`:
  ```
  pyinstaller --onedir --windowed main.py
  ```

### 5. Black Window or Immediate Crash

**Symptoms**: Application opens briefly and then disappears.

**Solutions**:
- Check for hidden exceptions by running from command line
- Verify that all imported modules are included by adding:
  ```
  pyinstaller --onefile --windowed --debug all main.py
  ```

### 6. Tkinter Issues

**Symptoms**: Issues with the GUI not displaying properly or Tkinter errors.

**Solutions**:
- Ensure Tcl/Tk is properly included:
  ```
  pyinstaller --onefile --windowed --hidden-import tkinter --collect-all tkinter main.py
  ```

### 7. Images or Resources Not Found

**Symptoms**: The application runs but images or resources are missing.

**Solutions**:
- Include all resource files explicitly:
  ```
  pyinstaller --onefile --windowed --add-data "images/*;images/" main.py
  ```
- Use this code pattern to find resources:
  ```python
  import sys
  import os
  
  def resource_path(relative_path):
      if hasattr(sys, '_MEIPASS'):
          return os.path.join(sys._MEIPASS, relative_path)
      return os.path.join(os.path.abspath("."), relative_path)
  
  # Then use resource_path() for all file paths
  image = PhotoImage(file=resource_path("images/icon.png"))
  ```

## Advanced Solutions

### Creating a .spec File

For more complex builds, create and edit a .spec file:

1. Generate a spec file:
   ```
   pyi-makespec --onefile --windowed main.py
   ```

2. Edit the `main.spec` file to add additional options

3. Build using the spec file:
   ```
   pyinstaller main.spec
   ```

### Clean Build

If you've made changes to your code or updated PyInstaller:

```
pyinstaller --clean --onefile --windowed main.py
```

## Still Having Issues?

1. Verify your Python code works correctly before packaging
2. Check PyInstaller version compatibility with your Python version
3. Try a simpler test app to verify PyInstaller is working correctly
4. Check PyInstaller documentation for specific issues
