import re
import pandas as pd

def contact_to_csv(file_name):

    df = pd.DataFrame()

    # file_name = 'SCD1Contact.txt'
    data_folder = 'C:/Users/carlos.batista/Documents/.coding/plantuml/phdModelling/python_scritps/data/'+file_name

    count = 0
    with open(data_folder) as fp:
        while True:
            count += 1
            line = fp.readline()

            if not line:
                break

            match = re.findall('Target',line)
            if match:
                target = line[8:-1]

            match = re.findall('Observer:',line)
            if match:
                observer = line[10:-1]

            match = re.findall('\d\d ',line)
            if match:
                start_time = line[0:24]
                end_time = line[28:52]
                duration = line[58:70]
                data_cols = pd.DataFrame({'Target': [target],'Observer': [observer], 'Start Time (UTC)': [start_time], 'Stop Time (UTC)': [end_time], 'Duration (s)': [duration]})
                df = pd.concat([df,data_cols], ignore_index=True)

    fp.close()

    # df.to_csv('contact.csv',index=False)

    return df