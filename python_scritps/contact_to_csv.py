#!/usr/bin/env python

from ast import parse
import pandas as pd
from os import listdir
import argparse

import libs.from_gmat as gmat

parser = argparse.ArgumentParser(
    description="Convert the contact files from GMAT and save it as CSV"
)

parser.add_argument("-o",
                  "--output",
                  required=False,
                  default='contact',
                  help="filename to be saved")
parser.add_argument("-i",
                  "--input",
                  required=False,
                #   default='all',
                  help="filename to be saved")

args = parser.parse_args()

print('=========================================================')
print('         Runnning contact_to_csv.py script\n')

data = pd.DataFrame()

try:
    file_path = 'C:/Users/carlos.batista/Documents/.coding/plantuml/phdModelling/python_scritps/data/'
    listdir(file_path)
    print("Running on WIN")
    print(file_path)
except:
    file_path = '/media/clgbatista/data/repos/phdModelling/python_scritps/data/'
    print("Running on Linux\n")
    print("PATH = "+file_path)

try:
    if args.input :
        data = gmat.contact_to_csv(args.input)
        # data = pd.concat([data,df],ignore_index=True)

        print('File {} appended'.format(args.input))

        file_to_save = args.output+'.csv'
        err = data.to_csv(file_to_save,index=False)
    
    else:

        for file_name in listdir(file_path):

            if file_name.endswith('.txt') :
                df = gmat.contact_to_csv(file_path+file_name)
                data = pd.concat([data,df],ignore_index=True)

                print('File {} appended'.format(file_name))

                file_to_save = args.output+'.csv'
                err = data.to_csv(file_to_save,index=False)
            else:
                break

    if not err:
        print('\nSaved to file {}'.format(file_to_save))
    else:
        print('\nUnable to save file')

except:
    print('No .txt file or directory')



