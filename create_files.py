import numpy
import os

# Constants del programa
num_files = 20
num_rows_columns = 20
fmt_numbers='%3d'
# creo la matriu inicial a desar
identity_matrix = numpy.diag(numpy.ones(num_rows_columns))
# Agafo el directori de treball.
path_ini= os.path.abspath(os.getcwd())
# Llisto els subdirectoris
list_ini=os.listdir(path_ini)

for file in list_ini:
    if 'fitxer' in file:
        for i in range (num_files):
            fname=os.path.join(path_ini,file,'matrix'+str(i))
            if (os.path.exists(fname)) == False:
                numpy.savetxt(fname, identity_matrix, fmt=fmt_numbers)