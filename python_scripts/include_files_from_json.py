
import libs.from_gmat as gmat
import os

print("Running "+os.path.basename(__file__)+"\n")

# json_file = "./python_scritps/data/groundStations/etc.json"
json_file = "./python_scritps/data/scd/scd1.json"

outputDirectory = "./gmat/phdSim/"

# outputFile = gmat.from_json(object="GroundStation",
outputFile = gmat.from_json(object="Spacecraft",
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)