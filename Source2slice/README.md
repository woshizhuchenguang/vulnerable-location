
## Step 1: Source2slice

#### For SARD program###

 (1). getVulLineForCounting.py
 
> python getVulLineForCounting.py ../../000 ../../xxx.xml 

This file is used to get the line numbers of vulnerable lines in the source code file. The input is the source code file and xxx.xml file. The output is xxx.txt file, which is renamed as SARD-hole_line.txt.
此文件用于获取源代码文件中易受攻击行的行号。输入是源代码文件和xxx.xml文件。输出为xxx.txt文件，重命名为SARD-hole_line.txt。
 (2). multiFileCompile.py
 
> python multiFileCompile.py ../../000/ ../../xxx.xml 

This file is used to compile the source code file to .bc file.
此文件用于将源代码文件编译为.bc文件。
 (3). get-llvmwithline.cpp
 
> ./get-llvmwithline SARD-hole_line.txt 

This file is used to extract four kinds of focuses. The output file is in the directory of "000".
该文件用于提取四种焦点。输出文件位于“000”目录中。
 (4). autoReorder.py
 
> python2 autoRecorder.py ../../000/ 


 (5). getFlawLoc.py
 
> python2 getFlawLoc.py ../../000/



 (6). addFlawtag.py
 
> python addFlawtag.py SARD-hole_line.txt


 (7). getSourceLine.py
 
> python getSourceLine.py ../../000/


###For real-world project program######

(1). allCompilexxx.py (or allCompilexxx0.py)
 
> python allCompilexxx.py (or allCompilexxx0.py) xxx.xls, "xxx" means name of software. 

This file is used to compile the source code file to get .bc file, and also extract four      kinds of focuses (i.e., sSyVCs). source_root is the directory of source code files, diff_root is the directory of diff files, slicer_root is the directory of output files. hole_line.txt is the  output of this step, which is renamed as "xxx-hole_line.txt".
该文件用于编译源代码文件以获取.bc文件，并提取四种焦点（即SSYVC）。source_root是源代码文件的目录，diff_root是diff文件的目录；slicer_root则是输出文件的目录。hole_line.txt是该步骤的输出，重命名为“xxx-hole_line.txt”。
 (2). autoReorder.py
 
> python2 autoReorder.py ../../newslice (or newslice0)/, "newslice" is the directory of slice files. 

This file is used to reorder the statements extracted from the source code file. The output is .final.ll file in the directory of newslice, which is an llvm slice.
此文件用于对从源代码文件中提取的语句进行重新排序。输出为.final.ll文件，它是一个llvm切片。
 (3). getFlawLoc.py
 
> python2 getFlawLoc.py ../../newslice (or newslice0)/, "newslice" is the directory of slice files. 

This file is used to get slice2flawline.pkl, which contains the line number of vulnerale lines.
此文件用于获取slice2flawline.pkl，其中包含易受攻击线路的行号。
 (4). addFlawtag.py
 
> python addFlawtag.py xxx-hole_line.txt, "xxx" means name of software. 

This file is used to get the source code slices (.slicer.c) corresponding to the llvm slices in the directory of newslice.
此文件用于获取与newslice目录中的llvm切片相对应的源代码切片（.slicer.c）。
 (5). getSourceLine.py
 
> python getSourceLine.py ../../newslice（or newslice0）/ 

This file is used to the slice2flawline.pkl, which contains the line number of vulnerable lines corresponding to the .slicer.c files.
此文件用于slice2flawline.pkl，其中包含与.slicer对应的易受攻击行的行号.c文件。


