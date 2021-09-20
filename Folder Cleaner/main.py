import os


def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldern, files):
    for file in files:
        os.replace(file, f"{foldern}/{file}")


files = os.listdir()
# print(files)
files.remove('main.py')
create('Images')
create('Pdf')
create('excel')
create('text')
create('others')

imgext = ['.png', '.jpg', '.jpeg']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgext]
print(images)

textext = ['.txt', '.docx']
text = [file for file in files if os.path.splitext(file)[1].lower() in textext]
print(text)

excelext = ['.xlsx', '.csv']
excel = [file for file in files if os.path.splitext(file)[1].lower() in excelext]
print(excel)

pdfext = ['.pdf']
pdf = [file for file in files if os.path.splitext(file)[1].lower() in pdfext]
print(pdf)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in textext) and (ext not in imgext) and (ext not in excelext) and (ext not in pdfext) and os.path.isfile(file):
        others.append(file)


move('Images', images)
move('excel', excel)
