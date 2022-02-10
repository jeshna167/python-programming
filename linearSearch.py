print('linear search')
def linear(data,num):
    for i in data:
        #print(type(i),type(num))
        if i==num:
            #print(i,num)
            return num
    return -1
arr=[1,3,9,7,0,5,8]
a= int(input('what do you want to search? '))
result= linear(arr,a)
if result==-1 :
    print('the number not found')
else :
    print('the number is found')