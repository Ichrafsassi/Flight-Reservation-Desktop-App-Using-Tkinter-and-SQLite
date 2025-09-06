# Flight Reservation Desktop App

A modern desktop application for flight reservations built with Python, Tkinter, and SQLite.

## Features

- Modern and professional UI design with blue header and card layout
- Create flight reservations with passenger and flight details
- View all reservations in a tabular format
- Search for reservations by name, flight number, departure, or destination
- Edit existing reservations
- Delete reservations
- SQLite database for storing reservation information
- Splash screen with application logo
- Executable file for easy distribution

## Project Structure
```
├── main.py               # Entry point of the application
├── database.py           # SQLite database operations
├── home.py               # Home page with navigation cards
├── booking.py            # Form for creating new reservations
├── reservations.py       # View and manage existing reservations
├── edit_reservation.py   # Edit or delete a specific reservation
├── flights.db            # SQLite database file (created on first run)
├── requirements.txt      # Required Python libraries
├── dist/                 # Directory containing executable file
│   └── main.exe          # Windows executable
├── LICENSE               # License information
├── README.md             # Project documentation
```

## Database Schema

The application uses a simple database with a single table:

```sql
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    departure TEXT NOT NULL,
    destination TEXT NOT NULL,
    date TEXT NOT NULL,
    seat_number TEXT NOT NULL
);
```

## Requirements
- Python 3.x
- Tkinter (included with most Python installations)
- SQLite3 (included with Python)

## Installation and Usage

### Method 1: Running from Source Code

1. Clone the repository:
   ```bash
   git clone https://github.com/Ichrafsassi/Flight-Reservation-Desktop-App-Using-Tkinter-and-SQLite.git
   cd Flight-Reservation-Desktop-App-Using-Tkinter-and-SQLite
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py  # Windows
   python3 main.py  # Linux/macOS
   ```

### Method 2: Using the Executable

#### Windows
1. Download the latest release from the GitHub repository
2. Extract the ZIP file
3. Run `main.exe` from the extracted folder

#### Linux
1. Download the latest release from the GitHub repository
2. Extract the archive file
3. Make the file executable: `chmod +x main`
4. Run the executable: `./main`

## Creating the Windows Executable

### Method 1: Using the Batch Script (Recommended for Windows Users)

1. Simply double-click the `create_windows_exe.bat` file included in this repository
2. The script will automatically install required dependencies and create the executable
3. Once completed, the executable will be available in the `dist` folder

### Method 2: Manual Creation

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to the project directory and run:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```

3. The executable will be created in the `dist` directory

### Documentation and Troubleshooting

- For a comprehensive guide on creating Windows executables, see [WINDOWS_EXE_GUIDE.md](WINDOWS_EXE_GUIDE.md)
- If you encounter issues with the Windows executable, see [WINDOWS_EXE_TROUBLESHOOTING.md](WINDOWS_EXE_TROUBLESHOOTING.md)

## Application Workflow

1. **Home Page**: Navigate between booking a new flight or viewing existing reservations
2. **Booking Page**: Enter passenger and flight details to create a new reservation
3. **Reservations Page**: View all reservations with search functionality
4. **Edit Page**: Modify or delete an existing reservation

## Future Improvements

- User authentication system
- Flight search API integration
- Email confirmation for bookings
- Seat map selection
- Boarding pass generation
