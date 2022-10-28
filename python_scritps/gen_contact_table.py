#!/usr/bin/env python

from ast import parse
import pandas as pd
from os import listdir
import argparse

import warnings
warnings.filterwarnings("ignore")

import libs.from_gmat as gmat

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

print('=========================================================')
print('         Runnning gen_contac_table.py script\n')

if args.input :
    data = gmat.gen_contact_table(args.input)
    file_to_save = args.output+'.csv'
    err = data.to_csv(file_to_save,index=False)

else :
    print("No input file")