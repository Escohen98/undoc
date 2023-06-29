from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
#Selecting a file
#Choose file and change text of given label to file
#Taken from  https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
class handler():

    #Select the file for tkinter
    #To-Do: Move properties to json
    def selectfile(label, convert_button):

        filetypes = (
            ('docx files', '*.docx'),
            ('doc files', ' *.doc')
        )

        filename = fd.askopenfilename(
            title='Choose file',
            initialdir='./',
            filetypes=filetypes
        )

        label["text"] = filename[filename.rfind("/")+1:]
        convert_button.place(relx=0.4, rely=0.75)

    #Invalid popup
    def invalidfile():
        showerror(
        'File does not exist.',
        "Invalid file. Please choose an existing 'doc' or 'docx' file.",
        icon='error'
        )

    #Popup box asking to overwrite file
    def overwrite():
        ow = askyesno(
        'Overwrite?',
        "There already is a file with the same name in this location. Do you want to overrwrite the file?",
        icon='question'
        )

        return ow

    def finished(file):
        finish = askyesno(
        'Success!',
        f"\nFile successfully converted. Do you want to open {file}?"
        )
        return finish
