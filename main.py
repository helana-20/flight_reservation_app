import tkinter as tk
from pages import HomePage, BookingPage, ReservationsPage, EditReservationPage


class FlightReservationApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Flight Reservation App")
        self.geometry("400x300")

        self.frames = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Register all pages here
        for PageClass in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page = PageClass(container, self)
            self.frames[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


if __name__ == "_main_":
    app = FlightReservationApp()
    app.mainloop()