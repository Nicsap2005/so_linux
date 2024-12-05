from performances import Performances_stat
from utility import util
import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.performance_instance = Performances_stat()
        self.utility_instance = util()
        # Initialize the Label and Text widgets as attributes
        self.performances_label = tk.Label(self.window, height=5, justify="left", text="Hello World")
        self.text_box = tk.Text(self.window, height=1, width=38)
                
        self.backup_box = tk.Text(self.window, height=1, width=38)        
        ###########################################################################################
        self.tree_box = tk.Text(self.window, height=20, width=70)#10,50
        self.scrollbar = ttk.Scrollbar(self.window,orient="vertical", command=self.tree_box.yview)
        ###########################################################################################
        
        self.graph_label = tk.Label(self.window, width=100, height=2)
        # Set up the main window layout
        self._setup_window()
    
    def _performances_btn_function(self,performance_instance, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self._show_label()
        self._else_btn_function(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        performance_instance.performances_btn(window, performances_label, graph_label)
        
    def _utility_btn_function(self,utility_instance, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self._show_label()
        self._else_btn_function(performances_label, graph_label, text_box,tree_box,scrollbar,backup_box)
        utility_instance.util_btn(window, performances_label, graph_label, text_box,tree_box,scrollbar,backup_box)
    
    def _else_btn_function(self,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.performance_instance.elsebtn(performances_label, graph_label)
        self.utility_instance.elsebtn(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
                
    def _setup_window(self):
        # Place a left label
        self.window.title("Project SO")
        self.window.geometry("900x600")
        
        left_label = tk.Label(self.window, width=10, text="Project SO", font=("Arial", 12))
        left_label.grid(row=0, column=0)
        
        # Initially display the Label and hide the Text widget
        self.performances_label.grid(row=1, column=1, columnspan=8, rowspan=2)
        
        # Create other widgets
        self.graph_label.grid(row=3, column=1, columnspan=100, rowspan=100)
        
        # Button to toggle to the Label view
        performances_btn = tk.Button(self.window, width=12, height=2, text="Performances", borderwidth=2, relief="solid", 
                                     command=lambda: self._performances_btn_function(self.performance_instance, self.window, self.performances_label, self.graph_label,self.text_box,self.tree_box,self.scrollbar,self.backup_box))
        performances_btn.grid(row=1, column=0)
        
        # Button to toggle to the Text view
        utility_btn = tk.Button(self.window, width=12, height=2, text="Utility", borderwidth=2, relief="solid", 
                                command=lambda:self._utility_btn_function(self.utility_instance, self.window, self.performances_label, self.graph_label,self.text_box,self.tree_box,self.scrollbar,self.backup_box))
        utility_btn.grid(row=2, column=0)
        
        # Another button
        else_btn = tk.Button(self.window, width=12, height=2, text="Else", borderwidth=2, relief="solid", command=lambda:self._else_btn_function(self.performances_label, self.graph_label,self.text_box,self.tree_box,self.scrollbar,self.backup_box))
        else_btn.grid(row=3, column=0)

        self.text_box.bind("<Return>", "break")
        self.window.mainloop()

    def _show_label(self):
        # Hide the Text widget and show the Label
        self.text_box.grid_forget()
        self.performances_label.grid(row=1, column=1, columnspan=8, rowspan=2)
    
    def _show_text_box(self):
        # Hide the Label and show the Text widget
        self.performances_label.grid_forget()
        self.text_box.grid(row=1, column=1, columnspan=8, rowspan=2)
    

if __name__ == "__main__":
    app = MainApp()
