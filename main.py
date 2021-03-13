from alldupparser import AllDupParser

p = AllDupParser()
groups = p.parse("pdf.txt")
print(len(groups))
print(groups[0].get_full_description())