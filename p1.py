class p1:
    e=0;
    def __init__(self, name, id):
        self.name=name
        self.id=id
        p1.e=p1.e+1
    def display(self):
        print("name: ",self.name)
        print("id: ",self.id)

    def d(self):
        print(p1.e)



e1=p1("rahul",1)
e2=p1("kanthi",2)
e1.display()
e2.display()
print(p1.e)