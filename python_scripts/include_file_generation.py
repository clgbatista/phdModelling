
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
parser.add_argument(
    "-i",
    "--item",
    required=True,
    help="object item to be added",
    choices=["Spacecraft","GroundStation","ForceModel","Propagator","ContactEvent"]
)

args = parser.parse_args()

print("Running "+os.path.basename(__file__)+"\n")

json_file = args.json
item = args.item
outputDirectory = args.output

outputFile = gmat.from_json(object=item,
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)