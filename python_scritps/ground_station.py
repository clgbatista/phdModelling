
import libs.from_gmat as gmat

observer = "ETC"
path_to_json = "./python_scritps/data/groundStations/"+observer.lower()+".json"
outputFile = gmat.ground_station_file(observer=observer,
                                  path_to_json=path_to_json)

f = open(outputFile,"r")
print(f.read())
f.close()

print("Saved to file: "+outputFile)