## Environment

Source2slice: clang-6.0 + llvm + dg (dg: https://github.com/mchalupa/dg)

Data preprocess and Model training: python3.6 + tensorflow1.6 + keras2.1.2 + gensim3.4
数据预处理和模型训练：python3.6+tensorflow1.6+keras2.1.2+gensim3.4

## Step 2: Data preprocess ##

1. process_dataflow.py: Get the corpus of slices generated from the systhetic and academic dataset. 
process_dataflow_NVD.py: Get the corpus of slices generated from the real-world dataset. 
The input is slices generated from the systhetic and academic dataset and the real-world dataset and the output is corpus files.
process_dataflow.py：获取从综合和学术数据集生成的切片语料库。
process_dataflow_NVD.py：获取从真实数据集生成的切片语料库。
输入是从系统和学术数据集以及真实世界数据集生成的切片，输出是语料库文件。


2. create_word2vecmodel.py: Train the word2vec model. The input is the corpus files and the output is the trained model.
create_word2vecmodel.py：训练word2vec模型。输入是语料库文件，输出是训练模型。
3. get_dl_input.py. Get the vectors of tokens in the corpus files. The input is the corpus file and the trained word2vec model and the output is the vector file.
get_dl_input.py。获取语料库文件中的标记向量。输入是语料库文件和经过训练的word2vec模型，输出是向量文件。
