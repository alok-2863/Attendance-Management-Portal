import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.overrideredirect(True)

width = 550
height = root.winfo_screenheight()-100 # Get the screen height
# Calculate the x- and y-coordinates to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

root.geometry(f"{width}x{height}+{x}+{y}")
root.configure(bg='white')

# Load the logo image
logo = Image.open('logo_1.png')
logo_small = logo.resize((int(logo.width/3), int(logo.height/3))) # make small copy
logo_tk = ImageTk.PhotoImage(logo_small) # convert to tkinter compatible format

# Create a label widget to display the logo
label = tk.Label(root, image=logo_tk, bd=0)
label.pack(pady=(screen_height/2)-logo.height+5)


text_label= tk.Label(root, text="ATTENDANCE MANAGEMENT PORTAL" ,bg="white"  ,fg="black"  ,width=35  ,height=1,font=('Sitka Text Semibold', 18, 'bold')) 
text_label.place(x=9, y=height-75)

hello_label = tk.Label(root, text="THAPAR INSTITUTE OF ENGINEERING AND TECHNOLOGY" ,bg="white"  ,fg="red"  ,width=46  ,height=1,font=('Sitka Text Semibold', 12, 'bold'))
hello_label.place(x=40, y=height-40)

def animate():
    # Get current size of logo
    width, height = logo_small.size
    # Calculate target size
    target_width, target_height = logo.size
    # Calculate step size
    step_width = (target_width - width) / 20
    step_height = (target_height - height) / 20
    # Animate image
    for i in range(1, 21):
        new_width = int(width + i*step_width)
        new_height = int(height + i*step_height)
        new_logo = logo.resize((new_width, new_height))
        new_logo_tk = ImageTk.PhotoImage(new_logo)
        label.configure(image=new_logo_tk)
        root.update() # update window
        root.after(100) # wait a bit before updating again
    

animate()


# Set a timer to close the splash screen after 2 seconds
root.after(0, root.destroy)
os.system(f'python main_page.py')

root.mainloop()
