import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))

p=id_generator(1000, "6793YUIO")
text_file = open("Output.txt", "w")
text_file.write(p)
text_file.close()