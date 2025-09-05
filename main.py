"""
main.py - Main application file for the Flight Reservation App

This is the entry point for the Flight Reservation Desktop App.
It sets up the main window and manages navigation between different pages.

The app is structured with the following components:
- database.py: Database connections and operations
- home.py: Main navigation page
- booking.py: Flight booking form
- reservations.py: View all reservations
- edit_reservation.py: Update/Delete functionality
"""
import tkinter as tk
from tkinter import ttk

# Import modules
from database import Database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App:
    def __init__(self, root):
        """
        Initialize the main application
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.db = Database()
        
        # Configure root window
        self.root.title("Flight Reservation System")
        self.root.geometry("900x650")  # Width x Height
        
        # Set theme
        self.setup_style()
        
        # Initialize pages
        self.init_pages()
        
        # Show home page initially
        self.show_home_page()
    
    def setup_style(self):
        """Configure the application style and theme"""
        # Create and configure style
        style = ttk.Style()
        
        # Use a theme - 'clam', 'alt', 'default', 'classic'
        style.theme_use("clam")
        
        # Configure button style
        style.configure(
            "TButton",
            font=("Arial", 12),
            padding=5
        )
        
        # Configure Nav.TButton style for more professional look
        style.configure(
            "Nav.TButton",
            font=("Arial", 10, "bold"),
            padding=5,
            background="#0288d1",
            foreground="white"
        )
        
        # Configure hover effect (if supported)
        try:
            style.map(
                "Nav.TButton",
                background=[("active", "#026cb1")]
            )
        except Exception:
            pass  # Skip if not supported
    
    def init_pages(self):
        """Initialize all application pages"""
        # Create instances of all pages
        self.home_page = HomePage(
            self.root, 
            self.show_booking_page,
            self.show_reservations_page
        )
        
        self.booking_page = BookingPage(
            self.root,
            self.db,
            self.show_home_page
        )
        # Set the navigation button command
        self.booking_page.view_reservations_btn.config(command=self.show_reservations_page)
        
        self.reservations_page = ReservationsPage(
            self.root,
            self.db,
            self.show_home_page,
            self.show_edit_reservation_page
        )
        # Set the navigation button command
        self.reservations_page.book_flight_btn.config(command=self.show_booking_page)
        
        self.edit_reservation_page = EditReservationPage(
            self.root,
            self.db,
            self.show_reservations_page
        )
        # Set the navigation button commands
        self.edit_reservation_page.home_btn.config(command=self.show_home_page)
        self.edit_reservation_page.book_flight_btn.config(command=self.show_booking_page)
    
    def show_home_page(self):
        """Display the home page"""
        self.booking_page.hide()
        self.reservations_page.hide()
        self.edit_reservation_page.hide()
        self.home_page.show()
    
    def show_booking_page(self):
        """Display the booking page"""
        self.home_page.hide()
        self.reservations_page.hide()
        self.edit_reservation_page.hide()
        self.booking_page.show()
    
    def show_reservations_page(self):
        """Display the reservations page"""
        self.home_page.hide()
        self.booking_page.hide()
        self.edit_reservation_page.hide()
        self.reservations_page.show()
    
    def show_edit_reservation_page(self, reservation_id):
        """
        Display the edit reservation page
        
        Args:
            reservation_id (int): ID of the reservation to edit
        """
        self.home_page.hide()
        self.booking_page.hide()
        self.reservations_page.hide()
        self.edit_reservation_page.show(reservation_id)

# Create a splash screen for the application
def show_splash(root):
    # Hide the main window initially
    root.withdraw()
    
    # Create splash screen window
    splash = tk.Toplevel(root)
    splash.title("FlySky Reservations")
    
    # No window border
    splash.overrideredirect(True)
    
    # Get screen dimensions
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    
    # Set splash screen size and position
    width = 400
    height = 250
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    splash.geometry(f"{width}x{height}+{x}+{y}")
    
    # Set background color
    splash.configure(bg="#0288d1")
    
    # Add plane icon
    icon_label = tk.Label(
        splash,
        text="✈",
        font=("Arial", 48, "bold"),
        fg="white",
        bg="#0288d1"
    )
    icon_label.pack(pady=(30, 10))
    
    # Add app name
    app_label = tk.Label(
        splash,
        text="FlySky Reservations",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#0288d1"
    )
    app_label.pack()
    
    # Add loading text
    loading_label = tk.Label(
        splash,
        text="Loading...",
        font=("Arial", 12),
        fg="white",
        bg="#0288d1"
    )
    loading_label.pack(pady=20)
    
    # Function to destroy splash and show main window
    def finish_splash():
        splash.destroy()
        root.deiconify()
    
    # Set delay to close splash screen (1.5 seconds)
    splash.after(1500, finish_splash)
    
    return splash

# Main entry point
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Show splash screen
    splash = show_splash(root)
    
    # Create and run the application
    app = App(root)
    
    # Start the Tkinter event loop
    root.mainloop()
    
    # Close database connection when app closes
    app.db.close()