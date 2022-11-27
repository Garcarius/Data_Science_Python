import os
import shutil

src_fldr=r"/media/documentos/Cursos/Python/Test/src/"
dst_fldr=r"/media/documentos/Cursos/Python/Test/dst/"
file_name ='1.docx'


# check if file exist in destination
if os.path.exists(dst_fldr + file_name):
    # Split name and extension
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]
    # Adding the new name
    new_base = only_name + '_new' + extension
    # construct full file path
    new_name = os.path.join(dst_fldr, new_base)
    # move file
    shutil.move(src_fldr + file_name, new_name)
else:
    shutil.move(src_fldr + file_name, dst_fldr + file_name)