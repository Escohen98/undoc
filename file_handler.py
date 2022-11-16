from tkinter import filedialog as fd
#Selecting a file
#Taken from  https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
class handler():

    #Select the file for tkinter
    #To-Do: Move properties to json
    def select_file():

        filetypes (
            ('docx files', *.docx),
            ('doc files', *.doc)
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filestypes
        )

        showinfo(
            title='Selected File'
            message = filename
        )
