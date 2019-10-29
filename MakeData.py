import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir("C:/Users/beomj/Onedrive/바탕 화면");

f = open("KakaoTalk_20191029_2040_19_243_group.txt",'rt',encoding='UTF8');
dictionary = {};

lines = f.readlines()


for line in lines:
    if(line.find('[')==0):
        index1 = line.find('[') +1
        index2 = line.find(']')
        index3 = line.find(']',index2+1) +1

        name = line[index1:index2]
        if(name not in dictionary):
            dictionary[name] =[]
        else:
            dictionary[name].append(line[index3:])

name = '신재현 CUAI'
sentences = dictionary[name]

print(name)
for sentence in sentences:
    print(sentence)

f.close()