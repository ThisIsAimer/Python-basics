import zipfile
import pathlib

def zip_converter(files,directory):
    dir_parth = pathlib.Path(directory,"compressed.zip")
    with zipfile.ZipFile(dir_parth,"w") as archive:
        for file in files:
            file= pathlib.Path(file)
            archive.write(file,arcname=file.name)