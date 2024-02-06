import numpy
import random
import os

# Constants del programa
num_files = 20
num_rows_columns = 25

# Agafo el directori de treball.
path_ini= os.path.abspath(os.getcwd())

# Llisto els subdirectoris
list_ini=os.listdir(path_ini)

permisos = ['0','1','2','3','4','5','6','7']


for p1 in range(len(permisos)):
  for p2 in range(len(permisos)):
    for p3 in range(len(permisos)):
#      for p4 in range(len(permisos)):
#      subf=os.path.join(path_ini,'carpeta_permisos_'+str(permisos[p1])+str(permisos[p2])+str(permisos[p3])+str(permisos[p4]))
        subf=os.path.join(path_ini,'carpeta_permisos_'+str(permisos[p1])+str(permisos[p2])+str(permisos[p3]))
        if not os.path.exists(subf):
          os.makedirs(subf)        
        for inf in range(num_files):
          kk= numpy.random.rand(num_rows_columns, num_rows_columns)
          fname=os.path.join(subf,'file'+str(inf)+'.txt')
          if (os.path.exists(fname)) == False:
            numpy.savetxt(fname, kk)
