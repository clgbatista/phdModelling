
import libs.from_gmat as gmat

targets = ['SCD1','SCD2','CBERS4A','CONASAT1','CONASAT2','CONASAT3','CONASAT4','CONASAT5','CONASAT6']
elapsedDays = 15
propagator = 'EarthPointProp'
gmat.mission_sequence_file(targets=targets,elapsedDays=elapsedDays,propagator=propagator)

f = open("mission_sequence.txt", "r")
print(f.read())