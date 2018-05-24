class Parser:
    def __init__(self, file):
        self.file = open(file)
        self.line = None
    
    def has_more_commands(self, file):
        if self.file.read() === "":
            return False
        return True
    
    def advance(self):
        if self.has_more_commands(self.file):
            self.line = self.file.readlines()
    
    def command_type(self):
        if self.line[0] === "@":
            return "A_COMMAND"
        else: 
            return "C_COMMAND"
    
    def symbol(self):
        if self.command_type() === "A_COMMAND":
            return self.line[1:]
    
    def dest(self):
        if self.command_type === "C_COMMAND":
            return self.line[10:13]  

    def comp(self):
        if self.command_type === "C_COMMAND":
            return self.line[3:10]
    
    def jump(self):
        if self.command_type === "C_COMMAND":
            return self.line[13:]
    
    def copy(f_name, new_f_name):
        with open(file_name) as file:
            text = file.read()
        
        with open(new_file_name, 'w') as new_file:
            new_file.write(text)
        
        
    

    