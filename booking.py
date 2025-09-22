import tkinter as tk
from tkinter import messagebox
import sqlite3
from database import get_connection
from home import HomePage

class BookingPage(tk.Frame):
    def _init_(self, master):
        super()._init_(master)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        tk.Label(self, text="Book a Flight", font=("Arial", 16, "bold")).pack(pady=10)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field, anchor="w", width=15).grid(row=i, column=0, pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        tk.Button(self, text="Submit", command=self.save_reservation).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: master.show_frame(HomePage)).pack()

    def save_reservation(self):
        data = {field: entry.get() for field, entry in self.entries.items()}
        
        if any(v.strip() == "" for v in data.values()):
            messagebox.showwarning("Warning", "All fields are required!")
            return

        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
                  (data["Name"], data["Flight Number"], data["Departure"], data["Destination"], data["Date"], data["Seat Number"]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation saved!")
        self.master.show_frame(HomePage)