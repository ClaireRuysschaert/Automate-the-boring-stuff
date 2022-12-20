import PyPDF2
#open PDF in binary mode
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#get the number of pages
pdfReader.numPages

#extract the text from page 1 of the pdfFileReader
pageObj = pdfReader.getPage(0) #Page object
pageObj.extractText() #extract text 

#Decrypting PDF
pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdf_reader.is_encrypted)
pdf_reader.decrypt("rosebud")
print(pdf_reader.getPage(0))

#Merge 2 PDF
# 1. Open one or more existing PDFs (the source PDFs) into PdfFileReader
# objects.
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# 2. Create a new PdfFileWriter object.
pdfWriter = PyPDF2.PdfFileWriter() #blank pdf doc
# 3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
# 4. Use the PdfFileWriter object to write the output PDF.
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#Rotating pages
page = pdfReader.getPage(0)
page.rotateClockwise(90) # 90, 180 or 270


