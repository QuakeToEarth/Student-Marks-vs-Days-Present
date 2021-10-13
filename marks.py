import pandas as pd
import numpy as np
import plotly.express as pe
df = pd.read_csv('Student Marks vs Days Present.csv')
mk = df['Marks In Percentage'].tolist()
dp = df['Days Present'].tolist()
d = {'x':dp, 'y': mk}
coreRelation = np.corrcoef(d['x'], d['y'])
print(coreRelation)
graph = pe.scatter(df, x = 'Days Present', y = 'Marks In Percentage')
graph.show()