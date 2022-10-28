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
import json

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

# -----------------------------------------------------------------------------------------------------------------------------------
# @input
#     file_path     path to the folder where you can find the .txt GMAT contact files
# @returns
#     df            pandas data frame with target, observer, start time, end time and durantion of each overpass with contact from the satellite
#
def gen_contact_table(contact_path, geojson_path, coverage_path):

    data = pd.read_csv(contact_path,
                    parse_dates=[2,3],
                    infer_datetime_format=True)

    diff = data["Stop Time (UTC)"] - data["Start Time (UTC)"]

    time = 0

    rows,cols = data.shape

    data['rev_time'] = 0
    data['day'] = ''

    for i in range(1,rows) :
        aux = data['Start Time (UTC)'][i] - data['Stop Time (UTC)'][i-1]
        data['rev_time'][i] = aux.total_seconds()

    for i in range(0,rows) :
        aux = str(data['Start Time (UTC)'][i]).split()
        data["day"][i] = aux[0]

    data['rev_time'][0]=0

    data.rev_time[data.rev_time < 0] = 0

    data["coverage"] = round(data["Duration (s)"]/(1*24*60*60),10)

    # f = open('libs/geojson/brazil-states.geojson')
    # f = open(geojson_path)
    # brazil = json.load(f)

    # state_id_map = {}
    # for feature in brazil ['features']:
    #     feature['id'] = feature['properties']['name']
    #     state_id_map[feature['properties']['sigla']] = feature['id']

    print(geojson_path)

    # coverage = pd.read_csv('C:/Users/carlos.batista/Documents/.coding/plantuml/phdModelling/python_scritps/libs/geojson/capitals.csv')
    coverage = pd.read_csv(coverage_path)

    coverage['value'] = 0

    for id in data['Observer'].unique() :
        aux = data.query('Observer == @id ')
        aux.reset_index(inplace=True)

        for dia in data['day'].unique() :
            aux2 = aux.query('day == @dia')
            aux2.reset_index(inplace=True)
            
            cov_value = aux2.coverage.sum()/len(data['day'].unique())
            coverage["value"].where(coverage['id'] != id, cov_value, inplace=True)

    return(coverage)

# -----------------------------------------------------------------------------------------------------------------------------------
# @input
#     file_path     path to the folder where you can find the .txt GMAT contact files
# @returns
#     df            pandas data frame with target, observer, start time, end time and durantion of each overpass with contact from the satellite
#