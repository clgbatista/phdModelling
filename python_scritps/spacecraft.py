
import libs.from_gmat as gmat

target = "SCD1"
path_to_json = "./python_scritps/data/scd/"+target.lower()+".json"
outputFile = gmat.spacecraft_file(target=target,
                                  path_to_json=path_to_json)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)