"""
initialize_data.py - Populate the database with sample data

This script adds sample flights to the database for testing purposes.
Run this after setting up the database but before using the app.
"""
from database import Database

def initialize_sample_data():
    """Initialize the database with sample data"""
    # Create database connection
    db = Database()
    
    # Sample flights data
    flights = [
        ("FL100", "New York", "London", "2025-10-15", 250),
        ("FL101", "Paris", "Tokyo", "2025-10-16", 300),
        ("FL102", "Dubai", "Sydney", "2025-10-17", 280),
        ("FL103", "Chicago", "Berlin", "2025-10-18", 220),
        ("FL104", "Toronto", "Mumbai", "2025-10-19", 270)
    ]
    
    # Add flights to database
    for flight in flights:
        db.add_flight(*flight)
    
    # Close connection
    db.close()
    
    print("Sample data has been added to the database!")

if __name__ == "__main__":
    initialize_sample_data()
