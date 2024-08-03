import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from product_category import create_product

print("Starting the application...")

class ProductApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Product Categorization System")
        self.geometry("600x400")

        # Labels and entries
        self.sap_label = ctk.CTkLabel(self, text="SAP Code:")
        self.sap_label.pack(pady=(20, 5))

        self.sap_code_entry = ctk.CTkEntry(self)
        self.sap_code_entry.pack(pady=5)

        self.model_label = ctk.CTkLabel(self, text="Model Name:")
        self.model_label.pack(pady=5)

        self.model_name_entry = ctk.CTkEntry(self)
        self.model_name_entry.pack(pady=5)

        # Button to categorize product
        self.categorize_button = ctk.CTkButton(self, text="Categorize Product", command=self.categorize_product)
        self.categorize_button.pack(pady=10)

        # Text box for displaying features
        self.result_text = ctk.CTkTextbox(self, width=400, height=100)
        self.result_text.pack(pady=10)

        # Button to process a CSV or Excel file
        self.file_button = ctk.CTkButton(self, text="Process CSV/XLSX File", command=self.process_file)
        self.file_button.pack(pady=10)

        # Button to save the modified file
        self.save_button = ctk.CTkButton(self, text="Save Modified File", command=self.save_file)
        self.save_button.pack(pady=10)

        # Store the last processed dataframe
        self.processed_df = None

    def categorize_product(self):
        sap_code = self.sap_code_entry.get()
        model_name = self.model_name_entry.get()
        
        if not sap_code and not model_name:
            messagebox.showwarning("Input Error", "Please enter at least SAP Code or Model Name.")
            return
        
        product = create_product(sap_code, model_name)
        features = (
            f"Product categorized as: {product.class_name}\n"
            f"SAP Code: {product.sap_code}\n"
            f"Model Name: {product.model_name}\n"
            f"Body: {product.body}\n"
            f"Anno: {product.anno}\n"
            f"Extn: {product.extn}\n"
            f"Feature 1: {product.feature1}\n"
            f"Feature 2: {product.feature2}\n"
            f"Feature 3: {product.feature3}\n"
            f"Feature 4: {product.feature4}\n"
            f"Feature 5: {product.feature5}\n"
            f"Feature 6: {product.feature6}\n"
        )
        self.result_text.delete("1.0", ctk.END)
        self.result_text.insert(ctk.END, features)

    def process_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if not file_path:
            return

        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                messagebox.showerror("File Error", "Unsupported file type.")
                return

            # Check for required columns
            if 'SAP Code' not in df.columns or 'Model Name' not in df.columns:
                messagebox.showerror("File Error", "File must contain 'SAP Code' and 'Model Name' columns.")
                return

            # Process each row and add features
            df['Class Name'] = ''
            df['Body'] = ''
            df['Anno'] = ''
            df['Extn'] = ''
            df['Feature 1'] = ''
            df['Feature 2'] = ''
            df['Feature 3'] = ''
            df['Feature 4'] = ''
            df['Feature 5'] = ''
            df['Feature 6'] = ''

            for index, row in df.iterrows():
                product = create_product(row['SAP Code'], row['Model Name'])
                df.at[index, 'Class Name'] = product.class_name
                df.at[index, 'Body'] = product.body
                df.at[index, 'Anno'] = product.anno
                df.at[index, 'Extn'] = product.extn
                df.at[index, 'Feature 1'] = product.feature1
                df.at[index, 'Feature 2'] = product.feature2
                df.at[index, 'Feature 3'] = product.feature3
                df.at[index, 'Feature 4'] = product.feature4
                df.at[index, 'Feature 5'] = product.feature5
                df.at[index, 'Feature 6'] = product.feature6

            self.processed_df = df
            messagebox.showinfo("Process Complete", "File processed successfully. You can now save the modified file.")

        except Exception as e:
            messagebox.showerror("Processing Error", f"An error occurred: {e}")

    def save_file(self):
        if self.processed_df is None:
            messagebox.showwarning("Save Error", "No file to save. Please process a file first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if not file_path:
            return

        try:
            if file_path.endswith('.csv'):
                self.processed_df.to_csv(file_path, index=False)
            elif file_path.endswith('.xlsx'):
                self.processed_df.to_excel(file_path, index=False)
            else:
                messagebox.showerror("File Error", "Unsupported file type for saving.")
                return

            messagebox.showinfo("Save Complete", "File saved successfully.")

        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving: {e}")

def main():
    ctk.set_appearance_mode("light")  # Use "dark" for dark mode
    app = ProductApp()
    app.mainloop()

if __name__ == "__main__":
    main()
