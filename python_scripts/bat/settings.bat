
@REM @SET GMAT=C:\Users\carlos.batista\Documents\.app\GMAT\2020a\bin\GMAT.exe
@SET GMAT=C:\Users\carlos.batista\Documents\.app\GMAT\R2022a\bin\GMAT.exe

@REM PATH TO DIFERENT FILES LOCATIONS
@SET PATH_GMAT_FILES=%USERPROFILE%\Documents\.app\GMAT\2020a\output
@SET PATH_DATA=%USERPROFILE%\Documents\.coding\plantuml\phdModelling\python_scritps\data
@SET PATH_SCRIPT=%USERPROFILE%\Documents\.coding\gmat\phdSim

@REM PlantUML images generator
@REM java -jar ..\plantuml-1.2023.0.jar ..\csrm\*.plantuml -o ".\fig\" -v -q -progress
@REM java -jar ..\plantuml-1.2023.0.jar ..\csrm\*.plantuml -o ".\fig\" -q -progress 
@REM java -jar ..\plantuml-1.2023.0.jar ..\csrm\*_elements.plantuml -o ".\xmi\" -xmi -q -progress