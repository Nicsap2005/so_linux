from searcher import search
from central_function import LinuxOS
from ASCII_tree_documentation import tembelek
import tkinter as tk

class util:
    def __init__(self):
        self.ubuntu = LinuxOS()
        self.output = search()
        
        self.show_changedir_enabled = False
        self.changedirButton = None
        
        self.show_getText_enabled = False
        self.getTextButton = None
        
        self.show_tree_enabled = False
        self.TreeButton = None
        
        self.Show_getTree_enabled = False
        self.getTreeButton = None
        
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())
        
    
    def util_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar):
        self.changedir_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar)
        self.Tree_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar)
    
    def clearing(self, performances_label, graph_label,text_box,tree_box,scrollbar):
        self.remove_getTextButton_btn(text_box)
        self.remove_getTreeButton_btn(text_box)
        text_box.grid_forget()
        tree_box.grid_forget()
        scrollbar.grid_forget()
        performances_label.grid_forget()
        graph_label.grid_forget()
        

    ############### change directory ###############
    
    def update_changedir(self,window,performances_label, graph_label,text_box,tree_box,scrollbar):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar)
        performances_label.config(text="")
        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.config(height=2,width=62,text=show_curpath,justify="left")
        graph_label.grid(row=1,column=1,columnspan=len(show_curpath),rowspan=10)

        text_box.grid(row=1, column=0, columnspan=5, rowspan=1)
        self.getText_btn(window,graph_label,text_box)

    def changedir_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar):
        if self.changedirButton is None:  # Check if the button exists
            self.changedirButton = tk.Button(window, width=15, height=1, text='change directory', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_changedir(window,performances_label, graph_label,text_box,tree_box,scrollbar))
            self.changedirButton.grid(row=0, column=1)
        else:
            self.changedirButton.grid(row=0, column=1)
    
    def getText_btn(self, window,graph_label,text_box):
        if self.getTextButton is None:  # Check if the button exists
            self.getTextButton = tk.Button(window, width=13, height=1, text='change directory', borderwidth=2,command=lambda:self.get_text(graph_label,text_box))
            self.getTextButton.grid(row=1, column=3)
        else:
            self.getTextButton.grid(row=1, column=3)
            
    def get_text(self,graph_label,text_box):
        content = text_box.get("1.0", "end-1c")
        print("Text box content:", content)
        self.ubuntu.change_directory(content)
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())

        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.config(text=show_curpath)
        graph_label.grid(columnspan=len(show_curpath))

    def remove_changedir_btn(self):
        if self.changedirButton is not None:
            self.changedirButton.grid_forget()  # Hide the button
            self.changedirButton = None  # Reset the button reference
            
    def remove_getTextButton_btn(self,text_box):
        text_box.grid_forget()
        if self.getTextButton is not None:
            self.getTextButton.grid_forget()  # Hide the button
            self.getTextButton = None  # Reset the button reference
        
    ############### ASCII TREE ###############
    
    def update_Tree(self,window,performances_label, graph_label,text_box,tree_box,scrollbar):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar)
        
        text_box.grid(row=1, column=0, columnspan=5, rowspan=1)
        self.getTree_btn(window,graph_label,text_box,tree_box)
        
        tree_box.grid(row=3, column=1, rowspan=25,columnspan=15, sticky="nsew")
        scrollbar.grid(row=3, column=20,rowspan=25,sticky="ns")
    
        tree_box.config(yscrollcommand=scrollbar.set)
        

    def Tree_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar):
        if self.TreeButton is None:  # Check if the button exists
            self.TreeButton = tk.Button(window, width=15, height=1, text='ASCII Tree', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_Tree(window,performances_label, graph_label,text_box,tree_box,scrollbar))
            self.TreeButton.grid(row=0, column=2)
        else:
            self.TreeButton.grid(row=0, column=2)
    
    def getTree_btn(self, window,graph_label,text_box,tree_box):
        if self.getTextButton is None:  # Check if the button exists
            self.getTreeButton = tk.Button(window, width=13, height=1, text='Get Tree', borderwidth=2,command=lambda:self.get_tree(text_box,tree_box))
            self.getTreeButton.grid(row=1, column=3)
        else:
            self.getTextButton.grid(row=1, column=3)
            
    def get_tree(self,text_box,tree_box):
        tree_box.delete("1.0", tk.END)
        content = text_box.get("1.0", "end-1c")
        print("Text box content:", content)
        tembelek(self.ubuntu,int(content), output_file_path='output.txt')
        tree = ''
        with open(f"{self.output.main()}/output.txt") as output:
            for i in output:
                tree += i
        tinggi = len(tree)
        if tinggi > 50:
            tinggi = len(tree)//20
        print(tree)
        tree_box.insert(tk.END, tree + "\n")
        
    def remove_Tree_btn(self):
        if self.TreeButton is not None:
            self.TreeButton.grid_forget()  # Hide the button
            self.TreeButton = None  # Reset the button reference
        
    def remove_getTreeButton_btn(self,text_box):
        text_box.grid_forget()
        if self.getTreeButton is not None:
            self.getTreeButton.grid_forget()  # Hide the button
            self.getTreeButton = None  # Reset the button reference
    
    ############### else button ###############
    def elsebtn(self, performances_label, graph_label,text_box,tree_box,scrollbar):
        self.show_available_directory_enabled = False
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar)
        self.remove_changedir_btn()
        self.remove_getTextButton_btn(text_box)
        self.remove_Tree_btn()
        self.remove_getTreeButton_btn(text_box)
    