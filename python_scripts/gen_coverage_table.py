#!/usr/bin/env python

from ast import parse
import pandas as pd
import os as os
import argparse

import warnings
warnings.filterwarnings("ignore")

import libs.from_gmat as gmat

output_dir = 'output/coverage/'
input_dir = 'output/contact/'

parser = argparse.ArgumentParser(
    description="Convert the contact files from GMAT and save it as CSV"
)

parser.add_argument("-o",
                  "--output",
                  required=False,
                  default='contact_table',
                  help="filename to be saved")
parser.add_argument("-i",
                  "--input",
                  required=False,
                  default='contact.csv',
                  help="filename to be saved")

args = parser.parse_args()

script_name = os.path.basename(__file__)
print('=========================================================')
print('         Runnning <'+script_name+'> script\n')

geojson_file = 'libs/geojson/brazil-states.geojson'
coverage_file = 'C:/Users/carlos.batista/Documents/.coding/plantuml/phdModelling/python_scritps/libs/geojson/capitals.csv'

if args.input :
    print('Reading {}'.format(input_dir+args.input))

    data = gmat.gen_contact_table(
        contact_path=input_dir+args.input,   
        geojson_path=geojson_file,
        coverage_path=coverage_file)
    file_to_save = args.output+'.csv'
    err = data.to_csv(output_dir+file_to_save,index=False)

    if not err:
        print('\nSaved to file {}'.format(output_dir+file_to_save))
    else:
        print('\nUnable to save file')

else :
    print("No input file")