colorsAndHexes=[]

for i in range(0,42):
     colorsAndHexes.append(""+str(i)+":black")

for i in range(42,84):
     colorsAndHexes.append(""+str(i)+":dgrey")

for i in range(84,126):
     colorsAndHexes.append(""+str(i)+":grey")

for i in range(126,168):
     colorsAndHexes.append(""+str(i)+":lgrey")

for i in range(168,210):
     colorsAndHexes.append(""+str(i)+":llgrey")

for i in range(210,256):
     colorsAndHexes.append(""+str(i)+":white")

#with open("./colorMap/colorMap.txt") as f:
#     content=f.readlines()
#for line in content:
#     line=line.replace(" ","")
#     line=line.replace(",","")
#     line=line.replace("(","")
#     line=line.replace(")","")
#     if line not in colorsAndHexes:
#          colorsAndHexes.append(line)

def findName(hexCode:str):
     for item in colorsAndHexes:
          item=item.split(":")
          if hexCode==item[0]:
               return item[1]
     return "black"
