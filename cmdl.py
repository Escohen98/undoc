import os
import zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

#Converts word document to text
def main(file):
    filename = file[:file.rfind(".")]
    extension = file[file.rfind(".")+1:]
    #Checks to make sure correct file path
    if (not ((extension == "docx" or extension == "doc") and os.path.isfile(file))):
        print("Invalid file. Please choose an existing 'doc' or 'docx' file.")
        main(input("file: "))
        exit()

    docToTxt(filename)
    print("Done.")

#Creates zip object from word document
#Pulls and formats xml
#Extracts text from XML and parses to text document.
def docToTxt(folder):
    #Reading lines. Efficient?
    doc = zipfile.ZipFile(folder + ".docx")
    #Turns 1 line into formatted XML
    prettyXML = BeautifulSoup(doc.read('word/document.xml'), features="xml").prettify()
    root = ET.fromstring(prettyXML)

    namespace = {'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    text = root.findall('.//w:t', namespace) #All text is stored in <w:t*>

    g = open(overwrite(folder), 'w')
    for t in text: #XML is one line, but just to be safe..
        #print(repr(t.text.replace("\n", "").strip()))
        g.write(t.text.replace("\n", "").strip())
    g.close()

#Checks if output file exists
#Asks if overwrite
def overwrite(folder):
    newfile =  folder + ".txt"
    if(os.path.isfile(newfile)):
        overwrite = False
        while(True):
            inp = input("There already is a file with the same name in this location. Do you want to overrwrite (y/n)? ").lower()
            if(inp == "no" or inp == "n"):
                break
            if(inp == "yes" or inp == "y"):
                overwrite = True
                break
            print("Please answer yes or no")

        #Uses windows naming convention of (n)
        if(not overwrite):
            x = 0
            while(os.path.isfile(newfile)):
                x+=1
                newfile = f"{folder}({x}).txt"
    return newfile

main(input("file: "))
