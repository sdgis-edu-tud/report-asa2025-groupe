import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import geopandas as gpd
import os

class GeopackageColumnRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("Geopackage Column Renamer")
        self.root.geometry("800x600")
        
        self.gpkg_path = ""
        self.layer_name = ""
        self.gdf = None
        self.entry_widgets = {}
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # File selection
        ttk.Label(main_frame, text="Geopackage File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        file_frame = ttk.Frame(main_frame)
        file_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        file_frame.columnconfigure(0, weight=1)
        
        self.file_path_var = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.file_path_var, state="readonly").grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        ttk.Button(file_frame, text="Browse", command=self.browse_file).grid(row=0, column=1)
        
        # Layer selection
        ttk.Label(main_frame, text="Layer:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.layer_var = tk.StringVar()
        self.layer_combo = ttk.Combobox(main_frame, textvariable=self.layer_var, state="readonly")
        self.layer_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.layer_combo.bind('<<ComboboxSelected>>', self.load_columns)
        
        # Load button
        ttk.Button(main_frame, text="Load Columns", command=self.load_columns).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Scrollable frame for columns
        self.setup_scrollable_frame(main_frame)
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Preview Changes", command=self.preview_changes).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Apply Changes", command=self.apply_changes).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_entries).pack(side=tk.LEFT, padx=5)
    
    def setup_scrollable_frame(self, parent):
        # Create scrollable frame for column entries
        canvas_frame = ttk.Frame(parent)
        canvas_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure scrollable frame
        parent.rowconfigure(3, weight=1)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Geopackage File",
            filetypes=[("Geopackage files", "*.gpkg"), ("All files", "*.*")]
        )
        
        if file_path:
            self.gpkg_path = file_path
            self.file_path_var.set(file_path)
            self.load_layers()
    
    def load_layers(self):
        if not self.gpkg_path:
            return
        
        try:
            # Try to get list of layers in the geopackage
            try:
                layers_df = gpd.list_layers(self.gpkg_path)
                layers = layers_df['layer'].tolist()
            except Exception as list_error:
                # If list_layers fails, try to read the file directly (assumes single layer)
                print(f"list_layers failed: {list_error}")
                try:
                    # Try reading without specifying layer (works for single-layer files)
                    test_gdf = gpd.read_file(self.gpkg_path)
                    layers = ["default_layer"]  # Use a default name
                except Exception as read_error:
                    raise Exception(f"Could not read geopackage. list_layers error: {list_error}, read_file error: {read_error}")
            
            self.layer_combo['values'] = layers
            
            if layers:
                self.layer_combo.set(layers[0])
                # If only one layer, automatically load its columns
                if len(layers) == 1:
                    self.load_columns()
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load layers: {str(e)}")
    
    def load_columns(self, event=None):
        if not self.gpkg_path:
            return
        
        try:
            # Load the geopackage layer
            layer_to_load = self.layer_var.get()
            
            # If we're using the default_layer name, don't specify layer parameter
            if layer_to_load == "default_layer":
                self.gdf = gpd.read_file(self.gpkg_path)
                self.layer_name = "main"  # Use a simple name for single-layer files
            else:
                self.gdf = gpd.read_file(self.gpkg_path, layer=layer_to_load)
                self.layer_name = layer_to_load
            
            # Clear existing widgets
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            self.entry_widgets.clear()
            
            # Create header
            ttk.Label(self.scrollable_frame, text="Current Column Name", font=('TkDefaultFont', 10, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
            ttk.Label(self.scrollable_frame, text="New Column Name", font=('TkDefaultFont', 10, 'bold')).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Create entry widgets for each column
            for i, col_name in enumerate(self.gdf.columns, 1):
                # Current column name (read-only)
                ttk.Label(self.scrollable_frame, text=col_name).grid(row=i, column=0, padx=10, pady=2, sticky=tk.W)
                
                # New column name entry
                entry_var = tk.StringVar(value=col_name)
                entry = ttk.Entry(self.scrollable_frame, textvariable=entry_var, width=30)
                entry.grid(row=i, column=1, padx=10, pady=2, sticky=(tk.W, tk.E))
                
                self.entry_widgets[col_name] = entry_var
            
            # Configure column weights
            self.scrollable_frame.columnconfigure(1, weight=1)
            
            messagebox.showinfo("Success", f"Loaded {len(self.gdf.columns)} columns from the geopackage")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load columns: {str(e)}")
    
    def get_column_mapping(self):
        """Get mapping of old column names to new column names"""
        mapping = {}
        for old_name, entry_var in self.entry_widgets.items():
            new_name = entry_var.get().strip()
            if new_name and new_name != old_name:
                mapping[old_name] = new_name
        return mapping
    
    def preview_changes(self):
        mapping = self.get_column_mapping()
        
        if not mapping:
            messagebox.showinfo("Preview", "No column name changes detected.")
            return
        
        preview_text = "The following columns will be renamed:\n\n"
        for old_name, new_name in mapping.items():
            preview_text += f"'{old_name}' → '{new_name}'\n"
        
        messagebox.showinfo("Preview Changes", preview_text)
    
    def apply_changes(self):
        if self.gdf is None:
            messagebox.showwarning("Warning", "No data loaded. Please select a file and layer first.")
            return
        
        mapping = self.get_column_mapping()
        
        if not mapping:
            messagebox.showinfo("Info", "No column name changes detected.")
            return
        
        # Confirm changes
        preview_text = "Apply the following changes?\n\n"
        for old_name, new_name in mapping.items():
            preview_text += f"'{old_name}' → '{new_name}'\n"
        
        if not messagebox.askyesno("Confirm Changes", preview_text):
            return
        
        try:
            # Create a backup
            backup_path = self.gpkg_path + ".backup"
            if not os.path.exists(backup_path):
                import shutil
                shutil.copy2(self.gpkg_path, backup_path)
                print(f"Backup created: {backup_path}")
            
            # Apply the column renaming
            renamed_gdf = self.gdf.rename(columns=mapping)
            
            # Save back to the geopackage
            renamed_gdf.to_file(self.gpkg_path, layer=self.layer_name, driver="GPKG")
            
            messagebox.showinfo("Success", f"Successfully renamed {len(mapping)} columns!\n\nBackup saved as: {backup_path}")
            
            # Reload the data to show updated column names
            self.load_columns()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply changes: {str(e)}")
    
    def reset_entries(self):
        """Reset all entry fields to original column names"""
        for old_name, entry_var in self.entry_widgets.items():
            entry_var.set(old_name)

def main():
    root = tk.Tk()
    app = GeopackageColumnRenamer(root)
    root.mainloop()

if __name__ == "__main__":
    main()