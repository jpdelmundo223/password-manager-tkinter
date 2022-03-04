from tkinter import StringVar, Tk, Menu, N, Toplevel
from tkinter import ttk
from utils import center_window, generate_random_password
from auth import authenticate

def password_manager_window():
    password_manager = Toplevel()
    password_manager.title("Password Manager")
    password_manager.geometry("700x300")
    password_manager.resizable(
        False, 
        False
    )

    app = App()
    top_menu = Menu(password_manager)
    password_manager.config(menu=top_menu)

    options_menu = Menu(
        top_menu,
        tearoff=0
    )

    top_menu.add_cascade(
        label="File",
        menu=options_menu
    )
    
    options_menu.add_command(
        label="Generate New Password",
        command=lambda: [password_generator_dialog()]
    )

    options_menu.add_command(
        label="Logout",
        command=lambda:[password_manager.destroy(), app.deiconify()]
    )

    options_menu.add_separator()

    options_menu.add_command(
        label="Exit",
        command=lambda:[password_manager.destroy()]
    )

    about_menu = Menu(
        top_menu,
        tearoff=0
    )

    top_menu.add_cascade(
        label="Help",
        menu=about_menu
    )

    about_menu.add_command(
        label="About",
        command=lambda: [about_dialog()]
    )

    settings_menu = Menu(
        top_menu,
        tearoff=0
    )

    top_menu.add_cascade(
        label="Settings",
        menu=settings_menu
    )

    settings_menu.add_command(
        label="Change Master Password"
    )

    password_label = ttk.Label(
    password_manager,
    text="Genarated Password",
    wraplength=150
    ).pack()

    password_string_var = StringVar()
    password_entry = ttk.Label(
        password_manager,
        textvariable=password_string_var,
    ).pack()

    sample_label = ttk.Label(
        password_manager,
        text="Sample Label"
    )

    generate_password_button = ttk.Button(
        password_manager,
        text="Generate",
        command=lambda:[password_string_var.set(generate_random_password())]
    ).pack()

    center_window(root=password_manager, width=400, height=300)

    return password_manager

def about_dialog():
    about = Toplevel()
    about.title("About")

    about_label = ttk.Label(
        about,
        text="This application is created using Python and Tkinter, and was developed to help users manage their account credentials.",
        wraplength=150
    ).grid(row=1, column=2, sticky=N)

    about.resizable(
        False, 
        False
    )

def password_generator_dialog():
    password_generator = Toplevel()
    password_generator.title("Generate Password")   
    password_generator.geometry

    password_label = ttk.Label(
        password_generator,
        text="Genarated Password",
        wraplength=150
    ).pack()
    
    password_string_var = StringVar()
    password_entry = ttk.Label(
        password_generator,
        textvariable=password_string_var,
    ).pack()

    generate_password_button = ttk.Button(
        password_generator,
        text="Generate",
        command=lambda:[password_string_var.set(generate_random_password()), password_generator.update_idletasks]
    ).pack()

    password_generator.resizable(
        False, 
        False
    )

    center_window(root=password_generator, width=200, height=100)

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Login")
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        
        username_label = ttk.Label(
            self,
            text="Username"
        ).grid(column=1, row=1)

        username_var = StringVar()
        username_entry = ttk.Entry(
            self,
            textvariable=username_var
        ).grid(column=2, row=1)

        password_label = ttk.Label(
            self,
            text="Password"
        ).grid(column=1, row=2)

        password_var = StringVar()
        password_entry = ttk.Entry(
            self,
            textvariable=password_var,
            show="*"
        ).grid(column=2, row=2)

        login_button = ttk.Button(
            text="Login",
            command=lambda:[authenticate(self, username_var.get(), password_var.get(), password_manager_window())]
        ).grid(column=2, row=3)

        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()