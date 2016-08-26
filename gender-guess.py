import re
f = open('Tony_Judt.txt')
text = f.read()
f.close()

he = re.findall(r"\bhe\b", text, re.I)
she = re.findall(r"\bshe\b", text, re.I)
his = re.findall(r"\bhis\b", text, re.I)
her = re.findall(r"\bher\b", text, re.I)

male_count = len(he) + len(his)
female_count = len(she) + len(her)

print male_count
print female_count

if male_count > female_count: #assume equal numbers = woman
    print("man!")
else:
    print("woman!")

