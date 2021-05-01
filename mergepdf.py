from PyPDF2 import PdfFileMerger
import os

pdfs = list(os.listdir("final"))
pdf_paths=[os.path.join("final",f) for f in pdfs]
merger = PdfFileMerger()

for pdf in pdf_paths:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()