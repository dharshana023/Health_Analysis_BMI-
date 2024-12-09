import tkinter as tk
from tkinter import ttk
import pandas as pd
import scipy.stats as stats

# Function to perform ANOVA test and display result for Sleep Duration
def perform_sleep_duration_test():
    variable = 'Sleep Duration'
    levels = [4, 5, 8]
    perform_anova_test(variable, levels)

# Function to perform ANOVA test and display result for Soft Drinks Consumption
def perform_soft_drinks_test():
    variable = 'Soft drinks'
    levels = [0, 3, 5]
    perform_anova_test(variable, levels)

# Function to perform ANOVA test and display result for Fatty/Oily Foods Consumption
def perform_fatty_oily_test():
    variable = 'fatty/oily foods'
    levels = [2, 4, 5]
    perform_anova_test(variable, levels)

# Function to perform ANOVA test and display result for Sugary Foods Consumption
def perform_sugary_foods_test():
    variable = 'Sugary Foods'
    levels = [2, 3, 4]
    perform_anova_test(variable, levels)

# Function to perform ANOVA test and display result for Physical Activity
def perform_physical_activity_test():
    variable = 'PhysicalActivity'
    levels = [2, 3, 4]
    perform_anova_test(variable, levels)

# Function to perform ANOVA test and display result
def perform_anova_test(variable, levels):
    try:
        # Read data from CSV file into a DataFrame
        df = pd.read_csv("obesity_data.csv")

        # Perform ANOVA test
        anova_result = stats.f_oneway(*[df[df[variable] == level]['BMI'] for level in levels])

        # Null hypothesis (H0) and alternative hypothesis (H1)
        h0 = f"There is no significant difference in mean BMI among individuals with different levels of {variable}."
        h1 = f"There is a significant difference in mean BMI among individuals with different levels of {variable}."

        # Create a new window to display result
        result_window = tk.Toplevel(root)
        result_window.title(f"ANOVA Test for {variable}")
        screen_width = 800
        screen_height = 300

        # Set the window size to full screen
        result_window.geometry(f"{screen_width}x{screen_height}")

        # Frame to contain the result
        frame = ttk.Frame(result_window, padding="20",bg='#68ED86')
        frame.pack(expand=True, fill='both')

        # Label to display the null and alternative hypotheses
        hypotheses_label = ttk.Label(frame, text=f"\n\nNull Hypothesis (H0): {h0}\n"
                                                 f"Alternative Hypothesis (H1): {h1}",
                                     font=("Calisto MT", 14), background="#68ED86")
        hypotheses_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Label to display the ANOVA result
        f_statistic_label = ttk.Label(frame, text=f"F-Statistic: {anova_result.statistic:.4f}",
                                       font=("Calisto MT", 14), background="#68ED86")
        f_statistic_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        p_value_label = ttk.Label(frame, text=f"P-Value: {anova_result.pvalue:.4f}",
                                   font=("Calisto MT", 14), background="#68ED86")
        p_value_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Label to display the interpretation
        if anova_result.pvalue < alpha:
            interpretation = "There is a significant difference in mean BMI among individuals with different levels of the selected variable."
        else:
            interpretation = "There is no significant difference in mean BMI among individuals with different levels of the selected variable."

        interpretation_label = ttk.Label(frame, text=f"Interpretation:\n{interpretation}",
                                          font=("Calisto MT", 14), background="#68ED86")
        interpretation_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    except Exception as e:
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        error_label = ttk.Label(error_window, text=f"An error occurred: {str(e)}")
        error_label.pack(padx=20, pady=20)

# Create a GUI window
root = tk.Tk()
root.title("Hypothesis Testing")
root.attributes('-fullscreen', True)
root.configure(bg='#FFFD6B')

title_label = tk.Label(root, text="\nANOVA TEST", font=("Algerian", 45,), bg='#FFFD6B')
title_label.pack(pady=10)

# Set the significance level
alpha = 0.05

# Button for each hypothesis test
button1_color = "#26C454"  # Green
button2_color = "#1B8C3C"  # Light green
button3_color = "#2DE646"
button4_color = "#50B867"
button5_color = "#A4FF90" # Dark green

# Define font style for buttons
button_font = ("Britannic Bold", 16)

button_sleep_duration = tk.Button(root, text="Sleep Duration", command=perform_sleep_duration_test,
                                   bg=button1_color, font=button_font,  height=2, width=25, relief="raised")
button_sleep_duration.pack(pady=10)

button_soft_drinks = tk.Button(root, text="Soft Drinks Consumption", command=perform_soft_drinks_test,
                                bg=button2_color, font=button_font,  height=2, width=25, relief="raised")
button_soft_drinks.pack(pady=10)

button_fatty_oily = tk.Button(root, text="Fatty/Oily Foods Consumption", command=perform_fatty_oily_test,
                               bg=button3_color, font=button_font, height=2, width=25, relief="raised")
button_fatty_oily.pack(pady=10)

button_sugary_foods = tk.Button(root, text="Sugary Foods Consumption", command=perform_sugary_foods_test,
                                 bg=button4_color, font=button_font,  height=2, width=25, relief="raised")
button_sugary_foods.pack(pady=10)

button_physical_activity = tk.Button(root, text="Physical Activity", command=perform_physical_activity_test,
                                      bg=button5_color, font=button_font,  height=2, width=25, relief="raised")
button_physical_activity.pack(pady=10)

def close_window(root):
    root.destroy()

back_button = tk.Button(root, text="Back", command=lambda: close_window(root), font=("Arial", 22), bg='green', fg='white')
back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)

# Run the GUI
root.mainloop()
