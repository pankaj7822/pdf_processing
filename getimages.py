from pdf2image import convert_from_path,convert_from_bytes
import os
import PyPDF2
from PIL import Image
import tempfile

pdf_file="example.pdf"
dpi=150
quality=100


pdf = PyPDF2.PdfFileReader(pdf_file,"rb")
p = pdf.getPage(0)
w_in_user_space_units = p.mediaBox.getWidth()
h_in_user_space_units = p.mediaBox.getHeight()


# 1 user space unit is 1/72 inch
# 1/72 inch ~ 0.352 millimeters
# pixels = inches * PPI
# p.mediaBox.getWidth() returns width in user space unit

w = float(p.mediaBox.getWidth())*dpi/72.0
h = float(p.mediaBox.getHeight())*dpi/72.0
print(w,h)
# Store Pdf with convert_from_path function
images=convert_from_path(pdf_file,dpi=dpi,size=(w,h),fmt="jpeg",jpegopt={
    "quality": quality,
    "progressive": True,
    "optimize": True
})
 
for i in range(len(images)):
    save_path=os.path.join("images",'page'+ str(i+1) +'.jpeg')
    im=images[i]
    im.save(save_path, 'JPEG',quality=quality,dpi=(dpi, dpi))
    print("Sucessfuly Saved ",save_path)