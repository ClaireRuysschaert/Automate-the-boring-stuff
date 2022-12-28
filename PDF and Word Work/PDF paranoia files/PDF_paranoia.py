import os
from pathlib import Path
import PyPDF2
import sys

# go through every PDF in a folder/subfolder
# encrypt every file with a password provided on the command line
my_dir = Path.cwd()
input_mdp = sys.argv[1]

for root, sub_dir, pdf_list in os.walk(my_dir):
    for pdf_file in pdf_list:
        if pdf_file.endswith('.pdf'):
            pdf_to_encrypt= open(Path(root) / pdf_file, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_to_encrypt)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            pdf_writer.encrypt(input_mdp)
            # save the doc with an _encripted.pdf suffix added to the original filename
            result_pdf = open(Path(root) / f'{pdf_file}_encripted.pdf', 'wb')
            pdf_writer.write(result_pdf)
            pdf_to_encrypt.close()
            result_pdf.close()
            # delete the original file
            os.remove(Path(root) / pdf_file)

