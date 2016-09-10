import re
import glob

for name in glob.glob("*-raw.txt"):
    f = open(name)
    wikihistorian = f.read()
    f.close()


    he = re.findall(r"\bhe\b", wikihistorian, re.I)
    she = re.findall(r"\bshe\b", wikihistorian, re.I)
    his = re.findall(r"\bhis\b", wikihistorian, re.I)
    her = re.findall(r"\bher\b", wikihistorian, re.I)

    male_count = len(he) + len(his)
    female_count = len(she) + len(her)

    if male_count > female_count: #assume equal numbers = woman
        print(name+" guessing ... man. (male "+str(male_count)+ "/female "+str(female_count)+")")
    else:
        print(name+" guessing ... woman. (male "+str(male_count)+ "/female "+str(female_count)+")")
