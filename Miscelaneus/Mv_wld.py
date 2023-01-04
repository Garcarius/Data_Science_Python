import glob
import os
import shutil

src_fldr=r"/media/documentos/Cursos/Python/Test/src/"
dst_fldr=r"/media/documentos/Cursos/Python/Test/dst/"
pattern = "*.docx"

# Search files with .docx extension in source directory

files = glob.glob(src_fldr + pattern)

# move the files with txt extension
for file in files:
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_fldr + file_name)
    print('Moved:', file_name)