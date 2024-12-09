import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer import FactorAnalyzer
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FactorAnalysisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Factor Analysis")  # Set the title of the main window

        # Set full screen
        self.root.attributes('-fullscreen', True)

        # Load data
        self.df = pd.read_csv('obesity_data.csv')
        #self.df['Gender'] = self.df['Gender'].map({'Male': 1, 'Female': 0})
        self.features = ['BMI',  'PhysicalActivity', 'Sleep Duration', 'Soft drinks', 'fatty/oily foods', 'Sugary Foods']
        self.X = self.df[self.features]

        # PCA
        self.pca = PCA()
        self.pca.fit(self.X)
        self.eigenvalues = self.pca.explained_variance_

     
        self.n_factors = sum(self.eigenvalues > 1)

        
        self.fa = FactorAnalyzer(n_factors=self.n_factors, rotation='varimax')
        self.fa.fit(self.X)
        self.loadings = pd.DataFrame(self.fa.loadings_, columns=[f'Factor{i+1}' for i in range(self.n_factors)], index=self.features)

        # Background Image
        self.bg_image = Image.open("factor.jpg")
        resized_bg_image = self.bg_image.resize((1600, 900), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        self.style = ttk.Style()
        self.style.configure('Custom.TButton', font=('Algerian', 18))

        self.scree_button = ttk.Button(self.root, text="Show Scree Plot", command=self.show_scree_plot, width=30, style='Custom.TButton')
        self.scree_button.place(x=800,y=200)

        self.loadings_button = ttk.Button(self.root, text="Show Factor Loadings", command=self.show_factor_loadings, width=30, style='Custom.TButton')
        self.loadings_button.place(x=800,y=300)

        self.interpretation_button = ttk.Button(self.root, text="Show Interpretation", command=self.show_interpretation, width=30, style='Custom.TButton')
        self.interpretation_button.place(x=800,y=400)

        back_button = tk.Button(self.root, text="Back", command=lambda: self.root.destroy(), font=("Arial", 22), bg='green', fg='white')
        back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    def show_scree_plot(self):
        # Plot Scree Plot
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(self.eigenvalues) + 1), self.eigenvalues, marker='o', linestyle='--')
        plt.title('Scree Plot')
        plt.xlabel('Factors')
        plt.ylabel('Eigenvalue')
        plt.axhline(y=1, color='r', linestyle='-')
        plt.show()

    def show_factor_loadings(self):
        # Display Factor Loadings
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.loadings, annot=True, cmap='viridis')
        plt.title('Factor Loadings')
        plt.show()

    def show_interpretation(self):
        # Interpretation
        interpretation_popup = tk.Toplevel(self.root)
        interpretation_popup.title("Interpretation")

        # Set background color for the outer window
        interpretation_popup.configure(bg='lightblue')

        # Create a text widget
        text_widget = tk.Text(interpretation_popup)
        text_widget.pack()

        # Set background color for the text widget
        text_widget.configure(bg='lightblue')

        # Insert interpretation text
        text_widget.insert(tk.END, "Interpretation:\n")
        text_widget.insert(tk.END, f"Number of factors selected using Kaiser criterion: {self.n_factors}\n\n")
        for i, column in enumerate(self.loadings.columns):
            text_widget.insert(tk.END, f"\n\n{column} Loadings:\n")
            text_widget.insert(tk.END, self.loadings[column].sort_values(ascending=False).to_string())

        # Run the GUI
        interpretation_popup.mainloop()

# Run the GUI
root = tk.Tk()
app = FactorAnalysisGUI(root)
root.mainloop()
