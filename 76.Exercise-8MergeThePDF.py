# Question :
'''
Write a program to manipulate pdf files using pyPDF . Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities.
Hint :- pyPDF is a free and open-source pure-python PDF library capable of splitting and merging PDFs.
'''

from PyPDF2 import PdfMerger, PdfWriter , PdfReader

# We shall just make it done using the PdfMerger library. But the basic idea behind it is gonna be something like this

paths = ["/home/dc/Documents/PYTHON/pypdf Tutorial Folder/Poem.pdf","/home/dc/Documents/PYTHON/pypdf Tutorial Folder/web.pdf"]

writer = PdfWriter()

for i in paths :
    pdf = PdfReader(i,"rb")
    for page in range(len(pdf.pages)):
        writer.add_page(pdf.pages[page])
with open("merged.pdf","wb") as out :
    writer.write(out)

# Now let us see its use using the library
merger  = PdfMerger()
for path in paths :
    merger.append(path)
merger.write("Merged_New.pdf")

print("Done with the job. \n")

