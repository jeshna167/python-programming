def check (story,sub_str):
    #print (story, sub_str)
    '''finding a keyword'''
    if (story.find(sub_str)==-1) :
        print("your entered keyword is not found")
    else:
        print('your keyword has been found at index number :',story.find(sub_str))
str1='''Marlin (Albert Brooks), a clown fish, is overly cautious with his son, Nemo (Alexander Gould), who has a foreshortened fin. When Nemo swims too close to the surface to prove himself, he is caught by a diver, and horrified Marlin must set out to find him. A blue reef fish named Dory (Ellen DeGeneres) -- who has a really short memory -- joins Marlin and complicates the encounters with sharks, jellyfish, and a host of ocean dangers. Meanwhile, Nemo plots his escape from a dentist's fish tank.'''
sub_str1=input("enter your keyword=  ")
#print(str1.find(sub_str1))
check(str1, sub_str1)
print(check.__doc__)