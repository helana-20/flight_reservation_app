import tkinter as tk


class HomePage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        label = tk.Label(self, text="Home Page", font=("Arial", 18))
        label.pack(pady=20)

        tk.Button(self, text="Go to Booking Page",
                  command=lambda: controller.show_frame(BookingPage)).pack(pady=5)

        tk.Button(self, text="View Reservations",
                  command=lambda: controller.show_frame(ReservationsPage)).pack(pady=5)


class BookingPage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        label = tk.Label(self, text="Booking Page", font=("Arial", 18))
        label.pack(pady=20)

        tk.Button(self, text="Confirm Booking",
                  command=lambda: controller.show_frame(HomePage)).pack(pady=5)

        tk.Button(self, text="Back to Home",
                  command=lambda: controller.show_frame(HomePage)).pack(pady=5)


class ReservationsPage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        label = tk.Label(self, text="Reservations", font=("Arial", 18))
        label.pack(pady=20)

        tk.Button(self, text="Edit Reservation",
                  command=lambda: controller.show_frame(EditReservationPage)).pack(pady=5)

        tk.Button(self, text="Back to Home",
                  command=lambda: controller.show_frame(HomePage)).pack(pady=5)


class EditReservationPage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        label = tk.Label(self, text="Edit Reservation", font=("Arial", 18))
        label.pack(pady=20)

        tk.Button(self, text="Save Changes",
                  command=lambda: controller.show_frame(ReservationsPage)).pack(pady=5)

        tk.Button(self, text="Back to Reservations",
                  command=lambda: controller.show_frame(ReservationsPage)).pack(pady=5)