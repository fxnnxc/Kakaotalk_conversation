
import os

#사용법
#1. 카톡대화를 내려받는다.
#2. 파일명입력 / 상대카톡 아이디입력
os.chdir("C:/Users/beomj/Onedrive/바탕 화면");
f = open("구오추방.txt",'rt',encoding='UTF8');
name = '노잼방송'



dictionary = {};
lines = f.readlines()
for line in lines:
    if(line.find('[')==0):
        index1 = line.find('[') +1
        index2 = line.find(']')
        index3 = line.find(']',index2+1) +1

        name2 = line[index1:index2]
        if(name2 not in dictionary):
            dictionary[name2] =[]
        else:
            dictionary[name2].append(line[index3:])

sentences = dictionary[name]



dictionary2= {}
for sentence in sentences:
    temp = sentence
    index2 = 0
    while(temp.find(' ')!=-1 and index2!=-1 ):
        index1 = temp.find(' ')
        index2 = temp.find(' ', index1+1)
        word = temp[index1:index2]
        print(word)
        if(word not in dictionary2):
            dictionary2[word] = 1
        else:
            dictionary2[word] +=1
        temp = temp[index2+1:]


dictionary2 = sorted(dictionary2.items(), key=lambda x : x[1], reverse=False)

for word in dictionary2:
    print(word)
print(name)

#for word in dictionary2:
#    print(word, dictionary2[word])

f.close()
