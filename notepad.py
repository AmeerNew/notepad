import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")
        self.text = tk.Text(master)
        self.text.pack()
        
        # Add menu
        self.menu = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Edit", command=self.edit_file)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        master.config(menu=self.menu)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                file_content = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, file_content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                file_content = self.text.get("1.0", tk.END)
                f.write(file_content)

    def edit_file(self):
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit")
        edit_text = tk.Text(edit_window)
        edit_text.pack()
        edit_text.insert(tk.END, self.text.get("1.0", tk.END))
        save_button = tk.Button(edit_window, text="Save", command=lambda: self.save_edit(edit_text))
        save_button.pack()

    def save_edit(self, edit_text):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, edit_text.get("1.0", tk.END))

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
