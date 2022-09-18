# @clgbatista -- clgbatista@pm.me
#
# Jun 2022
#
# -----------------------------------------------------------------------------------------------------------------------------------
#
# Lib with methods to handle gmat files
#
# -----------------------------------------------------------------------------------------------------------------------------------
#
# v0.1 -- parse the contact text file generated on gmat
#
# -----------------------------------------------------------------------------------------------------------------------------------
# 

from email.utils import parsedate
from importlib.metadata import files

import re
import pandas as pd

# -----------------------------------------------------------------------------------------------------------------------------------
# @input
#     file_path     path to the folder where you can find the .txt GMAT contact files
# @returns
#     df            pandas data frame with target, observer, start time, end time and durantion of each overpass with contact from the satellite
#
def contact_to_csv(file_path):

    df = pd.DataFrame()

    count = 0
    with open(file_path) as fp:
        while True:
            count += 1
            line = fp.readline()

            if not line: # if reaches the end of the file
                break

            match = re.findall('Target',line) # extracts the target satellite
            if match:
                target = line[8:-1]

            match = re.findall('Observer:',line) # extracts the observer/gs on the overpass
            if match:
                observer = line[10:-1]

            match = re.findall('\d\d ',line) # extracts the start, end time and duration of the overpass
            if match:
                start_time = line[0:24]
                end_time = line[28:52]
                duration = line[58:70]
                # day = start_time.split()[0:3]
                data_cols = pd.DataFrame({'Target': [target],
                                         'Observer': [observer],
                                         'Start Time (UTC)': [start_time],
                                         'Stop Time (UTC)': [end_time],
                                         'Duration (s)': [duration],
                                        #  'Day': [day]
                                         })
                df = pd.concat([df,data_cols], ignore_index=True)

    fp.close() # close the file

    return df # returns the data frame