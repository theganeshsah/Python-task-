import tkinter as tk
from tkinter import messagebox
class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize contact list
        self.contacts = []

        # creating component
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Boxes design
        self.name_label.grid(row=0, column=0, sticky="E")
        self.name_entry.grid(row=0, column=1)

        self.phone_label.grid(row=1, column=0, sticky="E")
        self.phone_entry.grid(row=1, column=1)

        self.email_label.grid(row=2, column=0, sticky="E")
        self.email_entry.grid(row=2, column=1)

        self.address_label.grid(row=3, column=0, sticky="E")
        self.address_entry.grid(row=3, column=1)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{i+1}. {contact['Name']} - {contact['Phone']}" for i, contact in enumerate(self.contacts)])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        name_to_search = self.name_entry.get()
        found_contacts = [contact for contact in self.contacts if name_to_search.lower() in contact["Name"].lower()]

        if found_contacts:
            contact_list = "\n".join([f"{i+1}. {contact['Name']} - {contact['Phone']}" for i, contact in enumerate(found_contacts)])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Info", "No matching contacts found.")

    def update_contact(self):
        # this update contact as user requriment
        pass

    def delete_contact(self):
        # deleate cotact as user requriment
        pass

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
