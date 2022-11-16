from tkinter import *
from tkinter.ttk import *
#from tkinter import filedialog as fd


from main import converter
from file_handler import handler
root = Tk()
root.title("DOCX to TXT Converter")

#Relative Height
rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
root.geometry("640x360")
root.resizable(False, False)

label = Label (
    root,
    text="Please select the file you would like to convert"
)

open_button = Button (
    root,
    text='Open a File',
    command=lambda: handler.selectfile(file_entry, convert)
)
#open_button.grid(row=2, column=1)

file_entry = Label(
root,
text="No file chosen"
)

#file_entry.grid(row=2, column=2)
convert = Button (
    root,
    text="Convert",
    command=lambda: converter.run(converter, file_entry["text"])
)





label.pack()
open_button.pack(expand=True)
file_entry.pack()

root.mainloop()
