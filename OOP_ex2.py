class Car :
    def __init__(self,type,name,color,price,version):
        self.t1=type
        self.name=name
        self.color=color
        self.price=price
        self.version=version
    def dream_car(self):
        print('one day, I will get',self.name,"for ",self.price)
        print(f"one day, i will buy {self.name}for{self.price}")
        print("one day, i will buy {}of{}color".format(self.name,self.color))

c1=Car("electric","hundai","purple",10000,15.0)
c1.dream_car()

c2=Car("petrol","TATA","lavender",100000,15.0)
c2.dream_car()
