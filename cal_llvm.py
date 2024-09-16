#统计有多少漏洞文件 多少非漏洞文件
'''
import os

def count_folders_with_cwe_files(root_folder):
    cwe_folders_count = 0

    # 遍历根文件夹及其所有子文件夹
    for root, dirs, files in os.walk(root_folder):
        # 检查当前文件夹中是否有文件名带有"CWE"字符的文件
        if any("CWE" in file for file in files):
            cwe_folders_count += 1

    return cwe_folders_count

# 示例
root_folder_path = '/home/zcg/VulDeeLocator/program_zcg/SARD/SARD/corpus_new/'
cwe_folders_count = count_folders_with_cwe_files(root_folder_path)

# 打印结果
print(f"Number of folders with files containing 'CWE' in the name: {cwe_folders_count}")
'''

#统计 CWE的种类
import os
import re

def count_cwe_occurrences(folder_path):
    cwe_dict = {}

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # 使用正则表达式匹配文件名中的 CWE\d
            match = re.search(r'CWE\d{2,3}', file)
            if match:
                cwe_key = match.group()  # 获取匹配到的 CWE\d
                cwe_dict[cwe_key] = cwe_dict.get(cwe_key, 0) + 1

    return cwe_dict

folder_path = '/home/zcg/VulDeeLocator/program_zcg/SARD/SARD/corpus_new/'  # 替换为实际的文件夹路径
result = count_cwe_occurrences(folder_path)

# 打印每种 CWE\d 出现的次数
for cwe, count in result.items():
    print(f'{cwe}: {count} times')
print('len(cwe_dict)',len(result))

'''
import os
import re
import csv
import pickle
import pandas as pd
# 读取真实标签文件
with open('/home/zcg/VulDeeLocator/program_zcg/SARD/SARD-hole_line.txt', 'r') as labels_file:
    labels_data = labels_file.readlines()

# 处理每一行数据，只保留文件名部分，并存储在字典中
real_labels_location = {}
#real_labels={}
for line in labels_data:
    sample_name, label = line.split(' ')

    file_name = '/'.join(sample_name.split('/')[9:12])
    #print('file_name',file_name)
    label=label.strip()
    if file_name in real_labels_location:
        if int(label) not in real_labels_location[file_name]:
            real_labels_location[file_name].append(int(label))
    else:
        real_labels_location[file_name] = [int(label)]
    #print('real_labels_location',real_labels_location)
    #统计漏洞文件个数
    count_files_with_zero = 0

    # 遍历字典的值
    for f in real_labels_location:
        # 检查列表是否非空，且第一个元素是否为0
        if real_labels_location[f] !=[0]:
            count_files_with_zero += 1

    print(f"文件名中值为[0]的个数: {count_files_with_zero}")

'''

'''
def extract_suffix_from_filename(file_name):
    #print('file_name',file_name)
    # 使用正则表达式匹配文件名中的 _... 部分
    match = re.search(r'_CWE\d+_(.*?)_\d+', file_name)

    if match:
        extracted_part = match.group(1)
        print(extracted_part)
    else:
        print("未匹配到目标部分")

def get_files_with_suffix(folder_path, suffix):
    file_list = []

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # 提取文件名中的 _... 部分
            extracted_suffix = extract_suffix_from_filename(file)

            # 检查后缀是否匹配
            if extracted_suffix and file.endswith(suffix):
                file_list.append(file_path)

    return file_list

folder_path = '/home/zcg/VulDeeLocator/program_zcg/SARD/SARD/corpus_new/'  # 替换为实际的文件夹路径

# 提取后缀为 .c 的文件列表
c_files = get_files_with_suffix(folder_path, '.c')

# 提取后缀为 .cpp 的文件列表
cpp_files = get_files_with_suffix(folder_path, '.cpp')

print("C Files:")
print(c_files)

print("\nC++ Files:")
print(cpp_files)
'''
