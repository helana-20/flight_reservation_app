import tkinter as tk
from tkinter import ttk, messagebox
from database import get_connection
from home import HomePage
from edit_reservation import EditReservationPage

class ReservationsPage(tk.Frame):
    def _init_(self, master):
        super()._init_(master)

        tk.Label(self, text="Reservations", font=("Arial", 16, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"), show="headings")
        self.tree.pack(fill="both", expand=True)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.load_data()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Edit", command=self.edit_reservation).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_reservation).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Back", command=lambda: master.show_frame(HomePage)).grid(row=0, column=2, padx=5)

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        for row in c.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def edit_reservation(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to edit")
            return
        data = self.tree.item(selected)["values"]
        self.master.show_frame(EditReservationPage, data)

    def delete_reservation(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to delete")
            return
        data = self.tree.item(selected)["values"]

        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (data[0],))
        conn.commit()
        conn.close()

        self.load_data()
        messagebox.showinfo("Deleted", "Reservation deleted successfully")