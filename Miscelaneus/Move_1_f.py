import shutil

src_fldr=r"/media/documentos/Cursos/Python/Test/src/"
dst_fldr=r"/media/documentos/Cursos/Python/Test/dst/"
file="1.docx"
file2="1_r.docx"
shutil.move(src_fldr+file,dst_fldr+file2)