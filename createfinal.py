import os
import shutil


image_pdf_index=[1,2]
text_pdf_index=[3,4]


f=sorted(os.listdir("images_pdf"))
g=sorted(os.listdir("text_pdf"))
image_pdf_paths=[os.path.join("images_pdf",f[i-1]) for i in image_pdf_index]
text_pdf_paths=[os.path.join("text_pdf",g[j-1]) for j in text_pdf_index]

for i in range(len(image_pdf_paths)):
    original=image_pdf_paths[i]
    target=os.path.join("final",f[image_pdf_index[i]-1])
    shutil.copyfile(original, target)


for i in range(len(text_pdf_paths)):
    original=text_pdf_paths[i]
    target=os.path.join("final",g[text_pdf_index[i]-1])
    shutil.copyfile(original, target)