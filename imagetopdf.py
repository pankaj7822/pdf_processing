# Python3 program to convert image to pfd
# using img2pdf library
  
# importing necessary libraries
import img2pdf
from PIL import Image
import os

images_path=sorted([os.path.join("images",f) for f in os.listdir("images")])
print(images_path)  
# storing image path

for img_path in images_path:
    # img_path = "LL_17074010_page-0007.jpg"
    
    # storing pdf path
    pdf_path = os.path.join("images_pdf",img_path[7:-4]+"pdf")
    
    # opening image
    image = Image.open(img_path)
    
    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    
    # opening or creating pdf file
    file = open(pdf_path, "wb")
    
    # writing pdf files with chunks
    file.write(pdf_bytes)
    
    # closing image file
    image.close()
    
    # closing pdf file
    file.close()
    
    # output
    print("Successfully made pdf file")