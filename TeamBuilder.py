import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random  # Add this line for the random module

APP_VERSION = "1.0"

class NamePickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title(f"Team Builder v{APP_VERSION}")
        self.names = []
        self.undo_stack = []
        self.groups = ""
        self.num_groups_var = tk.StringVar(value=2)
        self.window_size_var = tk.StringVar(value=self.get_window_size())

        # Load the background image directly using Tkinter PhotoImage
        self.background_photo = tk.PhotoImage(file=r".\fish.png")
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        self.name_entry = ttk.Entry(self.master, font=("Helvetica", 12))
        self.names_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE)
        self.groups_display = tk.Label(self.master, text="")
        self.num_groups_entry = ttk.Entry(self.master, textvariable=self.num_groups_var, width=5)
        self.window_size_display = ttk.Entry(self.master, textvariable=self.window_size_var, state='readonly')

        self.setup_bindings()
        self.place_widgets()

    def create_button(self, text, command, x, y, width=10):
        button = ttk.Button(self.master, text=text, command=command, width=width)
        button.place(x=x, y=y, anchor="nw")
        return button

    def setup_bindings(self):
        self.master.bind('<Return>', lambda event: self.add_name())
        self.master.bind('<Configure>', lambda event: self.update_window_size())

    def place_widgets(self):
        self.name_entry.place(x=5, y=5, width=270, anchor="nw")
        self.names_listbox.place(x=5, y=55, anchor="nw")
        tk.Label(self.master, text="Groups:").place(x=5, y=220, anchor="nw")
        self.groups_display.place(x=5, y=220, anchor="nw")
        tk.Label(self.master, text="Number of Groups:").place(x=5, y=330, anchor="nw")
        self.num_groups_entry.place(x=120, y=330, width=20, anchor="nw")
      #  tk.Label(self.master, text="Window Size:").place(x=5, y=330, anchor="nw")
      #  self.window_size_display.place(x=80, y=330, width=60, anchor="nw")

        buttons = [
            ("Remove Selected", self.remove_selected, 5, 30, 15),
            ("Undo", self.undo, 105, 30),
            ("Generate Groups", self.pick_groups, 175, 30, 15),
            ("Save Data", self.save_data, 175, 100),
            ("Load Data", self.load_data, 175, 160),
        ]

        for button_info in buttons:
            self.create_button(*button_info)

        self.config_grid_weights()

    def get_window_size(self):
        return f"{self.master.winfo_width()} x {self.master.winfo_height()}"

    def update_window_size(self):
        self.window_size_var.set(self.get_window_size())

    def add_name(self):
        name = self.name_entry.get()
        if name:
            self.names.append(name)
            self.names_listbox.insert(tk.END, name)
            self.undo_stack.append(("add", name))
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a name.")

    def remove_selected(self):
        selected_indices = self.names_listbox.curselection()
        if selected_indices:
            removed_names = [self.names.pop(index) for index in reversed(selected_indices)]
            for index in selected_indices[::-1]:
                self.names_listbox.delete(index)
            self.undo_stack.append(("remove", removed_names))
        else:
            messagebox.showwarning("Warning", "Select names to remove.")

    def undo(self):
        if self.undo_stack:
            action, data = self.undo_stack.pop()
            if action == "add":
                index = self.names.index(data)
                self.names.pop(index)
                self.names_listbox.delete(index)
            elif action == "remove":
                for name in data:
                    self.names.append(name)
                    self.names_listbox.insert(tk.END, name)

    def pick_groups(self):
        num_groups = self.get_num_groups()
        if len(self.names) >= num_groups:
            self.groups = self.generate_groups(num_groups)
            self.groups_display.config(text=self.groups)
        else:
            messagebox.showwarning("Warning", f"Add at least {num_groups} names to pick groups.")

    def generate_groups(self, num_groups):
        if len(self.names) >= num_groups:
            random.shuffle(self.names)
            group_size = len(self.names) // num_groups
            groups = [self.names[i:i+group_size] for i in range(0, len(self.names), group_size)]
            return "\n".join([f"Group {i + 1}: {group}" for i, group in enumerate(groups)])
        else:
            return ""

    def get_num_groups(self):
        try:
            num_groups = int(self.num_groups_var.get())
            return max(2, num_groups)
        except ValueError:
            messagebox.showwarning("Warning", "Invalid input for the number of groups. Using default value (2).")
            return 2

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write("\n".join(self.names))
                file.write("\n\nGroups:\n" + self.groups)
            messagebox.showinfo("Save Successful", "Data saved successfully.")

    def load_data(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read().split("\n\nGroups:\n")
                self.names = data[0].splitlines()
                self.groups = data[1] if len(data) > 1 else ""
                self.names_listbox.delete(0, tk.END)
                for name in self.names:
                    self.names_listbox.insert(tk.END, name)
                self.groups_display.config(text=self.groups)
                self.num_groups_var.set(len(self.groups.splitlines()))
            messagebox.showinfo("Load Successful", "Data loaded successfully.")

    def close_window(self):
        self.master.destroy()

    def config_grid_weights(self):
        for i in range(1, 6):
            self.master.grid_rowconfigure(i, weight=1)
        self.master.grid_rowconfigure(6, weight=1)
        self.master.grid_rowconfigure(7, weight=1)
        self.master.grid_rowconfigure(8, weight=1)
        self.master.grid_rowconfigure(9, weight=1)
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)


def run_application():
    root = tk.Tk()
    root.geometry("280x350")
    app = NamePickerApp(root)
    # Disable window resizing
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    run_application()
