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

VECTOR_DIM = 30  
MAXLEN = 900



def get_dldata(filepath, dlTrainCorpusPath, dlTestCorpusPath, split=0.8, seed=2018, batch_size=16):
    """create deeplearning model dataset
    
    This function is used to create train dataset and test dataset

    # Arguments
        filepath: String, path of all vectors          
        dlTrainCorpusPath: String, path of train set    
        dlTestCorpusPath: String, path of test set     
        seed: seed of random                           
        batch_size: the size of mini-batch             
    
    """
    '''
    testcases=[]
    f = open("/home/zcg/VulDeeLocator/src/record/synthetic and academic dataset/testcases_train.pkl",'rb')
    testcases += pickle.load(f)
    f.close()

    f = open("/home/zcg/VulDeeLocator/src/record/synthetic and academic dataset/testcases_train.pkl",'rb')
    testcases += pickle.load(f)
    f.close()
    '''
    print("produce train dataset...")
    folders=os.listdir(filepath)
    np.random.seed(seed)#设置随机数，使用np.random()生成的数据会打乱顺序
    np.random.shuffle(folders)#打乱data的顺序
    folders_train=folders[:int(len(folders)*split)]
    folders_test=folders[int(len(folders)*split):]

    N = 6
    num = list(range(N))

    for i in num:
        train_set = [[], [], [], [], [], []]

        for folder_train in folders_train[int(i*len(folders_train)/N) : int((i+1)*len(folders_train)/N)]:
            if not folder_train in os.listdir(filepath):
                continue
            print("\r"+str(folder_train), end='')
            for filename in os.listdir(os.path.join(filepath, folder_train)):
                f = open(filepath + folder_train + '/' + filename, 'rb')
                data = pickle.load(f)
                f.close()
                if len(data[0][0]) > MAXLEN:
                    data[2] = [x for x in data[2] if x <= MAXLEN]
                data[0] = cutdata(data[0][0])
                if data[0] == None:
                    continue        
                for n in range(len(data)):
                    train_set[n].append(data[n])
                train_set[-1].append(folder_train+"/"+filename)
        f_train = open(dlTrainCorpusPath + "train_1000" + str(i)+ "_0721.pkl", 'wb')
        pickle.dump(train_set, f_train)
        f_train.close()

        del train_set 
        gc.collect() 

    print("\nproduce test dataset...")
    N = 6
    num = list(range(N))
    for i in num:
        test_set = [[], [], [], [], [], []]
        for folder_test in folders_test[int(i*len(folders_test)/N) : int((i+1)*len(folders_test)/N)]:
            if not folder_test in os.listdir(filepath):
                continue
            print("\r"+str(folder_test), end='')
            for filename in os.listdir(os.path.join(filepath, folder_test)):
                f = open(filepath + folder_test + '/' + filename, 'rb')
                data = pickle.load(f)
                f.close()
                if len(data[0][0]) > MAXLEN:
                    data[2] = [x for x in data[2] if x <= MAXLEN]
                data[0] = cutdata(data[0][0])
                if data[0] == None:
                    continue        
                for n in range(len(data)):
                    test_set[n].append(data[n])
                test_set[-1].append(folder_test+"/"+filename)
            
        f_test = open(dlTestCorpusPath + "test_1000" + str(i)+ "_0721.pkl", 'wb')
        pickle.dump(test_set, f_test)
        f_test.close()

        del test_set
        gc.collect()
    return
    
def cutdata(data, maxlen=MAXLEN, vector_dim=VECTOR_DIM):
    """cut data to maxlen
    
    This function is used to cut the slice or fill slice to maxlen

    # Arguments
        data: The slice
        maxlen: The max length to limit the slice
        vector_dim: the dim of vector
    
    """
    if maxlen:
        fill_0 = [0]*vector_dim
        if len(data) > 900:
            pass
        if len(data) <=  maxlen:
            data = data + [fill_0] * (maxlen - len(data))
        else:
            data = data[:maxlen]
    return data

if __name__ == "__main__":

    

    print("spliting the train set and test set...")
    VECTORPATH = "/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_new/"
    input_folder="/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_new/"
    dlTrainCorpusPath = "/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_5_fold/train1_1000/"
    dlTestCorpusPath = "/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_5_fold/test1_1000/"
    get_dldata(VECTORPATH, dlTrainCorpusPath, dlTestCorpusPath)
    '''#将有漏洞的和没有漏洞的区分到2个文件夹，方便平衡数据集
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            file_path=os.path.join(root,filename)
            with open(file_path,'rb') as f:
                var1,var2,var3,var4,var5=pickle.load(f)
            if vars is None:
                #output_folder=novul_folder
            else:
                #out_folder=vul_folder

            output_path=os.path.join(output_folder,filename)
            shutil.move(file_path,output_path)
    '''
    print("\nsuccess!")
    
