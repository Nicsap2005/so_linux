from searcher import search
from central_function import LinuxOS,PenghapusSementara,Search_and_Sort_Files,BackUp_Files
from ASCII_tree_documentation import tembelek
import tkinter as tk

class util:
    def __init__(self):
        self.ubuntu = LinuxOS()
        self.output = search()
        
        ##############################################
        self.show_changedir_enabled = False
        self.changedirButton = None
        
        self.show_getText_enabled = False
        self.getTextButton = None
        ##############################################
        self.show_tree_enabled = False
        self.TreeButton = None
        
        self.Show_getTree_enabled = False
        self.getTreeButton = None
        ##############################################
        self.Show_delTemp_enabled = False
        self.delTempButton = None
        
        self.Show_clearTemp_enabled = False
        self.clearTempButton = None
        ##############################################
        self.Show_backup_enabled = False
        self.clearbackupButton = None
        ##############################################
        self.Show_sort_enabled = False
        self.clearsortButton = None
        
        self.Show_getsort_enabled = False
        self.getsortButton = None
        self.counter = 0
        self.step1 =  None
        self.step2 =  None
        self.step3 =  None
        self.step4 =  None
        self.step5 =  None
        self.step6 = None
        self.success = None
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())
        
    
    def util_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.changedir_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        self.Tree_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        self.delTemp_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        self.backup_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        self.sort_btn(window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        
    def clearing(self, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.remove_getTextButton_btn(text_box)
        self.remove_getTreeButton_btn(text_box)
        self.remove_clearTemp_btn()
        self.remove_getsortButton_btn()
        
        text_box.delete("1.0", tk.END)
        backup_box.grid_forget()
        text_box.grid_forget()
        tree_box.grid_forget()
        scrollbar.grid_forget()
        performances_label.grid_forget()
        graph_label.grid_forget()
        

    ############### change directory ###############
    
    def update_changedir(self,window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        performances_label.config(text="")
        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.grid(row=1,column=1,columnspan=4,rowspan=10)
        graph_label.config(height=2,width=62,text=show_curpath,justify="left")

        text_box.config(width=38)
        text_box.grid(row=1, column=1,columnspan=2, rowspan=1)
        
        self.getText_btn(window,graph_label,text_box)

    def changedir_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        if self.changedirButton is None:  # Check if the button exists
            self.changedirButton = tk.Button(window, width=15, height=1, text='change directory', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_changedir(window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box))
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
        text_box.delete("1.0", tk.END)

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
    
    def update_Tree(self,window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        
        text_box.config(width=38)
        text_box.grid(row=1, column=1,columnspan=2, rowspan=1)
        self.getTree_btn(window,text_box,tree_box)
        
        tree_box.grid(row=3, column=1, rowspan=25,columnspan=15, sticky="nsew")
        scrollbar.grid(row=3, column=20,rowspan=25,sticky="ns")
    
        tree_box.config(yscrollcommand=scrollbar.set)
        

    def Tree_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        if self.TreeButton is None:  # Check if the button exists
            self.TreeButton = tk.Button(window, width=15, height=1, text='ASCII Tree', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_Tree(window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box))
            self.TreeButton.grid(row=0, column=2)
        else:
            self.TreeButton.grid(row=0, column=2)
    
    def getTree_btn(self, window,text_box,tree_box):
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
        text_box.delete("1.0", tk.END)
        
    def remove_Tree_btn(self):
        if self.TreeButton is not None:
            self.TreeButton.grid_forget()  # Hide the button
            self.TreeButton = None  # Reset the button reference
        
    def remove_getTreeButton_btn(self,text_box):
        text_box.grid_forget()
        if self.getTreeButton is not None:
            self.getTreeButton.grid_forget()  # Hide the button
            self.getTreeButton = None  # Reset the button reference
    ###########################################
    def update_delTemp(self,window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        performances_label.grid(row=1,column=1,rowspan=2,columnspan=3)
        performances_label.config(text='pressed the clear button to clear tmp directory!',width=38,height=5)
        self.clearTemp_btn(window,performances_label)
        
    def delTemp_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        if self.delTempButton is None:  # Check if the button exists
            self.delTempButton = tk.Button(window, width=15, height=1, text='clear temp', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_delTemp(window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box))
            self.delTempButton.grid(row=0, column=3)
        else:
            self.delTempButton.grid(row=0, column=3)
    
    def clearTemp_btn(self, window,performances_label):
        if self.clearTempButton is None:  # Check if the button exists
            self.clearTempButton = tk.Button(window, width=15, height=1, text='clear', borderwidth=2, relief='ridge',command=lambda:self.clear_function(performances_label))
            self.clearTempButton.grid(row=3, column=2)
        else:
            self.clearTempButton.grid(row=2, column=2)
    
    def clear_function(self,performances_label):
        clearing = PenghapusSementara()
        file = clearing.hapus_file_di_sementara()
    
        performances_label.config(text=f"tmp directory has been cleared!\n\nJumlah file yang dihapus: {file[0]}\nJumlah folder yang dihapus: {file[1]}")
            
    def remove_delTemp_btn(self):
        if self.delTempButton is not None:
            self.delTempButton.grid_forget()  # Hide the button
            self.delTempButton = None  # Reset the button reference
            
    def remove_clearTemp_btn(self):
        if self.clearTempButton is not None:
            self.clearTempButton.grid_forget()  # Hide the button
            self.clearTempButton = None  # Reset the button reference
    
    ################################### backup ###################################
    def update_backup(self,window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        performances_label.config(width=15,text="direktori asal:",justify="right")
        performances_label.grid(row = 1, column=1, columnspan=1,rowspan=2)
        graph_label.config(text="direktori tujuan: ",width=13,height = 1,justify='left')
        graph_label.grid(row = 1, column=1, columnspan=1,rowspan=3)
        # show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        # graph_label.config(height=2,width=62,text=show_curpath,justify="left")
        # graph_label.grid(row=1,column=1,columnspan=len(show_curpath),rowspan=10)
        text_box.config(width=40)
        text_box.grid(row=1, column=1,columnspan=4, rowspan=2)
        
        backup_box.config(width=40)
        backup_box.grid(row=1, column=1,columnspan=4, rowspan=3)
        
        self.getbackup_btn(window,text_box,backup_box)

    def backup_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        if self.clearbackupButton is None:  # Check if the button exists
            self.clearbackupButton = tk.Button(window, width=15, height=1, text='backup directory', borderwidth=2, relief='ridge',
                                        command=lambda:self.update_backup(window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box))
            self.clearbackupButton.grid(row=0, column=4)
        else:
            self.clearbackupButton.grid(row=0, column=4)
    
    def getbackup_btn(self, window,text_box,backup_box):
        if self.getTextButton is None:  # Check if the button exists
            self.getTextButton = tk.Button(window, width=10, height=1, text='backup', borderwidth=2,command=lambda:self.get_backup(window,text_box,backup_box))
            self.getTextButton.grid(row=3, column=2,rowspan=2)
        else:
            self.getTextButton.grid(row=3, column=2,rowspan=2)
            
    def get_backup(self,window,text_box,backup_box):
        backup = BackUp_Files()
        source = text_box.get("1.0", "end-1c")
        dest = backup_box.get("1.0", "end-1c")
        result = backup.backup_data(source,dest)
        # Function to show the confirmation popup
        def show_confirmation(result):
            # Popup window
            popup = tk.Toplevel(window)
            popup.title("Confirmation")
            popup.geometry(f"500x100")

            # Confirmation message
            label = tk.Label(popup, text=f"{result}", font=("Arial", 12))
            label.pack(pady=20)

            # Action for Yes button
            def ok():
                popup.destroy()

            btn_no = tk.Button(popup, text="ok", command=ok, width=50)
            btn_no.pack(side=tk.RIGHT, padx=(10, 50))

        # Call the confirmation popup
        show_confirmation(result)

        text_box.delete("1.0", tk.END)
        backup_box.delete("1.0", tk.END)

    def remove_backup_btn(self):
        if self.clearbackupButton is not None:
            self.clearbackupButton.grid_forget()  # Hide the button
            self.clearbackupButton = None  # Reset the button reference
            
    # def remove_getTextButton_btn(self,text_box):
    #     text_box.grid_forget()
    #     if self.getTextButton is not None:
    #         self.getTextButton.grid_forget()  # Hide the button
    #         self.getTextButton = None  # Reset the button reference
    
    ################################### sort ###################################
    def update_sort(self,window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        performances_label.config(text="Masukkan lokasi directory yang ingin diakses :",height=1,width=40,justify='left')
        performances_label.grid(column=0,row=1,columnspan=4)
        text_box.config(width=25)
        text_box.grid(column=3,row=1,columnspan=2)
        self.getsort_btn(window,graph_label,text_box)

    def sort_btn(self, window, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        if self.clearsortButton is None:  # Check if the button exists
            self.clearsortButton = tk.Button(window, width=15, height=1, text='sort', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_sort(window,performances_label, graph_label,text_box,tree_box,scrollbar,backup_box))
            self.clearsortButton.grid(row=0, column=5)
        else:
            self.clearsortButton.grid(row=0, column=5)
    
    def getsort_btn(self, window,graph_label,text_box):
        if self.getsortButton is None:  # Check if the button exists
            self.getsortButton = tk.Button(window, width=10, height=1, text='sort', borderwidth=2,command=lambda:self.get_sort(window,text_box))
            self.getsortButton.grid(row=1, column=4,columnspan=3)
        else:
            self.getsortButton.grid(row=1, column=4,columnspan=3)
            
    def get_sort(self,window,text_box):
        content = text_box.get("1.0", "end-1c")
        self.step1 = content
        self.counter = 2
        self.step2 =  None
        self.step3 =  None
        self.step4 =  None
        self.step5 =  None
        self.success = None
        sorting = Search_and_Sort_Files()
        def show_confirmation(result):
            # Popup window
            popup = tk.Toplevel(window)
            popup.title("Confirmation")
            popup.geometry(f"550x150")

            # Confirmation message
            label = tk.Label(popup, text=f"Masukkan nama file yang ingin dicari\n(kosongkan jika Anda ingin mencari semua file di folder tersebut) :", font=("Arial", 12))
            label.grid(row=0,column=0)
            # Action for Yes button
            # def step2():
            #     pass
            def go():
                content = text.get("1.0", "end-1c")
                if self.counter == 2:
                    content = text.get("1.0", "end-1c")
                    self.step2 = content
                    label.config(text="Masukkan jenis file\n(misalnya .txt, .pdf, .py\natau kosongkan jika Anda ingin mencari semua file):")
                if self.counter == 3:
                    content = text.get("1.0", "end-1c")
                    self.step3 = content
                    label.config(text="Urutkan file berdasarkan ('nama', 'ukuran', 'waktu edit'):")
                if self.counter == 4:
                    content = text.get("1.0", "end-1c")
                    self.step4 = content
                    label.config(text="Urutkan dari yang terbesar ke terkecil? (y/n):")
                if self.counter == 5:
                    content = text.get("1.0", "end-1c")
                    self.step5 = content
                    result = sorting.run(self.step1,self.step2,self.step3,self.step4,self.step5)
                    text.grid_forget()
                    if result == True:
                        self.success = "pengurutan berhasil!\ntekan go untuk kembali"
                    elif result == False:
                        self.success = "pengurutan gagal!\ntekan go untuk kembali"
                    label.config(text=self.success)
                if self.counter == 6:
                    popup.destroy()
    
                    
                    
                    
                self.counter += 1
                print(self.counter)
                print(self.step1,self.step2,self.step3,self.step4,self.step5,self.step6)
                
            text = tk.Text(popup, height=1, width=38) 
            text.grid(row=1,column=0)
            btn_no = tk.Button(popup, text="go", command=lambda:go(), width=10)
            btn_no.grid(row=2,column=0)
            

        # Call the confirmation popup
        if len(content) > 0:
            show_confirmation(content)
        text_box.delete("1.0", tk.END)

    def remove_sort_btn(self):
        if self.clearsortButton is not None:
            self.clearsortButton.grid_forget()  # Hide the button
            self.clearsortButton = None  # Reset the button reference
            
    def remove_getsortButton_btn(self):
        if self.getsortButton is not None:
            self.getsortButton.grid_forget()  # Hide the button
            self.getsortButton = None  # Reset the button reference
        
    ############### else button ###############
    def elsebtn(self, performances_label, graph_label,text_box,tree_box,scrollbar,backup_box):
        self.show_available_directory_enabled = False
        self.clearing(performances_label, graph_label,text_box,tree_box,scrollbar,backup_box)
        self.remove_changedir_btn()
        self.remove_getTextButton_btn(text_box)
        self.remove_Tree_btn()
        self.remove_getTreeButton_btn(text_box)
        self.remove_delTemp_btn()
        self.remove_backup_btn()
        self.remove_sort_btn()
        self.remove_getsortButton_btn()