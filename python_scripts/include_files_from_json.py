
import libs.from_gmat as gmat
import os

print("Running "+os.path.basename(__file__)+"\n")

script_name = "./gmat/phdSim/example.script"
script_file = open(script_name,"w")
gmat.write_header(file=script_file)

# ---------------------------------------------------------
# Spacecraft
item = "Spacecraft"
gmat.write_header(file=script_file,msg=item)

# json_file = "./python_scritps/data/groundStations/etc.json"
json_file = "./python_scripts/data/scd/scd1.json"

outputDirectory = "./gmat/phdSim/"

# outputFile = gmat.from_json(object="GroundStation",
outputFile,file_name = gmat.from_json(object=item,
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

script_file.write("# Include '"+ file_name +"' \n")
print("Saved to file: "+outputFile)

# ---------------------------------------------------------
# Ground Stations
item = "GroundStation"
gmat.write_header(file=script_file,msg=item)

json_file = "./python_scripts/data/groundStations/etc.json"

outputDirectory = "./gmat/phdSim/"

outputFile,file_name = gmat.from_json(object=item,
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

script_file.write("# Include '"+ file_name +"' \n")
print("Saved to file: "+outputFile)

# ---------------------------------------------------------
# Force Model
item = "ForceModel"
gmat.write_header(file=script_file,msg=item)

json_file = "./python_scripts/data/forceModel/earthpointprop_forcemodel.json"

outputDirectory = "./gmat/phdSim/"

outputFile,file_name = gmat.from_json(object=item,
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

script_file.write("# Include '"+ file_name +"' \n")
print("Saved to file: "+outputFile)

# ---------------------------------------------------------
# Propagator
item = "Propagator"
gmat.write_header(file=script_file,msg=item)

json_file = "./python_scripts/data/propagator/earthpointprop.json"

outputDirectory = "./gmat/phdSim/"

outputFile,file_name = gmat.from_json(object=item,
                            path_to_json=json_file,
                            path_to_save=outputDirectory)

script_file.write("# Include '"+ file_name +"' \n")
print("Saved to file: "+outputFile)

# ---------------------------------------------------------
# Mission Sequence
item = "MissionSequence"
gmat.write_header(file=script_file,msg=item)

outputFile,file_name = gmat.mission_sequence_file(targets=["SCD1"])

script_file.write("# Include '"+ file_name +"' \n")
print("Saved to file: "+outputFile)

print("\nSaved to file: "+script_name)