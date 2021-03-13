
from pubfile import PubFile

class Group:
    __pubfiles = []
    
    def add(self, pubfile):
        self.__pubfiles.append(pubfile)
        
    def get_full_description(self):
        res = ""
        for p in self.__pubfiles:
            res += p.get_full_description()+"\n"
        return res