import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from product_category import create_product
class ProductApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Product Categorization System")
        self.geometry("1000x500")

        # Configure grid layout
        self.grid_columnconfigure((1,2), weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1), weight=1)

        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.entry_frame.grid_columnconfigure((0,1), weight=1)
        self.entry_frame.grid_rowconfigure((0,1), weight=1)
        
        # SAP Code and Model Name entries
        ctk.CTkLabel(self.entry_frame, text="SAP Code:").grid(row=0, column=0, sticky="nse", padx=10, pady=10)
        self.sap_code_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter SAP Code")
        self.sap_code_entry.grid(row=0, column=1, sticky="nsew", padx=10, pady=20)

        ctk.CTkLabel(self.entry_frame, text="Model Name:").grid(row=1, column=0, sticky="nse", padx=10, pady=10)
        self.model_name_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter Model Name")
        self.model_name_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=20)
        
        self.categorize_frame = ctk.CTkFrame(self)
        self.categorize_frame.grid(row=0, column=2, padx=10, pady=(10,5), sticky="nsew")
        self.categorize_frame.grid_columnconfigure((0,1), weight=1)
        self.categorize_frame.grid_rowconfigure(0, weight=1)

        # Button to categorize product
        self.categorize_button = ctk.CTkButton(self.categorize_frame, text="Categorize Product", command=self.categorize_product)
        self.categorize_button.grid(row=0, column=0, padx=(20,10), pady=20, sticky="nsew")
        
        self.clear_button = ctk.CTkButton(self.categorize_frame, text="Clear Inputs", command=self.clear_inputs)
        self.clear_button.grid(row=0, column=1, padx=(10,20), pady=20, sticky="nsew")

        # Scrolled Text Box for displaying features with a scrollbar
        self.result_text = ctk.CTkTextbox(self)
        self.result_text.grid(row=1, column=1, columnspan=2, padx=10, pady=(5,10), sticky="nsew")
        
        self.file_frame = ctk.CTkFrame(self, width=300)
        self.file_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=(10,10), sticky="nsew")
        self.file_frame.grid_columnconfigure(0, weight=1)
        self.file_frame.grid_rowconfigure((0,1,2), weight=1)
        
        self.logo_label = ctk.CTkLabel(self.file_frame, text="Hikvision", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Buttons for file operations
        self.file_button = ctk.CTkButton(self.file_frame, text="Process CSV/XLSX File", command=self.process_file)
        self.file_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.save_button = ctk.CTkButton(self.file_frame, text="Save Modified File", command=self.save_file)
        self.save_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        # Store the last processed dataframe
        self.processed_df = None
        
    def clear_inputs(self):
        # Clear the content of the SAP Code entry field
        self.sap_code_entry.delete(0, 'end')
        self.sap_code_entry.insert(0, "")

        # Clear the content of the Model Name entry field
        self.model_name_entry.delete(0, 'end')
        self.model_name_entry.insert(0, "")

        # Clear the ScrolledText widget
        self.result_text.delete("1.0", "end")


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
    ctk.set_appearance_mode("dark")
    app = ProductApp()
    app.mainloop()

if __name__ == "__main__":
    main()
