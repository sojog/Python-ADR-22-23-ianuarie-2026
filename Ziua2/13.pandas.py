import pandas as pd # alias conventional
import numpy as np

arr = np.array([11, 22, 33, 44])
serie1 = pd.Series(arr)

serie2 = pd.Series([88, 99, 111, 222])
df = pd.DataFrame({"coloana1": serie1, "coloana2": serie2})
print(df)