@echo off

echo =========================================================
echo           Runnig to Coverage - %~nx0
echo:

cd ..

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py 

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py 

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT1Contact.txt -o contactCON1

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON1.csv -o coverageCON1

echo =========================================================
echo: