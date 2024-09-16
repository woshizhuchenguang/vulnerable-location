## coding: utf-8
'''
This python file is used to split database into 80% train set and 20% test set, tranfer the original code into vector, creating input file of deap learning model.
'''
from __future__ import print_function
from gensim.models.word2vec import Word2Vec
import numpy as np
import pickle
import os
import gc
import shutil

VECTOR_DIM = 30  
MAXLEN = 900




VECTORPATH = "/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_new/"
input_folder="/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_new/"
novul_folder="/home/zcg/VulDeeLocator/src/data_preprocess/data/novul_vector/"
vul_folder="/home/zcg/VulDeeLocator/src/data_preprocess/data/vul_vector/"
i=0
j=0
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        file_path=os.path.join(root,filename)
        with open(file_path,'rb') as f:
            var1,var2,var3,var4,var5=pickle.load(f)
        if var3==[]:
            output_folder=novul_folder
            i=i+1
        else:
            output_folder=vul_folder
            j=j+1
        output_path=os.path.join(output_folder,filename)
        shutil.move(file_path,output_path)

print("\nsuccess!")
print("novul num",i)
print("vul num",j)
