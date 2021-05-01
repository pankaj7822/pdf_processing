import os
dirs=["final","images","images_pdf","text_pdf"]

for d in dirs:
    if not os.path.exists(d):
        os.mkdir(d)