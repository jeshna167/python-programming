#for i in range (4) :
#    print('*')
 #   for a in range (4):
  #      print("*",end="")
  #  print('\r')

# for i in range (4) :
#    for a in range (i+1):
#        print("*",end="")
#    print('\r')
# print('----------------------')
# k=4
# for i in range (4) :
#     for a in range (k):
#         print("*",end="")
#     k=k-1
#     print('\r')

k=4
for i in range (4) :
    for a in range (k):
        print(" ",end="")
    for a in range (i+1):
       print("* ",end="")
    k=k-1
    print('\r')