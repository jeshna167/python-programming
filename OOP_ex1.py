class Cat:
    att1="cat" 
    att2="mammal"
    def fun(self):
        print("i am a",self.att1)
        print("I am a ", self.att2)

allergy=Cat()

print(allergy.att1)

allergy.fun()
