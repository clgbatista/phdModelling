
import libs.from_gmat as gmat
import os
import argparse

parser = argparse.ArgumentParser(
    description="Generate the include txt files for GMAT script"
)

parser.add_argument(
    "-o",
    "--output",
     required=True,
     help="path to the output directory"
)
parser.add_argument(
    "-j",
    "--json",
    required=True,
    help="json object file path"
)

args = parser.parse_args()

print("Running "+os.path.basename(__file__)+"\n")

# json_file = "./python_scritps/data/groundStations/etc.json"
# json_file = "./python_scritps/data/scd/scd1.json"
json_file = args.json

# outputDirectory = "./gmat/phdSim/"
outputDirectory = args.output

# outputFile = gmat.from_json(object="GroundStation",
outputFile = gmat.from_json(object="Spacecraft",
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)