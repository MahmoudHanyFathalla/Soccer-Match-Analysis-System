'''
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import pandas as pd

# Load the Excel file
file_path = 'C:\\Users\\hp\\Desktop\\excel kora\\AL_Ein_Match_event.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Filter necessary columns
df = df[['matchTimestamp', 'start_x', 'start_y', 'endLocation_x', 'endLocation_y']]

# Load the image
image_path = 'C:\\Users\\hp\\Desktop\\excel kora\\GT.jpg'
image = Image.open(image_path)
image = image.resize((1000, 600), Image.ANTIALIAS)

# Initialize the index for the line drawing
index = 0

def next_line():
    global index
    if index < len(df):
        row = df.iloc[index]
        timestamp.set(row['matchTimestamp'])
        start_x = row['start_x'] * 10
        start_y = row['start_y'] * 6
        end_x = row['endLocation_x'] * 10
        end_y = row['endLocation_y'] * 6
        # Draw the start point in blue
        canvas.create_oval(start_x-3, start_y-3, start_x+3, start_y+3, fill="blue", outline="blue")
        # Draw the end point in green
        canvas.create_oval(end_x-3, end_y-3, end_x+3, end_y+3, fill="green", outline="green")
        # Draw the line in red
        canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=2)
        index += 1

def back_line():
    global index
    if index > 0:
        index -= 1
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        for i in range(index):
            row = df.iloc[i]
            start_x = row['start_x'] * 10
            start_y = row['start_y'] * 6
            end_x = row['endLocation_x'] * 10
            end_y = row['endLocation_y'] * 6
            # Draw the start point in blue
            canvas.create_oval(start_x-3, start_y-3, start_x+3, start_y+3, fill="blue", outline="blue")
            # Draw the end point in green
            canvas.create_oval(end_x-3, end_y-3, end_x+3, end_y+3, fill="green", outline="green")
            # Draw the line in red
            canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=2)
        row = df.iloc[index-1]
        timestamp.set(row['matchTimestamp'])
# Create the main window
root = tk.Tk()
root.title("Match Visualization")

# Create a canvas for the image
canvas = Canvas(root, width=1000, height=600)
canvas.pack()
# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create buttons
frame = tk.Frame(root)
frame.pack()

next_button = tk.Button(frame, text="Next", command=next_line)
next_button.pack(side=tk.LEFT)

back_button = tk.Button(frame, text="Back", command=back_line)
back_button.pack(side=tk.LEFT)

# Create a label for the timestamp
timestamp = tk.StringVar()
timestamp_label = tk.Label(root, textvariable=timestamp)
timestamp_label.pack()

# Start the main loop
root.mainloop()
'''
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import pandas as pd

# Load the Excel file
file_path = 'C:\\Users\\hp\\Desktop\\KoraState\\excel kora\\AL_Ein_Match_event.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Filter necessary columns
df = df[['matchTimestamp', 'start_x', 'start_y', 'endLocation_x', 'endLocation_y']]

# Load the image
image_path = 'C:\\Users\\hp\\Desktop\\KoraState\\excel kora\\GT.jpg'
image = Image.open(image_path)
image = image.resize((1000, 600))

# Initialize the index for the line drawing
index = 0

# Variables to keep track of the current line and points
current_line = None
current_start_point = None
current_end_point = None

def update_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    if current_start_point:
        canvas.create_oval(current_start_point, fill="blue", outline="blue")
    if current_end_point:
        canvas.create_oval(current_end_point, fill="green", outline="green")
    if current_line:
        canvas.create_line(current_line, fill="red", width=2)

def next_line():
    global index, current_line, current_start_point, current_end_point
    if index < len(df):
        row = df.iloc[index]
        timestamp.set(row['matchTimestamp'])
        start_x = row['start_x'] * 10
        start_y = row['start_y'] * 6
        end_x = row['endLocation_x'] * 10
        end_y = row['endLocation_y'] * 6
        # Set the start and end points and line coordinates
        current_start_point = (start_x-3, start_y-3, start_x+3, start_y+3)
        current_end_point = (end_x-3, end_y-3, end_x+3, end_y+3)
        current_line = (start_x, start_y, end_x, end_y)
        update_canvas()
        index += 1

def back_line():
    global index, current_line, current_start_point, current_end_point
    if index > 0:
        index -= 1
        if index > 0:
            row = df.iloc[index-1]
            timestamp.set(row['matchTimestamp'])
            start_x = row['start_x'] * 10
            start_y = row['start_y'] * 6
            end_x = row['endLocation_x'] * 10
            end_y = row['endLocation_y'] * 6
            # Set the start and end points and line coordinates
            current_start_point = (start_x-3, start_y-3, start_x+3, start_y+3)
            current_end_point = (end_x-3, end_y-3, end_x+3, end_y+3)
            current_line = (start_x, start_y, end_x, end_y)
        else:
            timestamp.set('')
            current_start_point = None
            current_end_point = None
            current_line = None
        update_canvas()

# Create the main window
root = tk.Tk()
root.title("Match Visualization")

# Create a canvas for the image
canvas = Canvas(root, width=1000, height=600)
canvas.pack()

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create buttons
frame = tk.Frame(root)
frame.pack()

next_button = tk.Button(frame, text="Next", command=next_line)
next_button.pack(side=tk.LEFT)

back_button = tk.Button(frame, text="Back", command=back_line)
back_button.pack(side=tk.LEFT)

# Create a label for the timestamp
timestamp = tk.StringVar()
timestamp_label = tk.Label(root, textvariable=timestamp)
timestamp_label.pack()

# Start the main loop
root.mainloop()
