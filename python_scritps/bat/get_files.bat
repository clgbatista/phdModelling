@echo off

echo =========================================================
echo           Running - %~nx0
echo:

CALL settings.bat

echo =========================================================
echo  I - Copying script files from GMAT - %~nx0
echo:

@REM Copying the latest version of the GMAT scripts
xcopy /s /y C:\Users\carlos.batista\Documents\.coding\gmat\phdSim\*.script C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\gmat\phdSim

echo =========================================================
echo  II - Running GMAT - %~nx0
echo:

@REM 
%GMAT% -v --minimize --no_splash --version --run --exit ..\..\gmat\phdSim\fcs_default.script

%GMAT% -v --minimize --no_splash --version --run --exit ..\..\gmat\phdSim\fcs.script

echo =========================================================
echo  III - Copying/Moving Contact Results - %~nx0
echo:

@REM Copying contact files from the GMAT output folder
move /y C:\Users\carlos.batista\Documents\.app\GMAT\output\*Contact.txt C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data

@REM Move to respective folders
move /y C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\CON* C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\conasat
move /y C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\CBERS* C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\cbers
move /y C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\SCD* C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\python_scritps\data\scd

echo =========================================================
echo: