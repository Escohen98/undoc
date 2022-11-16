import os
import shutil
import zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def main(file):
    filename = file[:file.rfind(".")]
    extension = file[file.rfind(".")+1:]
    #Checks to make sure correct file path
    if (not (extension == "docx" or extension == "doc")):
        print("Invalid file. Please choose a 'doc' or 'docx'")
        main(input("file: "))
        exit()

    #Convert a document to zip
    folder = filename #Custom folder name
    newfile = docToZip(folder)

    # Rename the file
    shutil.copyfile(file, newfile)

    #Extracting files to folder
    with zipfile.ZipFile(newfile, 'r') as zip_ref:
        zip_ref.extractall(folder)

    zipToTxt(folder)

    os.remove(newfile) #Deletes zip
    shutil.rmtree(folder) #Deletes extracted directory tree
    print("Done.")

#Converts the zip xml content to text
def zipToTxt(folder):
    #Reading lines. Efficient?
    doc = zipfile.ZipFile(folder + ".docx")
    prettyXML = BeautifulSoup(doc.read('word/document.xml'), features="xml").prettify() #Turns 1 line into formatted XML
    root = ET.fromstring(prettyXML)

    namespace = {'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    text = root.findall('.//w:t', namespace) #All text is stored in <w:t*>
    g = open(folder + ".txt", 'w')

    print("hi")
    for t in text: #XML is one line, but just to be safe..
        print(t.text)
        g.write(t.text)
    g.close()

def docToZip(folder):
    newfile =  folder + ".zip"
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

        if(not overwrite):
            x = 0
            while(os.path.isfile(newfile)):
                x+=1
                folder = f"{filename}({x})"
                newfile = folder + ".zip"
    return newfile

def xmlToTxt(folder):

    tree = ET.parse(f"./{folder}/word/document.xml")
    root = tree.getroot()
    myroot = ET.fromstring(f"./{folder}/word/document.xml")

    g = open(folder + ".txt", 'w')

    #for x in root.findall('field'):
    for x in myroot[0]:
        print(x.text)
        g.write(x.text)

    g.close()

main(input("file: "))
