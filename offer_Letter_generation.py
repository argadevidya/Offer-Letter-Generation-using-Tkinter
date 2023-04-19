import tkinter as tk

from tkinter import messagebox
import datetime

class OfferLetterGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Offer Letter Generator")

        # Company Information
        self.company_label = tk.Label(master, text="Company Name:")
        self.company_label.grid(row=0, column=0)
        self.company_entry = tk.Entry(master)
        self.company_entry.grid(row=0, column=1)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=1, column=0)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=1, column=1)

        self.city_label = tk.Label(master, text="City:")
        self.city_label.grid(row=2, column=0)
        self.city_entry = tk.Entry(master)
        self.city_entry.grid(row=2, column=1)

        self.state_label = tk.Label(master, text="State:")
        self.state_label.grid(row=3, column=0)
        self.state_entry = tk.Entry(master)
        self.state_entry.grid(row=3, column=1)

        self.zip_label = tk.Label(master, text="Zip:")
        self.zip_label.grid(row=4, column=0)
        self.zip_entry = tk.Entry(master)
        self.zip_entry.grid(row=4, column=1)

        # Candidate Information
        self.name_label = tk.Label(master, text="Candidate Name:")
        self.name_label.grid(row=5, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=5, column=1)

        self.position_label = tk.Label(master, text="Position:")
        self.position_label.grid(row=6, column=0)
        self.position_entry = tk.Entry(master)
        self.position_entry.grid(row=6, column=1)

        self.salary_label = tk.Label(master, text="Salary:")
        self.salary_label.grid(row=7, column=0)
        self.salary_entry = tk.Entry(master)
        self.salary_entry.grid(row=7, column=1)

        # Buttons
        self.generate_button = tk.Button(master, text="Generate Offer Letter", command=self.generate_offer_letter)
        self.generate_button.grid(row=8, column=0)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_form)
        self.clear_button.grid(row=8, column=1)

    def generate_offer_letter(self):
        # Get data from entries
        company = self.company_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        zip_code = self.zip_entry.get()
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        # Generate offer letter
        offer_letter = f"""
        {name}
        {address}
        {city}, {state} {zip_code}

        Dear {name},

        We are delighted to offer you the position of {position} at {company}. Your starting salary will be {salary} per year. We are confident that you will be an asset to our company and look forward to welcoming you aboard.

        Please let us know by {datetime.datetime.now() + datetime.timedelta(days=7)} if you accept our offer. We look forward to hearing from you.

        Sincerely,
        {company}
        """

        # Show offer letter
        messagebox.showinfo("Offer Letter", offer_letter)

    def clear_form(self):
        # Clear all entries
        self.company_entry.delete(0, tk.END)
        self.address
root = tk.Tk()
my_gui = OfferLetterGenerator(root)
root.mainloop()