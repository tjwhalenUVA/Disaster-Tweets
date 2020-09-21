# Prior to running you need to unzip the data files in the data folder
import pandas as pd
import os

data_dir = 'C:/Users/Jake/Documents/Projects/Disasters/data'
data_dfs = {}

for f in os.listdir(data_dir):
    name, ext = os.path.splitext(f)
    if ext == '.csv':
        print(name)
        data_dfs[name] = pd.read_csv(os.path.join(data_dir, f))
        data_dfs[name].columns = [c.lower() for c in data_dfs[name].columns] #postgres doesn't like capitals or spaces
        print(data_dfs[name].columns)
        print(data_dfs[name].shape)

print('Creating tables in DB')
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:890*()iop@localhost:5432/disaster')
for key, value in data_dfs.items():
    print(key)
    value.to_sql(key, engine)
