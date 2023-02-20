@echo off

echo =========================================================
echo           Running - %~nx0
echo:

CALL settings.bat

echo =========================================================
echo  I - Copying script files from GMAT - %~nx0
echo:

@REM Copying the latest version of the GMAT scripts
xcopy /s /y %PATH_SCRIPT%\*.script C:\Users\carlos.batista\Documents\.coding\plantuml\phdModelling\gmat\phdSim

echo =========================================================
echo  II - Running GMAT - %~nx0
echo:

@REM 
%GMAT% -v --minimize --no_splash --version --run --exit %PATH_SCRIPT%\fcs_default.script

%GMAT% -v --minimize --no_splash --version --run --exit %PATH_SCRIPT%\fcs.script

echo  Done With GMAT

echo =========================================================
echo  III - Copying/Moving Contact Results - %~nx0
echo:

@REM Copying contact files from the GMAT output folder
move /y %PATH_GMAT_FILES%\*Contact.txt %PATH_DATA%

@REM Move to respective folders
move /y %PATH_DATA%\CON* %PATH_DATA%\conasat
move /y %PATH_DATA%\CBERS* %PATH_DATA%\cbers
move /y %PATH_DATA%\SCD* %PATH_DATA%\scd

echo =========================================================
echo Final result of %~nx0
echo:

if ERRORLEVEL 0 (
    echo SUCCESS !
) else (
    echo SOMETHING WENT WRONG !
)

echo:
echo =========================================================
echo: