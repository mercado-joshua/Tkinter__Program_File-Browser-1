#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import os

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #===========================================
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(self)
        self.init_UI()
        self.init_events()

    #===========================================
    def init_events(self):
        self.listbox.bind('<Double-Button>', self.evt__open_file)

    # ------------------------------------------
    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.main_frame, text='Search File')
        self.fieldset.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.extension = tk.StringVar()
        filetypes = ['.txt', '.pdf', '.py', '.docx']
        optionmenu = ttk.OptionMenu(self.fieldset, self.extension, *filetypes)
        optionmenu.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.X, padx=5, pady=5)

        button = ttk.Button(self.fieldset, text='Browse Folder', command=self.m__choose_directory)
        button.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)

        button = ttk.Button(self.main_frame, text='Go', command=self.m__search_file)
        button.pack(side=tk.TOP, anchor=tk.NE, padx=5, pady=(0, 5))

        self.listbox = tk.Listbox(self.main_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # EVENTS -----------------------------------
    def evt__open_file(self, event):
        os.startfile(self.listbox.get(self.listbox.curselection()[0]))

    # INSTANCE METHODS -------------------------
    def m__choose_directory(self):
        self.folderpath = fd.askdirectory(initialdir='/')

    def m__search_file(self):
        """Create a .txt file with all the file of a type"""
        self.filelist = []
        for r, d, f in os.walk(self.folderpath):
            for file in f:
                if file.endswith(self.extension.get()):
                    self.filelist.append(f'{r}\\{file}')

        self.u__insert_listbox_content()

    def u__insert_listbox_content(self):
            for file in self.filelist:
                self.listbox.insert(0, file)

#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.resizable(True, True)
    app.style.theme_use('clam')
    app.title('File Browser Version 1.0')
    app.iconbitmap('python.ico')
    app.mainloop()

if __name__ == '__main__':
    main()