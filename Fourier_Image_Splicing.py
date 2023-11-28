# Import necessary libraries
import tkinter as tk
from PIL import ImageTk, Image
import functions as splice
import time

# Global variables for image size and index
global image_size_x
image_size_x = 860
global image_size_y
image_size_y = 672
global i
i = 0

# Function to render the near-field image
def render_image():
    # Get image and display
    global image_1
    input_text = e.get()
    image_1 = ImageTk.PhotoImage(Image.open("images/{}".format(input_text)).resize((350, 280)))
    show_image_1 = tk.Label(image=image_1)
    show_image_1.grid(row=3, column=0)

# Function to render the far-field image
def render_image_2():
    # Get image and display
    global image_2
    input_text = e2.get()
    image_2 = ImageTk.PhotoImage(Image.open("images/{}".format(input_text)).resize((350, 280)))
    show_image_2 = tk.Label(image=image_2)
    show_image_2.grid(row=7, column=0)

# Function to render the merged image
def render_merged_image():
    # Get image and display
    global image_3
    global label_wait
    global show_image_3

    # Call the splice function to merge images
    splice.Image_mesh(e.get(), e2.get(), float(e_merged.get()))
    
    # Display the merged image
    image_3 = ImageTk.PhotoImage(Image.open("images/spliced.png").resize((image_size_x, image_size_y)))
    show_image_3 = tk.Label(image=image_3)
    show_image_3.grid(row=3, column=1, rowspan=5, columnspan=2)

# Function to delete the displayed image
def delete():
    print("delete")
    show_image_3.grid_forget()
    return

# Function to decrease the displayed image size
def decrease_image(x, y):
    global show_image_4
    global image_4
    print("the")

    # Decrease image size by 5%
    image_size_x_ = int(0.95 * x)
    image_size_y_ = int(0.95 * y)

    # Resize and display the image
    image_4 = ImageTk.PhotoImage(Image.open("images/spliced.png").resize((image_size_x_, image_size_y_)))
    print(type(image_4))
    show_image_4 = tk.Label(image=image_4)
    show_image_4.grid(row=3, column=1, rowspan=5, columnspan=2)
    
    # Update global variables
    global show_image_3
    global image_3
    image_3 = image_4
    show_image_3 = show_image_4
    global image_size_x
    global image_size_y
    image_size_x = image_size_x_
    image_size_y = image_size_y_

# Function to increase the displayed image size
def increase_image(x, y):
    global show_image_4
    global image_4
    print("the")

    # Increase image size by 5%
    image_size_x_ = int(1.05 * x)
    image_size_y_ = int(1.05 * y)

    # Resize and display the image
    image_4 = ImageTk.PhotoImage(Image.open("images/spliced.png").resize((image_size_x_, image_size_y_)))
    print(type(image_4))
    show_image_4 = tk.Label(image=image_4)
    show_image_4.grid(row=3, column=1, rowspan=5, columnspan=2)
    
    # Update global variables
    global show_image_3
    global image_3
    image_3 = image_4
    show_image_3 = show_image_4
    global image_size_x
    global image_size_y
    image_size_x = image_size_x_
    image_size_y = image_size_y_

# Function to create a label widget
def widget_label(row=0, column=0, rowspan=1, columnspan=1, text="", width=10, height=1,
                 background_colour="black", forground_colour="white", padx=0, pady=0):
    label = tk.Label(root, text=text, width=width, height=height, padx=padx, pady=pady)
    label.config(bg=background_colour, fg=forground_colour)
    label.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    return label

# Function to create entry widgets
def widget_insert(row=0, column=0, rowspan=1, columnspan=1, text="", width=10, height=1,
                  background_colour="black", forground_colour="white", padx=0, pady=0, borderwidth=5):
    e = tk.Entry(root, width=width, borderwidth=borderwidth)
    e.insert(0, text)
    e.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    return e

# Function to create button widgets
def widget_button(row=0, column=0, rowspan=1, columnspan=1, text="", width=10, height=1,
                  background_colour="#f0f0f0", forground_colour="white", padx=0, pady=0, command=None):
    button = tk.Button(root, text=text, width=width, height=height, padx=padx,pady=pady, command=command)
    button.config(bg=background_colour, fg=forground_colour)
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    return button

# Create the main Tkinter window
root = tk.Tk()

# Define label widgets
label_1 = widget_label(row=0, column=0, text="Near Field Image", width=50, background_colour="#601F15", forground_colour="white")
label_blank = widget_label(row=3, column=0, width=48, background_colour="black", forground_colour="white", padx=10, pady=150)
label_2 = widget_label(row=4, column=0, text="Far Field Image", width=50, background_colour="#601F15", forground_colour="white")
label_blank_2 = widget_label(row=7, column=0, width=48, background_colour="black", forground_colour="white", padx=10, pady=150)
label_blank = widget_label(row=3, column=1, rowspan=5, columnspan=2, width=124, height=48, background_colour="black", forground_colour="white")
label_merged = widget_label(row=0, column=1, text="Merged Image -  full far field = 0,  full near field = 0.5", background_colour="#601F15", forground_colour="white", padx=350)

# Define button widgets
button_1 = widget_button(row=2, column=0, text="render image", command=render_image, forground_colour="#601F15")
button_2 = widget_button(row=6, column=0, text="render image", command=render_image_2, forground_colour="#601F15")
button_merged = widget_button(row=2, column=1, text="render image", command=render_merged_image, forground_colour="#601F15")

button_decrease_size = widget_button(row=0, column=2, text="decrease size -", command=lambda: [delete(), decrease_image(image_size_x, image_size_y)], forground_colour="#601F15", padx=40)

button_increase_size = widget_button(row=1, column=2, text="decrease size +", command=lambda: [delete(), increase_image(image_size_x, image_size_y)], forground_colour="#601F15", padx=40)

button_delete = widget_button(row=2, column=2, text="Delete Image", command=lambda: delete(), forground_colour="#601F15", padx=40)

# Define text inputs
e = widget_insert(row=1, column=0, text="Enter the filename of the near field image   ", width=50, borderwidth=5, background_colour="#601F15", forground_colour="white")

e2 = widget_insert(row=5, column=0, text="Enter the filename of the far field image   ", width=50, borderwidth=5, background_colour="#601F15", forground_colour="black")

e_merged = widget_insert(row=1, column=1, text="Enter near field - far field parameter between 0 and 0.5", width=50, borderwidth=5, background_colour="#601F15", forground_colour="black")

# Start the Tkinter event loop
root.mainloop()
