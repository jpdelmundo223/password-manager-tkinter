from random import randint
from random import shuffle

def generate_random_password():
    """Function that helps user to generate random characteres 
    consists of letter and number (20 in length)
    
    :return:"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = 1234567890
    password = []
    for l in range(0, 10):
        password.append(letters[randint(0, len(letters) - 1)])
    for n in range(0, 10):
        password.append(str(numbers)[randint(0, len(str(numbers)) - 1)])
    shuffle(password)
    return ''.join(password)

def center_window(root, height: int, width: int):
    """Function that """
    window_height = height
    window_width = width

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))