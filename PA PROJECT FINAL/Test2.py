import tkinter as tk
from tkinter import ttk
import pandas as pd
import scipy.stats as stats
from PIL import Image, ImageTk

def main():
   
    def perform_anova_test(variable, levels):
        try:
           
            df = pd.read_csv("obesity_data.csv")

            
            anova_result = stats.f_oneway(*[df[df[variable] == level]['BMI'] for level in levels])

            
            h0 = f"There is no significant difference in mean BMI among individuals with different levels of {variable}."
            h1 = f"There is a significant difference in mean BMI among individuals with different levels of {variable}."

            
            result_window = tk.Toplevel(root)
            result_window.title(f"ANOVA Test for {variable}")

           
            result_window.configure(bg="#68ED86")  

            
            frame = ttk.Frame(result_window, padding="20", style='My.TFrame')  

            
            frame.configure(style='My.TFrame')

            
            root.style = ttk.Style()
            root.style.configure('My.TFrame', background='#68ED86')

           
            frame.pack(expand=True, fill='both')

            
            hypotheses_label = ttk.Label(frame, text=f"\n\nNull Hypothesis (H0): {h0}\n"
                                                     f"Alternative Hypothesis (H1): {h1}",
                                         font=("Calisto MT", 14), background="#68ED86")
            hypotheses_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

           
            f_statistic_label = ttk.Label(frame, text=f"F-Statistic: {anova_result.statistic/100:.4f}",
                                           font=("Calisto MT", 14), background="#68ED86")
            f_statistic_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            p_value_label = ttk.Label(frame, text=f"P-Value: {anova_result.pvalue}",
                                       font=("Calisto MT", 14), background="#68ED86")
            p_value_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

            
            interpretation_label = ttk.Label(frame, text=f"Interpretation:\n"
                                                          f"The prevalence of BMI is {'different' if anova_result.pvalue < alpha else 'the same'} "
                                                          f"among individuals with different levels of {variable}.",
                                              font=("Calisto MT", 14), background="#68ED86")
            interpretation_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        except Exception as e:
            error_window = tk.Toplevel(root)
            error_window.title("Error")
            error_label = ttk.Label(error_window, text=f"An error occurred: {str(e)}")
            error_label.pack(padx=20, pady=20)

    def close_window(root):
        root.destroy()

   
    root = tk.Tk()
    root.title("Hypothesis Testing")
    root.attributes('-fullscreen', True)
    root.configure(bg='#FFFD6B')

    window_width = 1800
    window_height = 900

    
    gif_path = "Energy in Food Education Presentation in Collage Neat Style.gif"
    gif = Image.open(gif_path)

    
    num_frames = gif.n_frames

    
    resized_frames = []
    for frame_index in range(num_frames):
        gif.seek(frame_index)
        resized_frame = gif.resize((window_width, window_height))
        resized_frames.append(resized_frame)

    
    frame_index = 0
    frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
    gif_label = tk.Label(root, image=frame_image)
    gif_label.place(x=0, y=0, relwidth=1, relheight=1)  

    
    def update_gif():
        nonlocal frame_index
        frame_index = (frame_index + 1) % num_frames
        frame_image = ImageTk.PhotoImage(resized_frames[frame_index])
        gif_label.configure(image=frame_image)
        gif_label.image = frame_image
        root.after(200, update_gif)

    update_gif()  

    
    alpha = 0.05

    
    button1_color = "#26C454"  
    button2_color = "#1B8C3C"  
    button3_color = "#2DE646"
    button4_color = "#50B867"
    button5_color = "#A4FF90" 

    
    button_font = ("Britannic Bold", 16)

    button_sleep_duration = tk.Button(root, text="Sleep Duration", command=lambda: perform_anova_test('Sleep Duration', [4, 5, 8]),
                                       bg=button1_color, font=button_font,  height=2, width=25, relief="raised")
    button_sleep_duration.pack(pady=10)

    button_soft_drinks = tk.Button(root, text="Soft Drinks Consumption", command=lambda: perform_anova_test('Soft drinks', [0, 3, 5]),
                                    bg=button2_color, font=button_font,  height=2, width=25, relief="raised")
    button_soft_drinks.pack(pady=10)

    button_fatty_oily = tk.Button(root, text="Fatty/Oily Foods Consumption", command=lambda: perform_anova_test('fatty/oily foods', [2, 4, 5]),
                                   bg=button3_color, font=button_font, height=2, width=25, relief="raised")
    button_fatty_oily.pack(pady=10)

    button_sugary_foods = tk.Button(root, text="Sugary Foods Consumption", command=lambda: perform_anova_test('Sugary Foods', [2, 3, 4]),
                                     bg=button4_color, font=button_font,  height=2, width=25, relief="raised")
    button_sugary_foods.pack(pady=10)

    button_physical_activity = tk.Button(root, text="Physical Activity", command=lambda: perform_anova_test('PhysicalActivity', [2, 3, 4]),
                                          bg=button5_color, font=button_font,  height=2, width=25, relief="raised")
    button_physical_activity.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=lambda: close_window(root), font=("Arial", 22), bg='green', fg='white')
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    button_sleep_duration.place(x=150, y=350)
    button_soft_drinks.place(x=150, y=450)
    button_fatty_oily.place(x=150, y=550)
    button_sugary_foods.place(x=150, y=650)
    button_physical_activity.place(x=150, y=750)

    
    root.mainloop()

if __name__=="__main__":
    main()
