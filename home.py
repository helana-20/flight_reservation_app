import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage(tk.Frame):
    def _init_(self, master):
        super()._init_(master)
        
        tk.Label(self, text="Flight Reservation System", font=("Arial", 18, "bold")).pack(pady=40)
        
        tk.Button(self, text="Book Flight", width=20, command=lambda: master.show_frame(BookingPage)).pack(pady=10)
        tk.Button(self, text="View Reservations", width=20, command=lambda: master.show_frame(ReservationsPage)).pack(pady=10)