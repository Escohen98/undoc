from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
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

        #showinfo(
        #    title='Selected File',
        #    message = filename
        #)

        label["text"] = filename[filename.rfind("/")+1:]
        convert_button.pack(expand=True)
