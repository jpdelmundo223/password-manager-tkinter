import sqlite3
from tkinter import messagebox

def init_db():
    global con
    global cur
    """Initialize sqlite3 database and schemas
    
    :param None:"""
    con = sqlite3.connect('credentials.db')
    # Create database file
    cur = con.cursor()
    # Create table 
    cur.execute("""CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY,
        platform TEXT(20),
        username TEXT(20),
        password TEXT(20)
    )""")

def show_all():
    items = []
    items.clear()
    for item in cur.execute("""SELECT id,
                        platform,
                        username, 
                        password
                    FROM
                        credentials"""):
        items.append(item)
    return items

def select_by_id(id):
    row = cur.execute("""SELECT id,
                                platform,
                                username,
                                password
                        FROM
                            credentials
                        WHERE id = {}""".format(id))
    return row

def insert(platform: str, username: str, password: str, error: str, window):
    empty_fields = []
    if platform == "" or username == "" or password == "":
        if platform == "":
            empty_fields.append("Platform")
        if username == "":
            empty_fields.append("Username")
        if password == "":
            empty_fields.append("Password")
        error.set("All field is required!")
    else:
        window.withdraw()
        cur.execute("""INSERT INTO credentials (platform,
                                                username,
                                                password)
                        VALUES('{}',
                                '{}',
                                '{}'
                        )""".format(platform, username, password))
        con.commit()

def delete_all():
    confirm = messagebox.askquestion("Delete records", "Are you sure you want to delete all the records?", icon="warning")
    if confirm == "yes":
        cur.execute("""DELTE FROM credentials""")
        con.commit()