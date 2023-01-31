f=open("/Users/divyamjain/Desktop/Code/python/game/ballandbar/game/components/public/src/level/level1.txt","r")
lines=f.readlines()
f.close()
for i in range(len(lines)):
    lines[i]=lines[i].strip()
    
print(lines)
    
def returnList():
    return lines