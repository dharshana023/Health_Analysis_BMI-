import tkinter as tk
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def perform_z_test(result_label):
    
    df = pd.read_csv("obesity_data.csv")
    
    
    obese_df = df[df['ObesityCategory'] == 'Obese']
    
    
    male_obese_count = obese_df[obese_df['Gender'] == 'Male'].shape[0]
    female_obese_count = obese_df[obese_df['Gender'] == 'Female'].shape[0]
    
    
    total_male_count = df[df['Gender'] == 'Male'].shape[0]
    total_female_count = df[df['Gender'] == 'Female'].shape[0]
    
    
    z_stat, p_value = proportions_ztest([male_obese_count, female_obese_count], [total_male_count, total_female_count])
    
    
    h0 = "The prevalence of obesity (Obese category) is the same between males and females."
    h1 = "The prevalence of obesity (Obese category) is different between males and females."
    
    
    result_label.config(text=f"\n\n\nNull Hypothesis (H0): {h0}\n"
                              f"Alternative Hypothesis (H1): {h1}\n\n"
                              f"Z-Statistic: {abs(z_stat):.4f}\n"
                              f"P-Value: {p_value:.4f}\n\n"
                              f"Interpretation:\n"
                              f"The prevalence of obesity (Obese category) is {'different' if p_value < 0.05 else 'the same'} "
                              f"between males and females.",
                        font=("Calisto MT", 20),  
                        justify="center")  

def close_window(root):
    root.destroy()

def main():
    root = tk.Tk()
    root.title("Z-Test for Obesity Prevalence")
    root.configure(bg="#3F9152")

    result_label = tk.Label(root, text="", fg="white", bg="#3F9152")
    result_label.pack(pady=20)

    perform_z_test(result_label)

    back_button = tk.Button(root, text="Back", command=lambda: close_window(root), height=1, width=4, font=("Arial", 12), bg='green', fg='white')
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    root.mainloop()

if __name__ == "__main__":
    main()
