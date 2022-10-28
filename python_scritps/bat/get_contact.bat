@echo off

echo =========================================================
echo           Copying files from GMAT - %~nx0
echo:

xcopy /s /y C:\Users\carlos.batista\Documents\.app\GMAT\output\*Contact.txt C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data

xcopy /s /y C:\Users\carlos.batista\Documents\.coding\gmat\phdSim\*.script C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\gmat\phdSim

py ..\contact_to_csv.py -i CONASAT1Contact.txt -o contactCON1

py ..\gen_contact_table.py -i contactCON1.csv -o coverageCON1