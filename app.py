from tkinter import ttk
from tkinter import Tk, Menu, StringVar, Toplevel, ACTIVE
from utils import center_window, generate_random_password
from database import delete_all, init_db, insert, select_by_id, show_all
from functools import partial

def generate_password_window():
    window = Toplevel(
        padx=12,
        pady=12
    )
    window.title("Generate Password")
    window.geometry("300x200")
    window.resizable(
        False,
        False
    )

    password_label = ttk.Label(
        window,
        text="Generated Password"
    ).pack()

    global password_var
    password_var = StringVar()
    password_entry = ttk.Entry(
        window,
        textvariable=password_var,
        width=25,
        state=ACTIVE
    ).pack(pady=12)

    generate_button = ttk.Button(
        window,
        text="Generate",
        command=lambda:[password_var.set(generate_random_password())]
    ).place(x=45, y=75)

    close_button = ttk.Button(
        window,
        text="Close",
        command=lambda:[window.withdraw()]
    ).place(x=150, y=75)

    center_window(window, 150, 300)

    return window

class App(Tk):

    def __init__(self):
        init_db()

        super().__init__()
        self.title("Password Manager")
        self.geometry("900x300")    
        self.resizable(
            False,
            False
        )

        # creating the menubar
        self.menu_bar = Menu(
            self
        )

        self.config(menu=self.menu_bar)

        self.file_menu = Menu(
            self.menu_bar,
            tearoff=0
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu
        )

        self.file_menu.add_command(
            label="Exit",
            command=lambda: [self.destroy()]
        )

        self.options_menu = Menu(
            self.menu_bar,
            tearoff=0
        )

        self.menu_bar.add_cascade(
            label="Options",
            menu=self.options_menu
        )

        self.options_menu.add_command(
            label="Generate Password",
            command=lambda:[generate_password_window().deiconify()]
        )

        # credentials_table = Frame(
        #     self,
        #     bg="black"
        # )
        # credentials_table.pack(
        #     pady=25
        # )

        # my_game = ttk.Treeview(
        #     credentials_table
        # )

        # my_game['columns'] = ('platform', 'username', 'password')

        # my_game.column("#0", width=0,  stretch=NO)
        # my_game.column("platform",anchor=CENTER, width=80)
        # my_game.column("username",anchor=CENTER,width=80)
        # my_game.column("password",anchor=CENTER,width=80)

        # my_game.heading(
        #     "#0",
        #     text="",
        #     anchor=CENTER
        # )

        # my_game.heading(
        #     "platform",
        #     text="Id",
        #     anchor=CENTER
        # )
        # my_game.heading(
        #     "username",
        #     text="Username",
        #     anchor=CENTER
        # )
        # my_game.heading(
        #     "password",
        #     text="Password",
        #     anchor=CENTER
        # )

        # my_game.pack()

        self.id_header = ttk.Label(
            self,
            text="ID",
        ).grid(column=1, row=1, padx=50, pady=12)

        self.platform_header = ttk.Label(
            self,
            text="Platform",
        ).grid(column=2, row=1, padx=50)

        self.username_header = ttk.Label(
            self,
            text="Username",
        ).grid(column=3, row=1, padx=50)

        self.password_header = ttk.Label(
            self,
            text="Password",
        ).grid(column=4, row=1, padx=50)

        self.actions_header = ttk.Label(
            self,
            text="Actions",
        ).grid(column=5, row=1, padx=50)

        self.underline = ttk.Label(
            self,
            text="-"*136,
        ).place(x=20, y=26)

        def load_items():
            if show_all() is not None:
                row_counter = 2
                for id, platform, username, password in show_all():
                    row_counter += 1
                    self.id_row = ttk.Label(
                        self,
                        text=id,
                    ).grid(column=1, row=row_counter)

                    self.platform_row = ttk.Label(
                        self,
                        text=platform,
                    ).grid(column=2, row=row_counter)

                    self.username_row = ttk.Label(
                        self,
                        text=username,
                    ).grid(column=3, row=row_counter)

                    self.password_row = ttk.Label(
                        self,
                        text=password,
                    ).grid(column=4, row=row_counter)
                    
                    button_text = "Edit {}".format(id)

                    self.edit = ttk.Button(
                        self,
                        text=button_text,
                        command=partial(lambda:[edit_credential(self, button_text.split(" ")[1])])
                    ).grid(column=5, row=row_counter)
        load_items()
        
        self.add_credential_button = ttk.Button(
            text="Add credential",
            command=lambda:[add_credential(self)]
        ).place(x=780, y=25)

        self.delete_credential = ttk.Button(
            text="Delete all",
            command=lambda:[delete_all(), load_items()]
        ).place(x=790, y=65)

        def add_credential(self):
            self = Toplevel()
            self.title("Add New Credential")
            self.geometry("300x200")
            self.width = 300

            self.platform_label = ttk.Label(
                self,
                text="Enter platform:"
            ).place(x=12, y=25)

            self.platform_var = StringVar()
            self.platform_entry = ttk.Entry(
                self,
                textvariable=self.platform_var
            ).place(x=150, y=25)

            self.username_label = ttk.Label(
                self,
                text="Enter username:"
            ).place(x=12, y=50)

            self.username_var = StringVar()
            self.username_entry = ttk.Entry(
                self,
                textvariable=self.username_var
            ).place(x=150, y=50)

            self.password_label = ttk.Label(
                self,
                text="Enter username:"
            ).place(x=12, y=75)

            self.password_var = StringVar()
            self.password_entry = ttk.Entry(
                self,
                textvariable=self.password_var
            ).place(x=150, y=75)

            self.error_message_var = StringVar()
            self.add_button = ttk.Button(
                self,
                text="Add",
                command=lambda:[insert(platform=self.platform_var.get(),
                                    username=self.username_var.get(),
                                    password=self.password_var.get(), 
                                    error=self.error_message_var, 
                                    window=self), 
                                    load_items()]
            ).place(x=65, y=120)

            self.cancel_button = ttk.Button(
                self,
                text="Cancel",
                command=lambda:[self.withdraw()]
            ).place(x=165, y=120)

            self.error_message_label = ttk.Label(
                self,
                textvariable=self.error_message_var,
                foreground="red",
            ).place(x=100, y=165)

            center_window(self, 200, 300)

        def edit_credential(self, id):
            print(id)
            self = Toplevel()
            self.title("Edit Credential")
            self.geometry("300x200")
            self.width = 300

            for id, platform, username, password in select_by_id(id):
                platform_label = ttk.Label(
                    self,
                    text="Enter platform:"
                ).place(x=12, y=25)

                platform_entry = ttk.Entry(
                    self,
                    text=platform
                ).place(x=150, y=25)

                username_label = ttk.Label(
                    self,
                    text="Enter username:"
                ).place(x=12, y=50)

                username_entry = ttk.Entry(
                    self,
                    text=username
                ).place(x=150, y=50)

                password_label = ttk.Label(
                    self,
                    text="Enter username:"
                ).place(x=12, y=75)

                password_entry = ttk.Entry(
                    self,
                    text=password
                ).place(x=150, y=75)

            self.error_message_var = StringVar()
            self.add_button = ttk.Button(
                self,
                text="Save",
                command=lambda:[insert(platform=self.platform_var.get(),
                                    username=self.username_var.get(),
                                    password=self.password_var.get(), 
                                    error=self.error_message_var, 
                                    window=self), 
                                    load_items()]
            ).place(x=65, y=120)

            self.cancel_button = ttk.Button(
                self,
                text="Cancel",
                command=lambda:[self.withdraw()]
            ).place(x=165, y=120)

            self.error_message_label = ttk.Label(
                self,
                textvariable=self.error_message_var,
                foreground="red",
            ).place(x=100, y=165)

            center_window(self, 200, 300)

        center_window(self, 300, 900)

if __name__ == "__main__":
    app = App()
    app.mainloop()