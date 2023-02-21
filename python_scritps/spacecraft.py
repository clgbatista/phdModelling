
import libs.from_gmat as gmat

f = open("./gmat/phdSim/spacecraft.txt", "w")
f.write("GMAT SCD1.SMA = 7121.000000000004;")
f.close()

f = open("./gmat/phdSim/spacecraft.txt","r")
print(f.read())
f.close()