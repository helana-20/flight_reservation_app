import tkinter as tk
from home import HomePage
from database import init_db

class App(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Flight Reservation System")
        self.geometry("600x400")
        self.resizable(False, False)

        init_db()  # Initialize database

        self.current_frame = None
        self.show_frame(HomePage)

    def show_frame(self, frame_class, *args, **kwargs):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "_main_":
    app = App()
    app.mainloop()