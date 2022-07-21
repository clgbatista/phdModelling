import pandas as pd
from os import listdir

import libs.from_gmat as gmat

print('Runnning contact_to_csv.py script\n')

data = pd.DataFrame()

try:
    file_path = 'C:/Users/carlos.batista/Documents/.coding/plantuml/phdModelling/python_scritps/data/'
    listdir(file_path)
    print("Running on WIN")
except:
    file_path = '/media/clgbatista/data/repos/phdModelling/python_scritps/data/'
    print("Running on Linux\n")

try:
    for file_name in listdir(file_path):
        
        if file_name.endswith('.txt'):
            df = gmat.contact_to_csv(file_path+file_name)
            # print(len(df))
            data = pd.concat([data,df],ignore_index=True)

            print('File {} appended'.format(file_name))

            file_to_save = 'contact.csv'
            err = data.to_csv(file_to_save,index=False)
        else:
            break

    if not err:
        print('\nSaved to file {}'.format(file_to_save))
    else:
        print('\nUnable to save file')

except:
    print('No .txt file or directory')



