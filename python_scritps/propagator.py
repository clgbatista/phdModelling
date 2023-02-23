
import libs.from_gmat as gmat
import os

print("Running "+os.path.basename(__file__)+"\n")
propagator = "earthPointProp"
path_to_json = "./python_scritps/data/propagator/"+propagator+".json"
outputFile = gmat.propagator_file(propagator=propagator,
                                   path_to_json=path_to_json)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)