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

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT2Contact.txt -o contactCON2

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON2.csv -o coverageCON2

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT3Contact.txt -o contactCON3

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON3.csv -o coverageCON3

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT4Contact.txt -o contactCON4

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON4.csv -o coverageCON4

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT5Contact.txt -o contactCON5

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON5.csv -o coverageCON5

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i conasat/CONASAT6Contact.txt -o contactCON6

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCON6.csv -o coverageCON6

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i SCD/SCD1Contact.txt -o contactSCD1

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactSCD1.csv -o coverageSCD1

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i SCD/SCD2Contact.txt -o contactSCD2

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactSCD2.csv -o coverageSCD2

echo =========================================================
echo:

@REM ----------------------------------------------------------
@REM Convert Contact text file(s) to csv
py contact_to_csv.py -i CBERS/CBERSContact.txt -o contactCBERS

@REM ----------------------------------------------------------
@REM Create Coverage csv file(s)
py gen_coverage_table.py -i contactCBERS.csv -o coverageCBERS

echo =========================================================
echo: