class return_string():
    def __init__(self):
        self.string = None

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


strObj = return_string()
strObj.get_string()
strObj.print_string()
