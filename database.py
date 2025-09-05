"""
database.py - SQLite database connection and setup

This module handles all database operations for the Flight Reservation System:
- Creating and connecting to the database
- Creating necessary tables
- CRUD operations for flights and reservations
"""
import sqlite3
import os

class Database:
    def __init__(self, db_name='flights.db'):
        """
        Initialize database connection
        
        Args:
            db_name (str): Name of the database file
        """
        # Store database name
        self.db_name = db_name
        
        # Check if database exists, if not create tables
        db_exists = os.path.exists(db_name)
        
        # Create connection to database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Create tables if they don't exist
        if not db_exists:
            self.create_tables()
    
    def create_tables(self):
        """Create necessary tables in the database if they don't exist"""
        
        # Create reservations table according to requirements
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
        ''')
        
        # Commit changes
        self.conn.commit()
    
    def add_reservation(self, name, flight_number, departure, destination, date, seat_number):
        """
        Add a new reservation
        
        Args:
            name (str): Passenger name
            flight_number (str): Flight identifier
            departure (str): Departure location
            destination (str): Destination location
            date (str): Flight date
            seat_number (str): Seat identifier
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, flight_number, departure, destination, date, seat_number))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding reservation: {e}")
            return False
    
    def get_all_reservations(self):
        """
        Get all reservations
        
        Returns:
            list: List of tuples containing reservation information
        """
        self.cursor.execute('''
        SELECT id, name, flight_number, departure, destination, date, seat_number 
        FROM reservations
        ''')
        
        return self.cursor.fetchall()
    
    def get_reservation_by_id(self, reservation_id):
        """
        Get a reservation by its ID
        
        Args:
            reservation_id (int): ID of the reservation
            
        Returns:
            tuple: Reservation information
        """
        self.cursor.execute('''
        SELECT id, name, flight_number, departure, destination, date, seat_number
        FROM reservations
        WHERE id = ?
        ''', (reservation_id,))
        
        return self.cursor.fetchone()
    
    def update_reservation(self, reservation_id, name, flight_number, departure, destination, date, seat_number):
        """
        Update reservation information
        
        Args:
            reservation_id (int): ID of the reservation to update
            name (str): Passenger name
            flight_number (str): Flight identifier
            departure (str): Departure location
            destination (str): Destination location
            date (str): Flight date
            seat_number (str): Seat identifier
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
            ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating reservation: {e}")
            return False
    
    def delete_reservation(self, reservation_id):
        """
        Delete a reservation
        
        Args:
            reservation_id (int): ID of the reservation to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting reservation: {e}")
            return False
    
    def search_reservations(self, search_term):
        """
        Search for reservations with a given search term
        
        Args:
            search_term (str): Term to search for in name, flight_number, departure, destination
            
        Returns:
            list: List of matching reservations
        """
        search_pattern = f"%{search_term}%"
        
        self.cursor.execute('''
        SELECT id, name, flight_number, departure, destination, date, seat_number 
        FROM reservations
        WHERE name LIKE ? OR flight_number LIKE ? OR departure LIKE ? OR destination LIKE ?
        ''', (search_pattern, search_pattern, search_pattern, search_pattern))
        
        return self.cursor.fetchall()
    
    def close(self):
        """Close the database connection"""
        self.conn.close()
