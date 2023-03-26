
import PyPDF2
import os
import sys

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        
       #print(file)
       
       merger.append(file)
    merger.write("CombinedFilesin.Docs.pdf")


    