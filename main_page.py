import tkinter as tk
from tkinter import ttk
import os
import csv

root = tk.Tk()
root.overrideredirect(True)
width = 550
height = root.winfo_screenheight() - 100 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))
root.geometry(f"{width}x{height}+{x}+{y}")

def button_pressed(button_num):
    root.destroy()
    os.system(f'python attendance.py {button_num}')

with open('class.csv', 'r') as file:
    csv_reader = csv.reader(file)
    n = sum(1 for row in csv_reader) - 1
    file.seek(0)  # Reset the file pointer
    next(csv_reader)  # Skip the header row

    # Create a list of buttons
    buttons = []
    for i, row in enumerate(csv_reader):
        button_num = i + 1
        button = tk.Button(
            text=f"  CLASS: {row[0]}\n  SUBJECT: {row[1]}",
            width=31,
            height=2,
            bg="#b4b4b5",
            fg="black",
            font=("Cascadia Code", 13),
            command=lambda num=button_num: os.system(f"python run.py {num}"),
            anchor="center",
            justify="center",
            bd=6,
        )
        buttons.append(button)


logo_frame = tk.Frame(root, bg="white", height=100)
logo_frame.pack(side="top", fill="x")
logo_image = tk.PhotoImage(file="logo.png").subsample(1)
logo_label = tk.Label(logo_frame, image=logo_image, bd=0)
logo_label.pack(side="left", anchor="nw", padx=10, pady=10)

text_label = tk.Label(logo_frame,text="ATTENDANCE\nMANAGEMENT PORTAL",bg="white",fg="black",width=35,height=2, font=("Sitka Text Semibold", 18, "bold underline"),)
text_label.pack(pady=10, anchor="nw")

# Create a line separator
line_canvas = tk.Canvas(root, height=1, width=700, bg="black", highlightthickness=0)
line_canvas.create_line(0, 0, width, 0, fill="black")
line_canvas.place(x=75, y=130)

# Create a frame for the table
table_frame = tk.Frame(root, padx=13, pady=13)
table_frame.pack(side="top", fill="both", expand=True)

# Create a scrollbar
scrollbar = ttk.Scrollbar(table_frame)
scrollbar.pack(side="right", fill="y", padx=1, pady=1)

# Create a table
table = tk.Text(table_frame,yscrollcommand=scrollbar.set,wrap="none",highlightbackground="black",bd=10,bg="blue",fg="black",)
table.pack(side="left", fill="both", expand=True)

# Configure the scrollbar to work with the table
scrollbar.config(command=table.yview)
table.config(yscrollcommand=scrollbar.set, highlightthickness=0, padx=2, pady=2)

with open('class.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i, a in enumerate(csv_reader, start=1):
        button = tk.Button(table,text=f"  CLASS: {a[0]}\n  SUBJECT: {a[1]}",width=31,height=2,bg="#b4b4b5",fg="black",
            font=("Cascadia Code", 13),command=lambda num=i: button_pressed(num),anchor="center",justify="center", bd=6,)
        table.window_create("end", window=button, padx=75, pady=10)
        table.insert("end", "\n")
nm = i

bottom_logo_frame = tk.Frame(root, bg="white")
bottom_logo_frame.pack(side="bottom", fill="x", padx=0, pady=0)

button_image = tk.PhotoImage(file="button.png")
button = tk.Button(bottom_logo_frame,image=button_image,bd=0,highlightbackground="white",bg="white",highlightcolor="white",command=lambda: (root.destroy(), os.system(f"python register_class.py {nm}")),)
button.pack(side="right", anchor="se", padx=20, pady=20)

exit_button = tk.Button(bottom_logo_frame,text="EXIT",width=10,height=1,bg="red",fg="white",font=("Sitka Text Semibold", 15, "bold"),command=root.destroy,)
exit_button.pack(side="left", anchor="nw", padx=20, pady=20)
table_frame.configure(bg="white")

root.mainloop()