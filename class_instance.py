class Person:
    name = "perterson"

    def __init__(self,name = None):
        self.name = name
    
jeffrey = Person("Jeffrey")
print(f"he is {jeffrey.name}")