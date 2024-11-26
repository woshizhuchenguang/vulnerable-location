## Environment

Source2slice: clang-6.0 + llvm + dg 
Data preprocess and Model training: python3.6.13 + tensorflow1.6.0 + keras2.1.2 + gensim3.4.0

Model training ##

 bgru_CNN_zcg_fusion.py: Train the BGRU model which can locate the vulnerabilities and evaluate it. The input is the training dataset and the test dataset, and the output is the trained BGRU model.
训练BGRU模型，该模型可以定位漏洞并对其进行评估。输入是训练数据集和测试数据集，输出是训练的模型。

