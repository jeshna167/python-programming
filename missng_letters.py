import random

words_str=input("please enter the word= ")
letters_num= len(words_str)
print("word =",words_str)
print("number of letters=",letters_num)
loop=0

while(loop<3):
     x_num=random.randint(0,letters_num-1)
     #y_num=random.randint(0,letters_num-1)
     print(x_num)
     print(words_str[x_num])  

     #converting str into list and back:

     list1=list(words_str)
     #t_char=list1[x_num]
     list1[x_num]= "_"
     #list1[y_num]=t_char
     words_str=''.join(list1)
     print(words_str)
    
     loop= loop+1