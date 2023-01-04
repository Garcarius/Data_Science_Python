import shutil

src_fldr=r"/media/documentos/Cursos/Python/Test/src/"
dst_fldr=r"/media/documentos/Cursos/Python/Test/dst/"
files_to_move = ['1.docx', '2.docx']
# iterate files
for file in files_to_move:
    # construct full file path
    source = src_fldr + file
    destination = dst_fldr + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)