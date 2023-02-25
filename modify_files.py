import numpy
import random
import os

fmt_numbers='%3d'
# Agafo el directori de treball.
path_ini= os.path.abspath(os.getcwd())
# Llisto els subdirectoris
list_ini=os.listdir(path_ini)

userRunning = os.getlogin()
if userRunning == 'u1':
    cent= 100
    row2change=0
elif userRunning == 'u2':
    cent= 200
    row2change=1
elif userRunning == 'u3':
    cent= 300
    row2change=2
else:
    cent= 900
    row2change=3

for file in list_ini:
    if 'fitxer' in file:
        path_tmp= os.path.join(path_ini,file)
        list_matrices=os.listdir(path_tmp)
        for i_file_matrix in list_matrices:
            fname=os.path.join(path_tmp,i_file_matrix)
            tmp_matrix = numpy.loadtxt(fname)
            shape_mat=tmp_matrix.shape
            if len(shape_mat) == 1:
                tmp_matrix[row2change]=random.randint(0,99)+cent
            else:
                for j_column in range(shape_mat[1]):
                    tmp_matrix[row2change][j_column]=random.randint(0,99)+cent
        os.remove(fname)
        numpy.savetxt(fname, tmp_matrix, fmt=fmt_numbers)