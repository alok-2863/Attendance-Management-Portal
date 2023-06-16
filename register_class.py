import tkinter as tk
import os
import csv
import time

root = tk.Tk()
root.config(bg="white")
root.overrideredirect(True)

def backk():
    root.destroy()
    os.system('python main_page.py')

def run_jj():
    if not txt.get() or not txt1.get():
        show_text('''Error!\nAny field should not be empty.''')
        return

    show_text("Class Registered Successfully.")

    folder_path = "StudentDetails"
    folder_name = f"{txt.get().upper()} {txt1.get().upper()}"
    full_path = os.path.join(folder_path, folder_name)

    try:
        os.makedirs(full_path)
        # print("Folder created successfully!")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")

    # print(txt.get())
    # print(txt1.get())

    with open('class.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not os.path.isfile('class.csv'):
            writer.writerow(['Class', 'Subject'])
        writer.writerow([txt.get().upper(), txt1.get().upper()])

def show_text(message):
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    insert_text_with_typing_animation(output_box, message)
    output_box.config(state=tk.DISABLED)

def insert_text_with_typing_animation(text_widget, text):
    text_widget.configure(state="normal")
    for char in text:
        text_widget.insert(tk.END, char)
        text_widget.see(tk.END)
        text_widget.update()
        time.sleep(0.05)
    text_widget.configure(state="disabled")

width, height = 700, 510
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = int((screen_width/2) - (width/2)), int((screen_height/2) - (height/2))
root.geometry(f"{width}x{height}+{x}+{y}")
x_cord, y_cord = 75, 20

logo_img = tk.PhotoImage(file="logo.png").subsample(1)
logo_label = tk.Label(root, image=logo_img, bd=0)
logo_label.pack(side="left", anchor="nw", padx=10, pady=10)

text_label = tk.Label(root, text="ATTENDANCE MANAGEMENT PORTAL", bg="white", fg="black", width=35, height=1, font=('Sitka Text Semibold', 18, 'bold underline'))
text_label.pack(pady=30, anchor="n")

# Add a line canvas
line_canvas = tk.Canvas(root, height=1, width=700, bg="black", highlightthickness=0)
line_canvas.create_line(0, 0, width, 0, fill="black")
line_canvas.place(x=75-x_cord, y=120-y_cord)

button_image = tk.PhotoImage(file="back.png")
button = tk.Button(root, image=button_image, bd=0, highlightbackground="white", bg="white", highlightcolor="white", command=backk)

button_image = tk.PhotoImage(file="back.png")
button = tk.Button(root, image=button_image, bd=0, highlightbackground="white",bg="white", highlightcolor="white", command=backk)
button.place(x=80-x_cord, y=125-y_cord)

message = tk.Label(root, text="Status:", width=5  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 18, ' bold ') ) 
message.place(x=120-x_cord, y=320-y_cord)

output_box = tk.Text(root, height=3, width=67, bg="#f0f4f9", fg="black", font=("Cascadia Code", 12), wrap="word", state="disabled")
output_box.place(x=120-x_cord, y=360-y_cord)

lbl = tk.Label(root, text="ENTER CLASS", width=21,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 15, ' bold ') ) 
lbl.place(x=120-x_cord, y=160-y_cord)

txt = tk.Entry(root,width=26,bg="blue" ,fg="white",font=('Times New Roman', 15, ' bold '))
txt.place(x=120-x_cord, y=198-y_cord)

lbl = tk.Label(root, text="ENTER SUBJECT", width=22,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 15, ' bold ') ) 
lbl.place(x=462-x_cord, y=160-y_cord)

txt1 = tk.Entry(root,width=26  ,bg="blue"  ,fg="white",font=('Times New Roman', 15, ' bold ')  )
txt1.place(x=462-x_cord, y=198-y_cord)

trainImg = tk.Button(root, text="REGISTER CLASS", command=run_jj,width=40 ,height=1  ,fg="black"  ,bg="#57a0e9" ,font=('Sitka Text Semibold', 18, ' bold ') )
trainImg.place(x=120-x_cord, y=250-y_cord)

exit_button = tk.Button(root, text="EXIT", width=10, height=1, bg="red", fg="white", font=('Sitka Text Semibold', 15, 'bold'), command=root.destroy)
exit_button.place(x=width-152, y=height-70)

# Run the main loop
root.mainloop()