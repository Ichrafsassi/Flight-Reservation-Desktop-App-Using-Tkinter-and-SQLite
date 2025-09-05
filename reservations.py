"""
reservations.py - View and manage reservations

This module handles the view and management of existing reservations:
- Displays list of reservations
- Allows searching reservations
- Supports editing and deleting reservations
"""
import tkinter as tk
from tkinter import ttk, messagebox

class ReservationsPage:
    def __init__(self, root, db, go_back, edit_reservation):
        """
        Initialize the reservations page
        
        Args:
            root: The main Tkinter window
            db: Database instance
            go_back: Function to return to home page
            edit_reservation: Function to show edit reservation page
        """
        self.root = root
        self.db = db
        self.go_back = go_back
        self.edit_reservation = edit_reservation
        self.frame = tk.Frame(root)
        
        # Create and place UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all widgets for the reservations page"""
        
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
            state=tk.DISABLED  # Disable since we're already on this page
        )
        view_nav_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Main content area with white background
        content_frame = tk.Frame(self.frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Page title and search area
        title_frame = tk.Frame(content_frame, bg="white")
        title_frame.pack(fill=tk.X, padx=40, pady=(40, 20))
        
        # Left side - Title
        title_label = tk.Label(
            title_frame,
            text="Flight Reservations",
            font=("Arial", 24, "bold"),
            fg="#0288d1",
            bg="white"
        )
        title_label.pack(side=tk.LEFT, anchor=tk.W)
        
        # Right side - Search
        search_frame = tk.Frame(title_frame, bg="white")
        search_frame.pack(side=tk.RIGHT, anchor=tk.E)
        
        search_label = tk.Label(
            search_frame,
            text="Search:",
            font=("Arial", 12),
            bg="white"
        )
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            width=20,
            bd=1,
            relief=tk.SOLID
        )
        self.search_entry.pack(side=tk.LEFT, padx=(0, 5))
        self.search_entry.config(highlightthickness=1, highlightbackground="#ddd")
        
        search_btn = ttk.Button(
            search_frame,
            text="Search",
            command=self.search_reservations
        )
        search_btn.pack(side=tk.LEFT)
        
        # Table view of reservations with shadow effect
        table_shadow_frame = tk.Frame(content_frame, bg="#dddddd")
        table_shadow_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=(0, 40))
        
        # Actual table frame with slight offset to create shadow
        table_frame = tk.Frame(table_shadow_frame, bg="white", bd=1, relief=tk.SOLID)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=(0, 4))
        
        # Treeview for displaying reservations
        self.tree_frame = tk.Frame(table_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Scrollbar for treeview
        tree_scroll = ttk.Scrollbar(self.tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Define columns
        columns = ("id", "name", "flight_number", "from", "to", "date", "seat")
        self.tree = ttk.Treeview(
            self.tree_frame, 
            columns=columns, 
            show="headings", 
            yscrollcommand=tree_scroll.set
        )
        
        # Configure scrollbar
        tree_scroll.config(command=self.tree.yview)
        
        # Define headings
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Passenger Name")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("from", text="From")
        self.tree.heading("to", text="To")
        self.tree.heading("date", text="Date")
        self.tree.heading("seat", text="Seat")
        
        # Configure column widths
        self.tree.column("id", width=30, stretch=tk.NO)
        self.tree.column("name", width=150)
        self.tree.column("flight_number", width=100)
        self.tree.column("from", width=100)
        self.tree.column("to", width=100)
        self.tree.column("date", width=80)
        self.tree.column("seat", width=50)
        
        # Pack the treeview
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Action buttons below the table
        action_frame = tk.Frame(content_frame, bg="white")
        action_frame.pack(fill=tk.X, padx=40, pady=(0, 30))
        
        # Delete button
        delete_btn = ttk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_reservation
        )
        delete_btn.pack(side=tk.RIGHT, padx=5)
        
        # Edit button
        edit_btn = ttk.Button(
            action_frame,
            text="Edit Selected",
            command=self.on_edit_reservation
        )
        edit_btn.pack(side=tk.RIGHT, padx=5)
        
        # Refresh button
        refresh_btn = ttk.Button(
            action_frame,
            text="Refresh List",
            command=self.load_reservations
        )
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_reservation_selected)
    
    def load_reservations(self):
        """Load all reservations from database into treeview"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all reservations from database
        reservations = self.db.get_all_reservations()
        
        # Insert into treeview
        for res in reservations:
            self.tree.insert("", tk.END, values=res)
    
    def search_reservations(self):
        """Search reservations based on search entry"""
        search_term = self.search_entry.get().strip()
        
        # If empty search, show all reservations
        if not search_term:
            self.load_reservations()
            return
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search reservations
        results = self.db.search_reservations(search_term)
        
        # Insert results into treeview
        for res in results:
            self.tree.insert("", tk.END, values=res)
    
    def on_reservation_selected(self, event):
        """Handle reservation selection event"""
        # Method kept for compatibility but no longer needed
        pass
    
    def on_edit_reservation(self):
        """Open edit page for selected reservation"""
        selected_items = self.tree.selection()
        
        if not selected_items:
            messagebox.showinfo("Info", "Please select a reservation to edit")
            return
        
        # Get the ID of selected reservation
        item = self.tree.item(selected_items[0])
        values = item["values"]
        reservation_id = values[0]
        
        # Navigate to edit page
        self.edit_reservation(reservation_id)
    
    def delete_reservation(self):
        """Delete selected reservation"""
        selected_items = self.tree.selection()
        
        if not selected_items:
            messagebox.showinfo("Info", "Please select a reservation to delete")
            return
        
        # Get the ID of selected reservation
        item = self.tree.item(selected_items[0])
        values = item["values"]
        reservation_id = values[0]
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this reservation?"
        )
        
        if confirm:
            success = self.db.delete_reservation(reservation_id)
            
            if success:
                messagebox.showinfo("Success", "Reservation deleted successfully")
                self.load_reservations()
            else:
                messagebox.showerror("Error", "Failed to delete reservation")
    
    def show(self):
        """Display the reservations page"""
        self.frame.pack(fill=tk.BOTH, expand=True)
        # Load reservations when page is shown
        self.load_reservations()
    
    def hide(self):
        """Hide the reservations page"""
        self.frame.pack_forget()
