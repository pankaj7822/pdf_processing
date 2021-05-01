from PyPDF2 import PdfFileWriter, PdfFileReader
import os
inputpdf = PdfFileReader(open("example.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    f_name=os.path.join("text_pdf","page"+str(i+1)+".pdf")
    with open(f_name, "wb") as outputStream:
        output.write(outputStream)