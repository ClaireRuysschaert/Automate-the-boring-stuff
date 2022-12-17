# Combines all the PDFs in the current working directory into
# into a single PDF.

# 1. Find all PDF files in the current working directory.
import PyPDF2
import os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# 2. Sort the filenames so the PDFs are added in order.
pdfFiles.sort(key = str.lower)
# 3. Write each page, excluding the first page, of each PDF to the output file.
pdfWriter = PyPDF2.PdfFileWriter()

# 4. Loop over each PDF file, creating a PdfFileReader object for it.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# 5. Loop over each page (except the first) in each PDF file.
    for pageNum in range(1, pdfReader.numPages): #skip 0 = first page
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# 6. Add the pages to the output PDF.
pdfOutput = open('allminutes.pdf', 'wb')

# 7. Write the output PDF to a file named allminutes.pdf.
pdfWriter.write(pdfOutput)
pdfOutput.close()