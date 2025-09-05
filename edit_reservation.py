"""
edit_reservation.py - Edit or delete a reservation

This module allows users to:
- Edit the details of an existing reservation
- Delete a reservation
- Return to the reservations page
"""
import tkinter as tk
from tkinter import ttk, messagebox

class EditReservationPage:
    def __init__(self, root, db, go_to_reservations):
        """
        Initialize the edit reservation page

        Args:
            root: The main Tkinter window
            db: Database instance
            go_to_reservations: Function to return to reservations page
        """
        self.root = root
        self.db = db
        self.go_to_reservations = go_to_reservations
        self.frame = tk.Frame(root)
        
        # Store the reservation ID being edited
        self.reservation_id = None
        
        # Create and place UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all widgets for the edit reservation page"""
        
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
            style="Nav.TButton"
            # We'll set command in main.py
        )
        home_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        self.home_btn = home_btn
        
        # Store book_flight as an attribute so it can be set from main.py
        self.book_flight_btn = ttk.Button(
            header_frame, 
            text="Book Flight",
            style="Nav.TButton"
            # We'll set command in main.py
        )
        self.book_flight_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        view_nav_btn = ttk.Button(
            header_frame, 
            text="View Reservations",
            style="Nav.TButton",
            command=self.go_to_reservations
        )
        view_nav_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Main content area with white background
        content_frame = tk.Frame(self.frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Page title
        title_frame = tk.Frame(content_frame, bg="white")
        title_frame.pack(fill=tk.X, padx=40, pady=(40, 20))
        
        title_label = tk.Label(
            title_frame,
            text="Edit Reservation",
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
        
        # Button row with cancel, delete and save options
        button_frame = tk.Frame(form_inner, bg="white")
        button_frame.grid(row=6, column=0, sticky=tk.E)
        
        # Style for buttons
        btn_style = ttk.Style()
        btn_style.configure("Cancel.TButton", font=("Arial", 12))
        btn_style.configure("Delete.TButton", font=("Arial", 12, "bold"), background="#ff5252")
        btn_style.configure("Save.TButton", font=("Arial", 12, "bold"), background="#0288d1")
        
        # Create a frame for the save button to add a blue background
        save_btn_frame = tk.Frame(button_frame, bg="#0288d1", padx=2, pady=2)
        save_btn_frame.pack(side=tk.RIGHT)
        
        # Save button
        save_btn = ttk.Button(
            save_btn_frame,
            text="Save Changes",
            style="Save.TButton",
            command=self.update_reservation
        )
        save_btn.pack()
        
        # Create a frame for the delete button to add a red background
        delete_btn_frame = tk.Frame(button_frame, bg="#ff5252", padx=2, pady=2)
        delete_btn_frame.pack(side=tk.RIGHT, padx=10)
        
        # Delete button
        delete_btn = ttk.Button(
            delete_btn_frame,
            text="Delete",
            style="Delete.TButton",
            command=self.delete_reservation
        )
        delete_btn.pack()
        
        # Cancel button
        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            style="Cancel.TButton",
            command=self.go_to_reservations
        )
        cancel_btn.pack(side=tk.RIGHT, padx=10)
    
    def load_reservation(self, reservation_id):
        """Load reservation details into the form fields"""
        self.reservation_id = reservation_id
        
        # Get reservation details from database
        reservation = self.db.get_reservation_by_id(reservation_id)
        
        if not reservation:
            messagebox.showerror("Error", "Reservation not found")
            self.go_to_reservations()
            return
        
        # Fill form fields with reservation details
        # Expected order: id, name, flight_number, departure, destination, date, seat
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, reservation[1])
        
        self.flight_entry.delete(0, tk.END)
        self.flight_entry.insert(0, reservation[2])
        
        self.departure_entry.delete(0, tk.END)
        self.departure_entry.insert(0, reservation[3])
        
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, reservation[4])
        
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, reservation[5])
        
        self.seat_entry.delete(0, tk.END)
        self.seat_entry.insert(0, reservation[6])
    
    def update_reservation(self):
        """Save changes to the reservation"""
        # Validate all fields
        name = self.name_entry.get().strip()
        flight_number = self.flight_entry.get().strip()
        departure = self.departure_entry.get().strip()
        destination = self.destination_entry.get().strip()
        date = self.date_entry.get().strip()
        seat_number = self.seat_entry.get().strip()
        
        if not (name and flight_number and departure and destination and date and seat_number):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Update reservation in database
        success = self.db.update_reservation(
            self.reservation_id,
            name,
            flight_number,
            departure,
            destination,
            date,
            seat_number
        )
        
        if success:
            messagebox.showinfo("Success", "Reservation updated successfully")
            self.go_to_reservations()
        else:
            messagebox.showerror("Error", "Failed to update reservation")
    
    def delete_reservation(self):
        """Delete the current reservation"""
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this reservation?"
        )
        
        if confirm:
            success = self.db.delete_reservation(self.reservation_id)
            
            if success:
                messagebox.showinfo("Success", "Reservation deleted successfully")
                self.go_to_reservations()
            else:
                messagebox.showerror("Error", "Failed to delete reservation")
    
    def show(self, reservation_id=None):
        """Display the edit reservation page"""
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # If reservation ID provided, load the reservation details
        if reservation_id:
            self.load_reservation(reservation_id)
    
    def hide(self):
        """Hide the edit reservation page"""
        self.frame.pack_forget()
