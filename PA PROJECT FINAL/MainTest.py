import tkinter as tk
from PIL import Image, ImageTk
import importlib
import subprocess

def run_t_test():
    test = importlib.import_module("test")
    test.main()

def run_anova():
    subprocess.run(["python", "-m", "Test2"], check=True)

def main():
    
    root = tk.Tk()
    root.title("Statistical Data")  

    
    root.configure(bg="#C9FF20")  

    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    
    gif_path = "White Aesthetic Collage Video (1).gif"
    gif = Image.open(gif_path)

    
    num_frames = gif.n_frames

    
    resized_frames = []
    for frame_index in range(num_frames):
        gif.seek(frame_index)
        resized_frame = gif.resize((screen_width, screen_height))
        resized_frames.append(resized_frame)

   
    frame_index = 0
    frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
    gif_label = tk.Label(root, image=frame_image)
    gif_label.place(x=0, y=0)

    
    def update_gif():
        nonlocal frame_index
        frame_index = (frame_index + 1) % num_frames
        frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
        gif_label.configure(image=frame_image)
        gif_label.image = frame_image
        root.after(200, update_gif)

    update_gif()  

    
    root.geometry(f"{screen_width}x{screen_height}")

   

    
    button1_color = "#2FD3E0"  
    button2_color = "#73FBFD"  

    
    button_font = ("Franklin Gothic Heavy", 19)

    
    button1 = tk.Button(root, text="Z-Test", command=run_t_test, bg=button1_color, font=button_font, height=2, width=20, relief="raised")
    button2 = tk.Button(root, text="ANOVA", command=run_anova, bg=button2_color, font=button_font, height=2, width=20, relief="raised")

    
    button1.place(x=130, y=250)
    button2.place(x=130, y=450)


    
    root.mainloop()

if __name__ == "__main__":
    main()

