import pandas as pd
import os
# mydata = {
#     "name": ["saad", "dash"],
#     "age": [23, 28]
# }

# df = pd.DataFrame(mydata, index= ["emp1", "emp2"])

base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, "Pandas",'data.csv')

df = pd.read_csv(data_path)
df2 = pd.DataFrame(df)

x = df2["Calories"].median()

df2.fillna({"Calories": x}, inplace=True)

data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir, 'sample.csv')

df2.to_csv(file_path, index=False)

print(f"Csv file saved to {file_path}")

# print(df.to_string())

# df2 = pd.DataFrame(df)
# print(df2)
# print(df2.tail())
# newdf = df.dropna()
# print(newdf.info())
# print(df.to_string())


# for x in df.index:
#     if df.loc[x, "Duration"] > 150:
#         df.loc[x, "Duration"] = 150

# print(df.to_string())        

# data_path.drop_duplicates(inplace=True)
# print(df.to_string)