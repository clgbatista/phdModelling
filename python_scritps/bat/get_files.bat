@echo off

echo =========================================================
echo           Copying files from GMAT - %~nx0
echo:

@REM Copying contact files from the GMAT output folder
xcopy /s /y C:\Users\carlos.batista\Documents\.app\GMAT\output\*Contact.txt C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data

@REM Copying the latest version of the GMAT scripts
xcopy /s /y C:\Users\carlos.batista\Documents\.coding\gmat\phdSim\*.script C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\gmat\phdSim

