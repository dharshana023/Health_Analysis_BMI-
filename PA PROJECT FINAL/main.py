import tkinter as tk
from PIL import Image, ImageTk
import importlib
import subprocess

def Factor():
    subprocess.run(["python", "-m", "Factor"], check=True)
    
def cluster():
    subprocess.run(["python", "-m", "cluster"], check=True)
    
def predict_bmi():
    bmi_prediction = importlib.import_module("bmi_prediction")
    bmi_prediction.main()

def test_code():
    subprocess.run(["python", "-m", "MainTest"], check=True)
    
def exit_program():
    window.destroy


window = tk.Tk()
window.title("BMI")

window_width = 1600
window_height = 900
window.geometry(f"{window_width}x{window_height}")


gif_path = "C:/Users/annje/OneDrive/Desktop/PA PROJECT FINAL/five tips fo skin (1).gif"
gif = Image.open(gif_path)


num_frames = gif.n_frames


resized_frames = []
for frame_index in range(num_frames):
    gif.seek(frame_index)
    resized_frame = gif.resize((window_width, window_height))
    resized_frames.append(resized_frame)


frame_index = 0
frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
gif_label = tk.Label(window, image=frame_image)
gif_label.place(x=0, y=0, relwidth=1, relheight=1)  

def update_gif():
    global frame_index
    frame_index = (frame_index + 1) % num_frames
    frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
    gif_label.configure(image=frame_image)
    gif_label.image = frame_image
    window.after(200, update_gif)

update_gif()  


button1_color = "#26C454"  # Green
button2_color = "#1B8C3C"  # Light green
button3_color = "#115725"  # Dark green


button_font = ("Elephant", 25)


button1 = tk.Button(window, text="TESTING", command=test_code, bg=button1_color, font=button_font,fg="white", height=1, width=18, relief="raised")
button2 = tk.Button(window, text="PREDICT BMI", command=predict_bmi, bg=button2_color, font=button_font,fg="white", height=1, width=18, relief="raised")
button3 = tk.Button(window, text="FACTOR ANALYSIS", command=Factor, bg=button2_color, font=button_font,fg="white", height=1, width=18, relief="raised")
button4 = tk.Button(window, text="CLUSTERING", command=cluster, bg=button3_color, font=button_font,fg="white", height=1, width=18, relief="raised")





button1.place(relx=0.35, rely=0.3, anchor=tk.CENTER)
button2.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
button3.place(relx=0.35, rely=0.45, anchor=tk.CENTER)
button4.place(relx=0.65, rely=0.45, anchor=tk.CENTER)


window.mainloop()
