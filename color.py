class User:
    def __init__(self, first, last):
        self.name = first

    def full_name(self):
        return f"{self.first} {self.last}"

user1 = User('Joe')
user2 = User('Balance') 
