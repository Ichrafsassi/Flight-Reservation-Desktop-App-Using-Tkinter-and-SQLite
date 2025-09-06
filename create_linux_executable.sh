#!/bin/bash

echo "Flight Reservation App - Executable Creator"
echo "========================================"
echo ""
echo "This script will create a standalone executable for the Flight Reservation App."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python first."
    exit 1
fi

echo "Checking for required packages..."
if ! python3 -m pip show pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    python3 -m pip install pyinstaller
fi

echo "Checking for required dependencies..."
python3 -m pip install -r requirements.txt

echo ""
echo "Creating executable file..."
echo ""

python3 -m PyInstaller --onefile --windowed main.py

echo ""
if [ $? -eq 0 ]; then
    echo "Success! The executable has been created in the dist folder."
    echo "You can find it at: $(pwd)/dist/main"
else
    echo "There was an error creating the executable."
    echo "Please check the output above for more information."
fi

echo ""
echo "Press Enter to exit..."
read
