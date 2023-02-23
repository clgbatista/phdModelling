
import libs.from_gmat as gmat
import os

print("Running "+os.path.basename(__file__)+"\n")
forceModel = "earthPointProp_ForceModel"
path_to_json = "./python_scritps/data/forceModel/"+forceModel+".json"
outputFile = gmat.force_model_file(forceModel=forceModel,
                                   path_to_json=path_to_json)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)