
import libs.from_gmat as gmat
import json as json

f = open("./python_scritps/data/scd/scd1.json")

data = json.load(f)
target = data["target"]
# print("Target "+target)
f.close

path_to_file = "./gmat/phdSim/spacecraft_"+target.lower()+".txt"

f = open(path_to_file, "w")
f.write("Create Spacecraft "+target+";\n")
f.close()

for i in data["parameters"] :
    f = open(path_to_file,"a")
    if i != "keplerianElements":
        info = i+" = "+str(data["parameters"][i])
        f.write("GMAT "+data["target"]+"."+info+";\n")
    else :
        for kepler in data["parameters"]["keplerianElements"] :
            info = kepler+" = "+str(data["parameters"]["keplerianElements"][kepler])
            f.write("GMAT "+data["target"]+"."+info+";\n")
    # f.write("GMAT "+data["target"]+"."+info+";\n")
    f.close()

f = open(path_to_file,"r")
print(f.read())
f.close()

print("Saved to file: "+path_to_file)