import os
import shutil
import time

src_fldr=r"/media/documentos/Cursos/Python/Test/src/"
dst_fldr=r"/media/documentos/Cursos/Python/Test/dst/"
files_to_move = ['1.docx', '2.docx']
currentDate = time.strftime("%Y-%m-%d")

# iterate files
for file in files_to_move:
    # check if file exist in destination
    if os.path.exists(dst_fldr + file):
    # Split name and extension
       data = os.path.splitext(file)
       only_name = data[0]
       extension = data[1]
    # Adding the new name
       new_base = only_name +'_'+ str(currentDate) + extension
    # construct full file path
       new_name = os.path.join(dst_fldr, new_base)
    # move file
       shutil.move(src_fldr + file, new_name)
       print('Moved:', new_base)
    else:
       shutil.move(src_fldr + file, dst_fldr + file)
       print('Moved:', file)