
import libs.from_gmat as gmat
import json as json

f = open("./python_scritps/data/scd/scd1.json")

data = json.load(f)
print("Target "+data["target"])
f.close

f = open("./gmat/phdSim/spacecraft.txt", "w")
f.write("Create Spacecraft "+data["target"]+";\n")
f.close()

path_to_file = "./gmat/phdSim/spacecraft.txt"

for i in data["parameters"] :
    f = open(path_to_file,"a")
    if i != "keplerianElements":
        info = i+" = "+str(data["parameters"][i])
        # f.write("GMAT "+data["target"]+"."+info+";\n")
    else :
        for kepler in data["parameters"]["keplerianElements"] :
            info = kepler+" = "+str(data["parameters"]["keplerianElements"][kepler])
            # f.write("GMAT "+data["target"]+"."+info+";\n")
    f.write("GMAT "+data["target"]+"."+info+";\n")
    f.close()

f = open("./gmat/phdSim/spacecraft.txt","r")
print(f.read())
f.close()