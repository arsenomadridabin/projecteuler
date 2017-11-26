class A():
    def __init__(self,name,age):
        self.name="Abin"
        self.age=22
    def __add__(self, other):
        age=self.age+other.age
        return(A("anonymous",age))

    def __str__(self):
        return str(self.age)
a=A("Abin",13)
b=A("Bibek",23)
print(a+b)




