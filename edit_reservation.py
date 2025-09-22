import tkinter as tk
from tkinter import messagebox
from database import get_connection
from reservations import ReservationsPage

class EditReservationPage(tk.Frame):
    def _init_(self, master, reservation_data):
        super()._init_(master)

        self.reservation_id = reservation_data[0]
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}

        tk.Label(self, text="Edit Reservation", font=("Arial", 16, "bold")).pack(pady=10)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field, width=15, anchor="w").grid(row=i, column=0, pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.insert(0, reservation_data[i+1])
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        tk.Button(self, text="Update", command=self.update_reservation).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: master.show_frame(ReservationsPage)).pack()

    def update_reservation(self):
        data = {field: entry.get() for field, entry in self.entries.items()}
        
        if any(v.strip() == "" for v in data.values()):
            messagebox.showwarning("Warning", "All fields are required!")
            return

        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, (data["Name"], data["Flight Number"], data["Departure"], data["Destination"], data["Date"], data["Seat Number"], self.reservation_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation updated!")
        self.master.show_frame(ReservationsPage)