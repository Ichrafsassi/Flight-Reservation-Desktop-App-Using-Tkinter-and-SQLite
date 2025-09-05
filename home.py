"""
home.py - Home page UI for the Flight Reservation App

This module provides the main navigation interface for the Flight Reservation App.
It displays options to:
- Book a new flight
- View existing reservations
- Exit the application
"""
import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, show_booking_page, show_reservations_page):
        """
        Initialize the home page
        
        Args:
            root: The main Tkinter window
            show_booking_page: Function to display the booking page
            show_reservations_page: Function to display the reservations page
        """
        self.root = root
        self.frame = tk.Frame(root)
        
        # Store callback functions
        self.show_booking_page = show_booking_page
        self.show_reservations_page = show_reservations_page
        
        # Create and place UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all widgets for the home page"""
        
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
        )
        home_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        book_nav_btn = ttk.Button(
            header_frame, 
            text="Book Flight",
            style="Nav.TButton",
            command=self.show_booking_page
        )
        book_nav_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        view_nav_btn = ttk.Button(
            header_frame, 
            text="View Reservations",
            style="Nav.TButton",
            command=self.show_reservations_page
        )
        view_nav_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Main content area
        content_frame = tk.Frame(self.frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            content_frame,
            text="Welcome to FlySky Reservations",
            font=("Arial", 28, "bold"),
            bg="white",
            fg="#0288d1"
        )
        title_label.pack(pady=(20, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            content_frame,
            text="Book your flights and manage your reservations with our simple and intuitive system.",
            font=("Arial", 12),
            bg="white",
            fg="#555555",
            wraplength=600
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Create a frame for the two cards
        cards_frame = tk.Frame(content_frame, bg="white")
        cards_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Left card - Book a Flight - Add shadow effect with frame
        book_card_shadow = tk.Frame(cards_frame, bg="#dddddd")
        book_card_shadow.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True, pady=(0, 5))
        
        book_card = tk.Frame(book_card_shadow, bg="white", bd=1, relief=tk.SOLID)
        book_card.pack(fill=tk.BOTH, expand=True, padx=2, pady=(0, 2))
        
        # Book flight icon - more professional with a circle background
        icon_frame = tk.Frame(book_card, bg="#0288d1", width=70, height=70)
        icon_frame.pack(pady=(20, 10))
        icon_frame.pack_propagate(False)  # Don't shrink frame to fit content
        
        book_icon_label = tk.Label(
            icon_frame, 
            text="✈", 
            font=("Arial", 32, "bold"), 
            bg="#0288d1",
            fg="white"
        )
        book_icon_label.pack(expand=True)
        
        book_title = tk.Label(
            book_card,
            text="Book a Flight",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#0288d1"
        )
        book_title.pack(pady=(0, 10))
        
        book_desc = tk.Label(
            book_card,
            text="Reserve your next flight by providing your details and flight information.",
            font=("Arial", 10),
            bg="white",
            wraplength=250,
            height=3
        )
        book_desc.pack(pady=(0, 20))
        
        # Book button with blue background
        book_btn_style = ttk.Style()
        book_btn_style.configure("Book.TButton", font=('Arial', 11, 'bold'))
        
        # Create a frame with blue background for the button
        book_btn_frame = tk.Frame(book_card, bg="#0288d1", padx=2, pady=2)
        book_btn_frame.pack(pady=(0, 20))
        
        book_button = ttk.Button(
            book_btn_frame,
            text="Book Flight",
            style="Book.TButton",
            command=self.show_booking_page
        )
        book_button.pack()
        
        # Right card - View Reservations - Add shadow effect with frame
        view_card_shadow = tk.Frame(cards_frame, bg="#dddddd")
        view_card_shadow.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True, pady=(0, 5))
        
        view_card = tk.Frame(view_card_shadow, bg="white", bd=1, relief=tk.SOLID)
        view_card.pack(fill=tk.BOTH, expand=True, padx=2, pady=(0, 2))
        
        # View icon - more professional with a circle background
        view_icon_frame = tk.Frame(view_card, bg="#0288d1", width=70, height=70)
        view_icon_frame.pack(pady=(20, 10))
        view_icon_frame.pack_propagate(False)  # Don't shrink frame to fit content
        
        view_icon_label = tk.Label(
            view_icon_frame, 
            text="➔", 
            font=("Arial", 32, "bold"), 
            bg="#0288d1",
            fg="white"
        )
        view_icon_label.pack(expand=True)
        
        view_title = tk.Label(
            view_card,
            text="View Reservations",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#0288d1"
        )
        view_title.pack(pady=(0, 10))
        
        view_desc = tk.Label(
            view_card,
            text="Manage your existing reservations, view details, edit or cancel if needed.",
            font=("Arial", 10),
            bg="white",
            wraplength=250,
            height=3
        )
        view_desc.pack(pady=(0, 20))
        
        # View button with blue background
        # Create a frame with blue background for the button
        view_btn_frame = tk.Frame(view_card, bg="#0288d1", padx=2, pady=2)
        view_btn_frame.pack(pady=(0, 20))
        
        view_button = ttk.Button(
            view_btn_frame,
            text="View Reservations",
            style="Book.TButton",
            command=self.show_reservations_page
        )
        view_button.pack()
    
    def show(self):
        """Display the home page"""
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        """Hide the home page"""
        self.frame.pack_forget()
