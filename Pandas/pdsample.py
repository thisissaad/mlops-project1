
import pandas as pd

mydata = [1, 2, 3]

myvar = pd.Series (mydata, index = ["x", "y", "z"])
print(myvar["x"])