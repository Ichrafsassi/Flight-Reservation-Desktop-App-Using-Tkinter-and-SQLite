"""
booking.py - Flight booking form for the Flight Reservation App

This module handles the flight booking functionality:
- Provides a form to enter flight and passenger information
- Creates reservations in the database
"""
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class BookingPage:
    def __init__(self, root, db, go_back):
        """
        Initialize the booking page
        
        Args:
            root: The main Tkinter window
            db: Database instance
            go_back: Function to return to home page
        """
        self.root = root
        self.db = db
        self.go_back = go_back
        self.frame = tk.Frame(root)
        
        # Create and place UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all widgets for the booking page"""
        
        # Create a header frame with blue background
        header_frame = tk.Frame(self.frame, bg="#0288d1", height=60)
        header_frame.pack(fill=tk.X)
        
        # Add plane icon and app name to header with a more professional look
        icon_text = "✈"  # Clean plane icon
        icon_label = tk.Label(
            header_frame, 
            text=icon_text, 
            font=("Arial", 24, "bold"), 
            bg="#0288d1", 
            fg="white"
        )
        icon_label.pack(side=tk.LEFT, padx=(20, 5), pady=10)
        
        app_name = tk.Label(
            header_frame, 
            text="FlySky Reservations", 
            font=("Arial", 16, "bold"), 
            bg="#0288d1", 
            fg="white"
        )
        app_name.pack(side=tk.LEFT, pady=10)
        
        # Add navigation buttons to header
        nav_style = ttk.Style()
        nav_style.configure("Nav.TButton", background="#0288d1", foreground="white")
        
        home_btn = ttk.Button(
            header_frame, 
            text="Home",
            style="Nav.TButton",
            command=self.go_back
        )
        home_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        book_nav_btn = ttk.Button(
            header_frame, 
            text="Book Flight",
            style="Nav.TButton",
            state=tk.DISABLED  # Disable since we're already on this page
        )
        book_nav_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Store view_reservations as an attribute so it can be set from main.py
        self.view_reservations_btn = ttk.Button(
            header_frame, 
            text="View Reservations",
            style="Nav.TButton"
            # We'll set command in main.py
        )
        self.view_reservations_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Main content area with white background
        content_frame = tk.Frame(self.frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Page title
        title_frame = tk.Frame(content_frame, bg="white")
        title_frame.pack(fill=tk.X, padx=40, pady=(40, 20))
        
        title_label = tk.Label(
            title_frame,
            text="Book a Flight",
            font=("Arial", 24, "bold"),
            fg="#0288d1",
            bg="white"
        )
        title_label.pack(anchor=tk.W)
        
        # Create a card-like form with a shadow effect
        form_card_shadow = tk.Frame(
            content_frame,
            bg="#dddddd"
        )
        form_card_shadow.pack(fill=tk.BOTH, expand=True, padx=40, pady=(0, 40), ipady=20)
        
        # Actual form card with slight offset to create shadow
        form_card = tk.Frame(
            form_card_shadow,
            bg="white",
            bd=1,
            relief=tk.SOLID
        )
        form_card.pack(fill=tk.BOTH, expand=True, padx=2, pady=(0, 4))
        
        # Form layout with grid
        form_inner = tk.Frame(form_card, bg="white", padx=30, pady=30)
        form_inner.pack(fill=tk.BOTH, expand=True)
        
        # Full Name
        name_label = tk.Label(
            form_inner,
            text="Full Name",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        name_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.name_entry = tk.Entry(
            form_inner,
            font=("Arial", 12),
            width=40,
            bd=1,
            relief=tk.SOLID
        )
        self.name_entry.grid(row=1, column=0, sticky=tk.W, pady=(0, 15))
        self.name_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Flight Number
        flight_label = tk.Label(
            form_inner,
            text="Flight Number",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        flight_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        self.flight_entry = tk.Entry(
            form_inner,
            font=("Arial", 12),
            width=40,
            bd=1,
            relief=tk.SOLID
        )
        self.flight_entry.grid(row=3, column=0, sticky=tk.W, pady=(0, 15))
        self.flight_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Two-column layout for departure and destination
        location_frame = tk.Frame(form_inner, bg="white")
        location_frame.grid(row=4, column=0, sticky=tk.EW, pady=(0, 15))
        location_frame.columnconfigure(0, weight=1)
        location_frame.columnconfigure(1, weight=1)
        
        # Departure
        departure_label = tk.Label(
            location_frame,
            text="Departure",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        departure_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.departure_entry = tk.Entry(
            location_frame,
            font=("Arial", 12),
            width=20,
            bd=1,
            relief=tk.SOLID
        )
        self.departure_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.departure_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Destination
        destination_label = tk.Label(
            location_frame,
            text="Destination",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        destination_label.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))
        
        self.destination_entry = tk.Entry(
            location_frame,
            font=("Arial", 12),
            width=20,
            bd=1,
            relief=tk.SOLID
        )
        self.destination_entry.grid(row=1, column=1, sticky=tk.W)
        self.destination_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Date and seat number in a two-column layout
        details_frame = tk.Frame(form_inner, bg="white")
        details_frame.grid(row=5, column=0, sticky=tk.EW, pady=(0, 25))
        details_frame.columnconfigure(0, weight=1)
        details_frame.columnconfigure(1, weight=1)
        
        # Date
        date_label = tk.Label(
            details_frame,
            text="Date (YYYY-MM-DD)",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        date_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # Create a simple entry for date
        self.date_entry = tk.Entry(
            details_frame,
            font=("Arial", 12),
            width=20,
            bd=1,
            relief=tk.SOLID
        )
        self.date_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.date_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Seat Number
        seat_label = tk.Label(
            details_frame,
            text="Seat Number",
            font=("Arial", 12),
            bg="white",
            anchor=tk.W
        )
        seat_label.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))
        
        self.seat_entry = tk.Entry(
            details_frame,
            font=("Arial", 12),
            width=20,
            bd=1,
            relief=tk.SOLID
        )
        self.seat_entry.grid(row=1, column=1, sticky=tk.W)
        self.seat_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        # Button row with cancel and book options
        button_frame = tk.Frame(form_inner, bg="white")
        button_frame.grid(row=6, column=0, sticky=tk.E)
        
        # Style for buttons
        btn_style = ttk.Style()
        btn_style.configure("Cancel.TButton", font=("Arial", 12))
        btn_style.configure("Book.TButton", font=("Arial", 12, "bold"), background="#0288d1")
        
        # Create a frame for the booking button to add a blue background
        book_btn_frame = tk.Frame(button_frame, bg="#0288d1", padx=2, pady=2)
        book_btn_frame.pack(side=tk.RIGHT)
        
        # Book Flight button (blue)
        book_btn = ttk.Button(
            book_btn_frame,
            text="Book Flight",
            style="Book.TButton",
            command=self.book_flight
        )
        book_btn.pack()
        
        # Cancel button
        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            style="Cancel.TButton",
            command=self.go_back
        )
        cancel_btn.pack(side=tk.RIGHT, padx=(0, 10))
    
    def book_flight(self):
        """Process the flight booking"""
        # Get values from form
        name = self.name_entry.get().strip()
        flight_number = self.flight_entry.get().strip()
        departure = self.departure_entry.get().strip()
        destination = self.destination_entry.get().strip()
        seat_number = self.seat_entry.get().strip()
        
        # Get date
        # Get date from entry
        date = self.date_entry.get().strip()
        
        # Validate all fields
        if not (name and flight_number and departure and destination and date and seat_number):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Add reservation to database
        success = self.db.add_reservation(
            name, flight_number, departure, destination, date, seat_number
        )
        
        if success:
            messagebox.showinfo("Success", "Flight booked successfully!")
            
            # Clear form fields
            self.name_entry.delete(0, tk.END)
            self.flight_entry.delete(0, tk.END)
            self.departure_entry.delete(0, tk.END)
            self.destination_entry.delete(0, tk.END)
            # Clear and reset date entry
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
            self.seat_entry.delete(0, tk.END)
            
            # Go back to home page
            self.go_back()
        else:
            messagebox.showerror("Error", "Failed to book flight. Please try again.")
    
    def show(self):
        """Display the booking page"""
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        """Hide the booking page"""
        self.frame.pack_forget()
