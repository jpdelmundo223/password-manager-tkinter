from tkinter import messagebox

def authenticate(this, username, password, func):
    if username == "" or password == "":
        messagebox.showerror("Error Message", "Incorrect username or password!")
    else:
        this.withdraw()
        func.deiconify()