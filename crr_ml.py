import random

lst_orig = []
lst_miss=[]
lst_scramble = []

n = int(input("num of elements:"))

for i in range(0,n):
    words_str=input()
    lst_orig.append(words_str)
    
##Missing letters
for index in range(len(lst_orig)):
    loop=0
    words_str = lst_orig[index]
    letters_num= len(words_str)

    while(loop<letters_num/2):
        x_num=random.randint(0,letters_num-1)
        list1=list(words_str)
        list1[x_num]= "_"
        words_str=''.join(list1)          
        loop= loop+1
    lst_miss.append(words_str)


## scrambled letters
for index in range(len(lst_orig)):
    loop=0
    words_str = lst_orig[index]
    letters_num= len(words_str)

    while(loop<letters_num/2):
        x_num=random.randint(0,letters_num-1)
        y_num=random.randint(0,letters_num-1)
        list1=list(words_str)
        t_char = list1[x_num]
        list1[x_num]= list1[y_num]
        list1[y_num] = t_char
        words_str=''.join(list1)          
        loop= loop+1        
    lst_scramble.append(words_str)

print("original=",lst_orig)
print("missing letters=",lst_miss)
print("scrambled letters=",lst_scramble)