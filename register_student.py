import tkinter as tk
import os,sys
import csv,time
from tkinter import filedialog


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
    
# nm=7
nm = int(sys.argv[1])
# print(nm)
images_dir = "images" + str(nm)

# Create the root window
root = tk.Tk()
root.title("Feed Data")
root.overrideredirect(True)


selected_photo = None

from tkinter import filedialog

def browse_file():
    global selected_photo
    global selected_photo
    if (txt.get()=="" or txt1.get()=="" or txt2.get()==""):
            show_text("Error! Any field should not be empty.")
            return
    with open('class.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for i in range(nm):
                a = next(csv_reader)
                text=f"{a[0]} {a[1]}"
    file.close()
    file_path1= os.path.join('StudentDetails', text, 'Student List.csv')
    if os.path.isfile(file_path1):
        with open(file_path1, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # skip header
            for row in csv_reader:
                if row[0] == txt.get():
                    show_text('Student already exists.')
                    
                    return
                
    file_path = filedialog.askopenfilename()            
    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1]
        
    # Check if the extension is valid
    if file_ext.lower() not in (".jpg", ".jpeg", ".png", ".bmp"):
        show_text("Error! Invalid file type. Only JPEG,JPG, PNG, and BMP are allowed.")
        return            
    
    if file_path:
        selected_photo = file_path
        show_text("File selected.")
    




        
def register_data():
    
    if (selected_photo is None) and (txt.get()=="" or txt1.get()=="" or txt2.get()==""):
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        insert_text_with_typing_animation(output_box,  '''Error!
Any field should not be empty.''') 
        output_box.config(state=tk.DISABLED) 
    elif selected_photo is None:
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        insert_text_with_typing_animation(output_box, '''Error!
Please select a photo.''') 
        output_box.config(state=tk.DISABLED)
            
    else:
        # Create the "Images" folder if it doesn't exist
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        # Get the filename and extension
        file_name = os.path.basename(selected_photo)
        file_ext = os.path.splitext(file_name)[1]

        # Save the file to the "Images" folder
        save_name = (txt.get()).upper()+"_"+(txt1.get()).upper()+"_"+(txt2.get()).upper()+ file_ext
        save_path = os.path.join(images_dir, save_name)

        with open(save_path, "wb") as f:
            f.write(open(selected_photo, "rb").read())
            
            
        with open('class.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for i in range(nm):
                a = next(csv_reader)
                text=f"{a[0]} {a[1]}"
        file.close()
        file_path1= os.path.join('StudentDetails', text, 'Student List.csv')
        file_path2= os.path.join('StudentDetails', text, 'Attendance.csv')   
        
        if os.path.isfile(file_path1):
            # If file exists, append to the existing file
            with open(file_path1, 'a', newline='') as file:
                writer = csv.writer(file)
                # Write the new data to the file
                writer.writerow([(txt.get()).upper(), (txt1.get()).upper()+" "+(txt2.get()).upper()])  
        else:
            # If file does not exist, create a new file and add headers
            with open(file_path1, 'w', newline='') as file:
                writer = csv.writer(file)
                # Add the headers to the file
                writer.writerow(['Roll No', 'Name'])
                # Write the new data to the file
                writer.writerow([(txt.get()).upper(), (txt1.get()).upper()+" "+(txt2.get()).upper()])    
        file.close()
        if os.path.isfile(file_path2):
            # If file exists, append to the existing file
            with open(file_path2, 'a', newline='') as file:
                writer = csv.writer(file)
                # Write the new data to the file
                writer.writerow([(txt.get()).upper(), (txt1.get()).upper()+" "+(txt2.get()).upper()])  
        else:
            # If file does not exist, create a new file and add headers
            with open(file_path2, 'w', newline='') as file:
                writer = csv.writer(file)
                # Add the headers to the file
                writer.writerow(['Roll No', 'Name'])
                # Write the new data to the file
                writer.writerow([(txt.get()).upper(), (txt1.get()).upper()+" "+(txt2.get()).upper()])    
        file.close()         
           

        output_box.config(state=tk.NORMAL)  # set state to normal to enable editing
        output_box.delete("1.0", tk.END)  # delete the current content of the widget
        insert_text_with_typing_animation(output_box, "Student registered successfully.")  # insert new text
        output_box.config(state=tk.DISABLED)  # set state back to disabled to prevent editing
        
        


def run_jj():
    root.destroy()
    os.system(f'python attendance.py {nm}') 

         
# Set the window size and position
width = 700
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

root.geometry(f"{width}x{height}+{x}+{y}")

x_cord = 75;
y_cord = 20;
checker=0;


# Set the background color to white
root.configure(bg="white")

# Add logo to the top left corner
logo_img = tk.PhotoImage(file="logo.png")
logo_img = logo_img.subsample(1)

# Create a label widget for the logo and pack it in the top left corner
logo_label = tk.Label(root, image=logo_img, bd=0)
logo_label.pack(side="left", anchor="nw", padx=10, pady=10)



# Add text to the right of the logo
text_label= tk.Label(root, text="ATTENDANCE MANAGEMENT PORTAL" ,bg="white"  ,fg="black"  ,width=35  ,height=1,font=('Sitka Text Semibold', 18, 'bold underline')) 

text_label.pack(pady=30, anchor="n")

line_canvas = tk.Canvas(root, height=1, width = 700,bg="black", highlightthickness=0)
line_canvas.create_line(0, 0, width, 0, fill="black")
line_canvas.place(x=75-x_cord,y=120-y_cord)


button_image = tk.PhotoImage(file="back.png")

# Create a button with the image and white background
button = tk.Button(root, image=button_image, bd=0, highlightbackground="white",bg="white", highlightcolor="white", command=run_jj)


# Place the button in the bottom right corner
button.place(x=80-x_cord, y=125-y_cord)

message = tk.Label(root, text="Status:", width=5  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 18, ' bold ') ) 
message.place(x=120-x_cord, y=410-y_cord)





output_box = tk.Text(root, height=3, width=67, bg="#f0f4f9", fg="black", font=("Cascadia Code", 12), wrap="word", state="disabled")
output_box.place(x=120-x_cord, y=450-y_cord)




lbl = tk.Label(root, text="ENTER YOUR ROLL NO.", width=21,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 15, ' bold ') ) 
lbl.place(x=120-x_cord, y=160-y_cord)


txt = tk.Entry(root,width=26,bg="blue" ,fg="white",font=('Times New Roman', 15, ' bold '))
txt.place(x=120-x_cord, y=198-y_cord)




lbl = tk.Label(root, text="ENTER YOUR FIRST NAME", width=22,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 15, ' bold ') ) 
lbl.place(x=462-x_cord, y=160-y_cord)

def validate_input(text):
    if text.isalpha() or text == "" or text == " ":
        return True
    else:
        return False


txt1 = tk.Entry(root, width=26, bg="blue", fg="white", font=('Times New Roman', 15, ' bold '), validate="key")
txt1.configure(validatecommand=(txt1.register(validate_input), '%S'))
txt1.place(x=462-x_cord, y=198-y_cord)


lbl2 = tk.Label(root, text="ENTER YOUR LAST NAME", width=22 ,anchor="w" ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 15, ' bold ') ) 
lbl2.place(x=120-x_cord, y=250-y_cord)

txt2 = tk.Entry(root, width=26, bg="blue", fg="white", font=('Times New Roman', 15, ' bold '), validate="key")
txt2.configure(validatecommand=(txt2.register(validate_input), '%S'))
txt2.place(x=120-x_cord, y=288-y_cord)

button = tk.Button(root, text="UPLOAD YOUR PICTURE", command=browse_file, width=21, height=1, fg="black", bg="#f0f3f9", font=('Sitka Text Semibold', 15, 'bold'))
button.place(x=462-x_cord, y=262-y_cord)


trainImg = tk.Button(root, text="REGISTER STUDENT", command=register_data,width=40 ,height=1  ,fg="black"  ,bg="#57a0e9" ,font=('Sitka Text Semibold', 18, ' bold ') )
trainImg.place(x=120-x_cord, y=340-y_cord)

exit_button = tk.Button(root, text="EXIT", width=10, height=1, bg="red", fg="white", font=('Sitka Text Semibold', 15, 'bold'), command=root.destroy)
exit_button.place(x=width-152, y=height-70)

# Run the main loop
root.mainloop()
