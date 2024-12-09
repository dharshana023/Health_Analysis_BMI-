import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

# Load data
data = pd.read_csv('obesity_data.csv')

# Feature selection
features = data[['BMI', 'PhysicalActivity', 'Sleep Duration', 'Soft drinks', 'fatty/oily foods', 'Sugary Foods']]

# Standardization
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_features)

# Centroids
centroids = kmeans.cluster_centers_
original_centroids = scaler.inverse_transform(centroids)
centroid_df = pd.DataFrame(original_centroids, columns=features.columns)
centroid_df['Cluster'] = range(3)

# PCA for visualization
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(scaled_features)
data['PCA1'] = reduced_features[:, 0]
data['PCA2'] = reduced_features[:, 1]

# Save the updated data with clusters to a new Excel file
data.to_excel('obesity_data_with_clusters.xlsx', index=False)

# Create GUI
class ObesityClusteringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Obesity Data Clustering")
        self.root.state('zoomed')  # Make window full size

        # Resize background image
        bg_image = Image.open("ai.jpg")
        resized_bg_image = bg_image.resize((1500, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        # Create frames
        self.top_frame = ttk.Frame(root)
        self.top_frame.pack(pady=10)
        self.bottom_frame = ttk.Frame(root)
        self.bottom_frame.pack(pady=10)

        # Create text widget for centroids and summary stats
        text_font = font.Font(family="Helvetica", size=16)
        self.text = tk.Text(self.root, width=75, height=20, bg='#97CBEF', fg='#103892', font=text_font)
        self.text.place(x=600, y=150)  # Place text widget at specified coordinates

        style = ttk.Style()
        style.configure('Custom.TButton', 
                        font=('Helvetica', 14, 'bold'), 
                        padding=(10, 10),
                        background='#4CAF50',
                        foreground='#103892')

        # Create buttons
        self.button_kmeans = ttk.Button(self.root, text="KMeans Clustering", command=self.show_results, style='Custom.TButton')
        self.button_kmeans.place(x=900, y=700)
        
        # Display results
        self.display_results()

    def show_results(self):
        # Plot PCA
        self.plot_pca_popup()

    def display_results(self):
        # Display centroids
        self.text.insert(tk.END, "Centroids of each cluster:\n")
        self.text.insert(tk.END, centroid_df.to_string(index=False))
        self.text.insert(tk.END, "\n\nNumber of instances in each cluster:\n")
        self.text.insert(tk.END, data['Cluster'].value_counts().to_string())

        # Display PCA loadings
        self.text.insert(tk.END, "\n\nMost significant variables for each principal component:\n")
        loadings = pd.DataFrame(pca.components_.T, columns=['PCA1', 'PCA2'], index=features.columns)
        self.text.insert(tk.END, loadings.to_string())
        self.text.update_idletasks()

    def plot_pca_popup(self):
        # Display PCA plot in a popup window
        popup = tk.Toplevel(self.root)
        popup.title('PCA Plot')
        fig, ax = plt.subplots(figsize=(10, 7))
        scatter = ax.scatter(data['PCA1'], data['PCA2'], c=data['Cluster'], cmap='viridis', alpha=0.5)
        ax.set_xlabel('PCA Component 1')
        ax.set_ylabel('PCA Component 2')
        ax.set_title('2D PCA of Clusters')
        plt.colorbar(scatter, label='Cluster')
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Run the app
root = tk.Tk()
app = ObesityClusteringApp(root)
root.mainloop()
