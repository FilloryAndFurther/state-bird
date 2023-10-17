from datetime import datetime
from random import choices
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import (
    BOTH, BOTTOM, CENTER, E, END, EW, LEFT, NE, NSEW, NW, RIGHT, SE, SW, TOP,
    W, X, Y
)
from tkinter.scrolledtext import ScrolledText
from pathlib import Path

import state_bird.data.read as read

PATH = Path(__file__).parent / 'assets'


class StateBirdApp(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=15)
        self.pack(fill=BOTH, expand=True)
        image_files = {
            "Create": "Plus.png",
            "Settings": "Settings.png",
            "Update": "hexsync.png",
        }
        self.photoimages = []
        imgpath = Path(__file__).parent / 'assets'
        for key, val in image_files.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))
            
        buttonbar = ttk.Frame(self, style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)
        
        btn = ttk.Button(
            master=buttonbar, 
            text='New Project',
            compound=LEFT,
            image='Create',
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)
        
        btn = ttk.Button(
            master=buttonbar, 
            text='Settings', 
            image='Settings',
            compound=LEFT, 
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        module_panel = ttk.Frame(self, style='primary.TFrame')
        module_panel.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=1)
        module_label = ttk.Label(
            master=module_panel,
            text='Modules',
            anchor=W,
            bootstyle=('primary', 'inverse')
        )
        module_label.pack(side=TOP)
        
        module_entry_frame = ttk.Frame(module_panel, style='primary.TFrame')
        module_entry_frame.pack(fill=X, expand=True, side=BOTTOM)
        module_name_entry = ttk.Entry(module_entry_frame)
        module_name_entry.pack(fill=X, expand=True, side=LEFT, padx=5, pady=1)
        module_create_btn = ttk.Button(
            master=module_entry_frame, 
            text='Create',
            compound=LEFT,
            image='Create',
        )
        module_create_btn.pack(side=RIGHT, ipadx=5, ipady=5, padx=0, pady=1)
        module_tv = ttk.Treeview(module_panel)
        module_tv.pack(fill=BOTH, expand=True, side=TOP)

        modules = read.get_all_modules()
        for module in modules:
            module_tv.insert('', 'end', text=module[1])

        state_panel = ttk.Frame(self, style='primary.TFrame')
        state_panel.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=1)
        state_label = ttk.Label(
            master=state_panel,
            text='states',
            anchor=W,
            bootstyle=('primary', 'inverse')
        )
        state_label.pack(side=TOP)
        
        state_entry_frame = ttk.Frame(state_panel, style='primary.TFrame')
        state_entry_frame.pack(fill=X, expand=True, side=BOTTOM)
        state_name_entry = ttk.Entry(state_entry_frame)
        state_name_entry.pack(fill=X, expand=True, side=LEFT, padx=5, pady=1)
        state_create_btn = ttk.Button(
            master=state_entry_frame, 
            text='Create',
            compound=LEFT,
            image='Create',
        )
        state_create_btn.pack(side=RIGHT, ipadx=5, ipady=5, padx=0, pady=1)
        state_tv = ttk.Treeview(state_panel)
        state_tv.pack(fill=BOTH, expand=True, side=TOP)

        states = read.get_states()
        for state in states:
            state_tv.insert('', 'end', text=state[2])


class ItemList(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


def main():
    main_app = ttk.Window("State Bird App")
    StateBirdApp(main_app)
    main_app.mainloop()


if __name__ == '__main__':
    main()
