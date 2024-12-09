import tkinter as tk
import importlib
from model_training import regression_model, coefficients, intercept, categories, y_test, y_pred, mae, r2

def predict_bmi(entries, result_label):
    user_input = [float(entries[factor].get()) for factor in entries]
    predicted_bmi = regression_model.predict([user_input])[0]
    category = next((category for range_, category in categories.items() if range_[0] < predicted_bmi <= range_[1]), None)
    result_label.config(text=f"Predicted BMI: {round(predicted_bmi, 2)}, Category: {category}")

def close_window(root):
    root.destroy()

def open_external_script():
    data_display = importlib.import_module("data_display")
    data_display.main()
    
def show_bmi_frame():
    root = tk.Tk()
    root.title("BMI Predictor")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root, bg='lightblue')
    main_frame.pack(fill='both', expand=True)

    title_label = tk.Label(main_frame, text="BMI Predictor", font=("OCR A Extended \n\n", 35, "bold"), bg='lightblue')
    title_label.pack(pady=10)

    regression_eq_label = tk.Label(main_frame, text=f"\n\nRegression Equation\nBMI = {intercept:.2f}  "
                                               f"{coefficients[0]:.2f} Sleep Duration  +"
                                               f"{coefficients[1]:.2f} Physical Activity  +"
                                               f"{coefficients[2]:.2f} Sugary Foods  +"
                                               f"{coefficients[3]:.2f} Fatty/Oily Foods  +"
                                               f"{coefficients[4]:.2f} Soft Drinks",
                                    font=("Ink Free", 19, "bold"), bg='lightblue')
    regression_eq_label.pack()

    open_script_button = tk.Button(main_frame, text="Predicted vs Actual", command=open_external_script,
                                   font=("Arial", 20), bg='#00A2E8', fg='white')
    open_script_button.pack(pady=10)

    mae_label = tk.Label(main_frame, text=f"Mean Absolute Error: {round(mae, 2)}", font=("OCR A Extended", 22), bg='lightblue')
    mae_label.pack()

    accuracy_label = tk.Label(main_frame, text=f"Accuracy of the Model: {round(r2*100, 2)}%\n", font=("OCR A Extended", 22), bg='lightblue')
    accuracy_label.pack()

    input_frame = tk.Frame(main_frame, bg='grey', bd=1, relief=tk.GROOVE)
    input_frame.pack(pady=10)

    factors = ['Sleep Duration', 'Physical Activity', 'Sugary Foods', 'Fatty/Oily Foods', 'Soft Drinks']
    entries = {}
    for factor in factors:
        row = tk.Frame(input_frame)
        row.pack(side=tk.TOP, padx=5, pady=5)
        label = tk.Label(row, width=20, text=factor, anchor='w', font=("Arial", 23), bg='white')
        label.pack(side=tk.LEFT)
        entry = tk.Entry(row, font=("Arial", 20))
        entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[factor] = entry

    predict_bmi_button = tk.Button(main_frame, text="Predict BMI", command=lambda: predict_bmi(entries, result_label),
                                   font=("Arial", 22), bg='#0A5ACF', fg='white')
    predict_bmi_button.pack(pady=10)

    result_frame = tk.Frame(main_frame, bg='blue', bd=1, relief=tk.GROOVE)
    result_frame.pack(pady=10)

    result_label = tk.Label(result_frame, font=("Arial", 22), bg='lightblue')
    result_label.pack(pady=10)

    back_button = tk.Button(main_frame, text="Back", command=lambda: close_window(root), font=("Arial", 22), bg='green', fg='white')
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    root.bind("<Escape>", lambda event: close_window(root))

    root.mainloop()

def main():
    show_bmi_frame()

if __name__ == "__main__":
    main()
