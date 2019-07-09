pinfo=open("pokemon.csv","r")
pnew=open("pokemon_new.csv","w+")

ptypeid=open("types.csv","r")
typeids = ptypeid.readlines()
ptypeid.close()
for each type in typeids:
    temp = type.split(",")
	types.add([temp[0],temp[1])
	
ptypes=open("pokemon_types.csv","r")
ptypos=ptypes.readlines()
ptypes.close()
for each ptype in ptypos:
    temp = ptype.split(",")


for each line in pinfo.readlines():
	temp = ptypes.readline()
	temps = temp.split(,)
	if temp[0] == line.split(",")[0]:
	    if temp[2] == 1:
		    type1 = type[1] where types[0] == temp[1]
		else:
		    type2 = type[1] where types[0] == temp[1]
    pnew.write(line + type1 + type2)
	
def CheckTypes()