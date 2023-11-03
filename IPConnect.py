import tkinter as easygui
import socket as socks
from PIL import ImageGrab

def create_new_window():
    ip = poot_textbox.get()
    port = poot_textbox2.get()
    new_window = easygui.Tk()
    new_window.title(ip+":"+port)
    try:
        # Create a socket object
        sock = socks.socket(socks.AF_INET, socks.SOCK_STREAM)
        sock.connect((ip, port))
        failed = False
    except:
        def kill():
            error_window.destroy()
            new_window.destroy()
        failed = True
        error_window = easygui.Tk()

        error_window.title("Error found")

        error_text = easygui.Label(error_window, text="""

An error has occurred. Check the IP/port number.
                                   
                                   """)
        error_text.pack()

        error_button = easygui.Button(error_window, text="Okay", command=kill)
        error_button.pack()

        error_window.mainloop()
    new_window.mainloop()
    while True:
        # Capture the screen
        screenshot = ImageGrab.grab()
        image = easygui.Image(new_window, imgtype=screenshot)



# Create the main window
window = easygui.Tk()
window.geometry("320x180")
window.title("IPConnect")

# Add the title
Title = easygui.Label(window, text="Welcome to IPConnect.")
Title.pack()

# Create the text box
poot_label = easygui.Label(window, text="Put the IP below.")
poot_label.pack() # Makes the label
poot_textbox = easygui.Entry(window)
poot_textbox.pack() # Makes the text box

# Create the port text box
# Create the text box
poot_label2 = easygui.Label(window, text="Put the Port below.")
poot_label2.pack() # Makes the label
poot_textbox2 = easygui.Entry(window)
poot_textbox2.pack() # Makes the text box

# Create the buttons
button = easygui.Button(window, text="Connect to machine", command=create_new_window)
button.pack()

button2 = easygui.Button(window, text="View files of machine", command=create_new_window)
button2.pack()

# Start the main window's event loop
window.mainloop()