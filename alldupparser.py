import re
import codecs
from pubfile import PubFile
from group import Group

class AllDupParser:
    
    @staticmethod
    def parse(filename):
        f = codecs.open(filename, 'r', 'utf8')
        lines = f.readlines()
        f.close()
        
        groups = []
        current_group = Group()
        for i in range(0, len(lines)):
            i+=1
            if i >= len(lines):
                groups.append(current_group)
                break
            if len(lines[i].strip()) == 0:
                i+=1
                groups.append(current_group)
                current_group = Group()
            else:
                current_group.add(AllDupParser.__parse_pubfile(lines[i]))
        return groups
    
    @staticmethod
    def __parse_pubfile(line) -> PubFile:
        fullname = ""
        fullpath = ""
        result = re.search(r'\[ \]\s*([^\[\]]+)\s*\[([^\[\]]+)\]', line)
        if not result is None:
            fullname = result.group(1)
            fullpath = result.group(2)+"\\"
        return PubFile(fullname, fullpath)