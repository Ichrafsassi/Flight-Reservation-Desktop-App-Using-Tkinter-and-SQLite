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

## Project Structure
```
├── main.py               # Entry point of the application
├── database.py           # SQLite database operations
├── home.py               # Home page with navigation cards
├── booking.py            # Form for creating new reservations
├── reservations.py       # View and manage existing reservations
├── edit_reservation.py   # Edit or delete a specific reservation
├── flights.db            # SQLite database file (created on first run)
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

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-reservation-app.git
   cd flight-reservation-app
   ```

2. Run the application:
   ```bash
   python main.py
   ```

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
