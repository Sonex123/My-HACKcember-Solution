import zipfile

name = "geschenk.zip"
while name.endswith(".zip"):
    cur = zipfile.ZipFile(name)
    name = cur.namelist()[0]
    cur.extractall()
print(name)

# And then just read the Textfile in your Folder