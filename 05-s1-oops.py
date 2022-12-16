class Person:
    name="khadeer"
    def sayHello(self):
        print(f"my name is {self.name} \nhi to you..  ")

def main():
    a=Person()
    a.sayHello()
    n=input("\nenter your name: ")
    a.name=n
    a.sayHello()

main()