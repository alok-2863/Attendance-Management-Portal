import tkinter as tk
import cv2,os,sys
import csv
import numpy as np
from datetime import datetime
import face_recognition

nm = int(sys.argv[1])
    
# nm=4

    
# Create the root window
root = tk.Tk()
root.title("Attendance Management Portal")

root.overrideredirect(True)


# Set the window size and position
width = 700
height = root.winfo_screenheight()-100 # Get the screen height
# Calculate the x- and y-coordinates to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

root.geometry(f"{width}x{height}+{x}+{y}")

x_cord = 75;
y_cord = 20;

def backk():  
    root.destroy()
    os.system('python main_page.py')  
    
    


message2 = tk.Text(root, height=screen_height//45, width=67, bg="#f0f4f9", fg="black", font=("Helvetica", 12), wrap="none", state="disabled")
message2.place(x=120-x_cord, y=300-y_cord)
message2.pack_propagate(False)



# Set the background color to white
root.configure(bg="white")

# Add logo to the top left corner
logo_img = tk.PhotoImage(file="logo.png")
logo_img = logo_img.subsample(1)

def run_jjcopy():
    root.destroy()
    os.system(f'python register_student.py {nm}') 

# Create a label widget for the logo and pack it in the top left corner
logo_label = tk.Label(root, image=logo_img, bd=0)
logo_label.pack(side="left", anchor="nw", padx=10, pady=10)




# Add text to the right of the logo
text_label= tk.Label(root, text="ATTENDANCE MANAGEMENT PORTAL" ,bg="white"  ,fg="black"  ,width=35  ,height=1,font=('Sitka Text Semibold', 18, 'bold underline')) 

text_label.pack(pady=30, anchor="n")

line_canvas = tk.Canvas(root, height=1, width = 700,bg="black", highlightthickness=0)
line_canvas.create_line(0, 0, width, 0, fill="black")
line_canvas.place(x=75-x_cord,y=120-y_cord)


def backend(message2):
    video_capture = cv2.VideoCapture(0)
    known_face_encodings = []
    known_face_names=[]
    final_ans=[]
    base_path = 'C:/Users/HP/OneDrive/Desktop/atten/at/images'
    path = '{}{}'.format(base_path, nm)
    for filename in os.listdir(path):
        
        image = face_recognition.load_image_file(path+'/'+filename)
        
        encoding = face_recognition.face_encodings(image)[0]
        
        known_face_encodings.append(encoding)
        
        known_face_names.append(os.path.splitext(filename)[0])
        
    # print(len(known_face_encodings))
    
    while True:   
        
        ret, frame = video_capture.read()
        
        rgb_frame = frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_frame)
        
        face_encodings = face_recognition.face_encodings(frame, face_locations) 
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(frame,(225,400),(620,450),(0,0,0),thickness=cv2.FILLED)
        cv2.putText(frame, 'Thapar Institute Of Engineering and Technolgy ', (245,420), font, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, 'Attendance Management System', (310, 440), font, 0.5, (0, 0, 255), 1)
        try:
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                      
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                
                name = "Unknown"  
                  
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                
                best_match_index = np.argmin(face_distances)
                
                if matches[best_match_index]:
                    
                    name = known_face_names[best_match_index]
                    
                    final_ans.append(name)
                    
                    split_str = name.split("_")
                    
                    first_name = split_str[1]
                    
                    name=first_name
                    

                if name == 'Unknown':
                    
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)
                    
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    
                    font = cv2.FONT_HERSHEY_DUPLEX
                    
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
                    
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    
                    font = cv2.FONT_HERSHEY_DUPLEX
                    
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)
                    
        except Exception as e:
            
            print("An error occurred: ", e)
            
            
        cv2.imshow('Video', frame)  
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break
        
    unique_names = set(final_ans)
    
    final_ans = list(unique_names)
    
    

# Insert text into the Text widget
    canvas = tk.Canvas(message2,bg="#f0f4f9")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(message2, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    
# Disable the Text widget again
    message2.configure(state="normal")
    table = tk.Frame(canvas, bg="#f0f4f9")
    table.pack()

    # Create labels for column headers
    tk.Label(table, text="Roll No.", bg="#f0f4f9",font=("Sitka Text Semibold", 15, "bold")).grid(row=0, column=0)
    tk.Label(table, text="Name", bg="#f0f4f9",font=("Sitka Text Semibold", 15, "bold"), anchor="w").grid(row=0, column=1)
    i=0
    for name1 in final_ans:
        i=i+1
        split_str = name1.split("_")

    # Extract the required information from the split string
        roll_id = split_str[0]
        first_name = split_str[1]
        last_name = split_str[2]

    # Print the extracted information
        # print("Roll ID:", roll_id)
        # print("First Name:", first_name)
        # print("Last Name:", last_name)
        tk.Label(table, text=roll_id, bg="#f0f4f9", font=("Helvetica", 12), anchor="w").grid(row=i, column=0, padx=40)
        tk.Label(table, text=first_name+" "+last_name, font=("Helvetica", 12), bg="#f0f4f9").grid(row=i, column=1, padx=40)

        with open('class.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for i in range(nm):
                a = next(csv_reader)
                text=f"{a[0]} {a[1]}"
        file.close()   
        
        file_path = 'StudentDetails/'+text+'/Attendance.csv'

        # get the current date and time as the column header
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

        # add a "P" to the column where row[0] = 102103582
        def mark_attendance():
            with open(file_path, 'r') as f:
                # read the csv file and store it as a list of lists
                csv_data = list(csv.reader(f))
                # get the index of the row where row[0] = 102103582
                index = [i for i, row in enumerate(csv_data) if row[0] == roll_id][0]
                # add the current date and time as the column header
                if dt_string not in csv_data[0]:
                    csv_data[0].append(dt_string)
                col_index = csv_data[0].index(dt_string)
                for _ in range(col_index-len(csv_data[index])+1):
                    csv_data[index].append("")
                # add a "P" to the cell where the row index matches and column index matches dt_string
                csv_data[index][col_index] = "P"
            with open(file_path, 'w', newline='') as f:
                # write the updated data back to the csv file
                writer = csv.writer(f)
                writer.writerows(csv_data)

        mark_attendance()




    message2.configure(state="disabled")
    canvas.create_window(((screen_height//45)/2, 0), window=table, anchor="nw")
    table.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    video_capture.release()
    cv2.destroyAllWindows()


def run():
    
    backend(message2)
    


with open('class.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate through the rows and retrieve data at the specified row and column
    for i, row in enumerate(csv_reader):
        if i == nm:
            data = row[0]
            data1=row[1]
            break
csv_file.close()
lbl10 = tk.Label(root, text="CLASS: "+data, width=350,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Times New Roman', 15, ' bold ') ) 
lbl10.place(x=180-x_cord, y=135-y_cord)
lbl10 = tk.Label(root, text="SUBJECT: "+data1, width=350,anchor="w"  ,height=1  ,fg="black"  ,bg="white" ,font=('Times New Roman', 15, ' bold ') ) 
lbl10.place(x=480-x_cord, y=135-y_cord)






trackImg = tk.Button(root, text="MARK ATTENDANCE", command=run, width=40 ,height=1  ,fg="black"  ,bg="#57a0e9" ,font=('Sitka Text Semibold', 18, ' bold ') )
trackImg.place(x=120-x_cord, y=175-y_cord)


lbl = tk.Label(root, text="Attendance list:", width=12  ,height=1  ,fg="black"  ,bg="white" ,font=('Sitka Text Semibold', 18, ' bold ') ) 
lbl.place(x=120-x_cord, y=250-y_cord)


# # Add a line below the "Attendance list:" line
# line2_canvas = tk.Canvas(root, height=1, bg="black", highlightthickness=0)
# line2_canvas.create_line(0, 0, width, 0, fill="black")
# line2_canvas.place(x=120-x_cord, y=150-y_cord)


button_image1 = tk.PhotoImage(file="back.png")
button1 = tk.Button(root, image=button_image1, bd=0, highlightbackground="white",bg="white", highlightcolor="white", command=backk)
button1.place(x=80-x_cord, y=125-y_cord)

button_image = tk.PhotoImage(file="button.png")

# Create a button with the image and white background
button = tk.Button(root, image=button_image, bd=0, highlightbackground="white",bg="white", highlightcolor="white",command=run_jjcopy)

# Place the button in the bottom right corner
button.place(x=width-70, y=height-70)

# Add an exit button in the bottom left corner
exit_button = tk.Button(root, text="EXIT", width=10, height=1, bg="red", fg="white", font=('Sitka Text Semibold', 15, 'bold'), command=root.destroy)
exit_button.place(x=20, y=height-70)
root.mainloop()













