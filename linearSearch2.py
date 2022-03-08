print('linear search')
def linear(data,num):
    for i in data:
        #print(type(i),type(num))
        if i==num:
            #print(i,num)
            return num
    return -1
arr=['hi','how are you?','hello','are you busy?','what are you doing?','are you outside?']
a= input('what do you want to search? ')
result= linear(arr,a)
if result==-1 :
    print('the sentence not found')
else :
    print('the sentence is found')