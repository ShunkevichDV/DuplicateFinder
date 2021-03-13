
class PubFile:
    fullname = ""
    fullpath = ""
    ext= ""
    
    def __init__(self, name, path):
        self.fullname = name
        self.fullpath = path
    
    def get_full_description(self):
        return self.fullpath+self.fullname