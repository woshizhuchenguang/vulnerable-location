import pickle
import numpy as np
import re
import os
'''
file=open('TP_index_BGRU.pkl','rb')
file1=open('/home/zcg/GNN/data/sysemul/syse/sysemul_gnn/sysemul_gnn.pkl','rb')
dataset_file, linetokens_file, vpointers_file, func_file, testcase_file = pickle.load(file)
dataset1_file,label_file=pickle.load(file1)
L=np.array(linetokens_file)
print("dataset:",L.shape)
#print("dataset:",dataset_file[1])
'''
#with open("TP_index_BGRU.pkl","rb") as f:
#    print("TP_index_BGRU:", f)
#    b=pickle.load(f)
#    print("TP_index_BGRU:", b)
'''
with open("result_analyze/FN/2.pkl","rb") as f1:
    A=pickle.load(f1)
    print("a", A)


with open("/home/zcg/VulDeeLocator/program_zcg/SARD/SARD/corpus_new/000000151/point_basic-00010-large_1_56:buf,60:buf_#main#.final.pkl","rb") as f1:
    A=pickle.load(f1)
    print("a", A)


with open("/home/zcg/VulDeeLocator/src/data_preprocess/data/test_new/test_5_0125.pkl","rb") as f1:
    var10,var11,var12,var13,var14,var15=pickle.load(f1)
    #data=pickle.load(f1)
    filtered_data1 = []
    filtered_data2 = []
    filtered_data3 = []
    filtered_data4 = []
    filtered_data5 = []
    filtered_data6 = []
    #for file in data:
        #if re.search(r'cwe416',file) or re.search(r'CWE416',file):
            #filtered_data.append(file)
    j=len(var15)
    print("var15", type(var15))
    print('test_1 len',j)
    for i in range(len(var10)):

        #print("var10",var10[i] )
        #print("var11", var11[i])
        #print("var12",var12[i])
        #print("var13",var13[i])
        #print("var14",var14[i])
        #print("var15",var15[i])
        if re.search(r'cwe806', var15[i]) or re.search(r'CWE806', var15[i]):
            filtered_data1.append(var10[i])
            filtered_data2.append(var11[i])
            filtered_data3.append(var12[i])
            filtered_data4.append(var13[i])
            filtered_data5.append(var14[i])
            filtered_data6.append(var15[i])


        with open('/home/zcg/VulDeeLocator/src/data_preprocess/data/test_new/CWE806_test_5.pkl','wb') as f:
            pickle.dump([filtered_data1,filtered_data2,filtered_data3,filtered_data4,filtered_data5,filtered_data6],f)


'''
'''
with open("/home/zcg/VulDeeLocator/program_zcg/SARD/SARD/corpus_new/000000421/arr_basic-00077-min_1_60:buf_#main#.final.pkl","rb") as f2:
    var1, var2, var3, var4 = pickle.load(f2)
    print("data",var1)
    print("b", var2)
    print("c",var3)
    print("d",var4)

with open("/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input_new/000000279/arr_basic-00042-large_1_58:buf_#main#.final.pkl","rb") as f3:
    var5, var6, var7, var8,var9 = pickle.load(f3)
    #print("data",var5)
    print("b", var6)
    print("c",var7)
    print("d",var8)
    print("var9",var9)




    data=pickle.load(f)
    if 'folders_train' in data:
        print('exit')
    else:
        print('no')


'''
folder_path="/home/zcg/VulDeeLocator/src/data_preprocess/data/CWE-ID_test/CWE806/"
i=0
for filename in os.listdir(folder_path):
    if filename.endswith(".pkl"):
        file_path=os.path.join(folder_path,filename)
        with open(file_path,"rb") as f5:

            var16, var17, var18, var19, var20, var21 = pickle.load(f5)
            print(type(var18))
            for j in range(len(var18)):

                if var18[j] !=[]:
                    i+=1

print("vulnerability",i)



'''
with open("/home/zcg/VulDeeLocator/src/data_preprocess/data/dl_input/test_all/test_5_0124.pkl", "rb") as f4:
    var16,var17,var18,var19,var20,var21=pickle.load(f4)
    l=len(var16)
    #print('l',l)
    #print("data",var5)
    #print("b", var17)
    print("c", var18)
    #print("d", var19)
    #print("var9", var20)
    #print("var10", var21)
    if var18 !=[]:
        i=i+1;
'''

'''
def read_pkl_files(folder_path):
    pkl_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pkl'):
            pkl_files.append(os.path.join(folder_path, filename))


    return pkl_files

def count_and_merge(pkl_files, output_file):
    total_count = 0
    merged_data = []
    for file in pkl_files:
        with open(file, 'rb') as f:
            data = pickle.load(f)
            count = len(data) # 样本数量
            merged_data.extend(data) # 合并所有样本
            total_count += count # 总样本数量累加

    with open(output_file, 'wb') as f:
        pickle.dump(merged_data, f) # 写入合并后的数据到输出文件
    return total_count


folder_path = '/home/zcg/VulDeeLocator/src/data_preprocess/data/CWE-ID_test' # 文件夹路径
output_file = '/home/zcg/VulDeeLocator/src/data_preprocess/data/' # 输出文件路径
pkl_files = read_pkl_files(folder_path)
if len(pkl_files) > 0:
    total_count = count_and_merge(pkl_files, output_file)
    print("Total samples count:", total_count)
else:
    print("No .pkl files found in the folder.")
'''