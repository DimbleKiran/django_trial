import pandas as pd

df = pd.read_json('http://127.0.0.1:8000/students/api/mechanical/')
print(df)
