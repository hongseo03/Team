import pandas as pd
import numpy as np

a=int(input())
data=np.random.randint(1,11,size=(a,a))
df = pd.DataFrame(data)

print (df)