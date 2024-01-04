import numpy as np
print(np.ones((5,5),dtype=int))
k=np.empty((5,5),dtype=int)
print(k)
import numpy as np
k=np.linspace(2,20,2)
print(k)
import pandas as pd
import numpy as np
pl=pd.DataFrame({"name":["ram","shyam","hari","priyanka","pratik","suvam","bibash","padam","amod","smith","subodh","roshan","sujal","manish","mod","nischal","rocky","sushant","shirish","pappu"],"age":[12,35,34,67,53,24,29,30,43,28,56,12,17,27,35,42,33,39,42,23],"salary":[35000,45000,47000,16000,23000,26000,28000,25000,10000,19000,67000,56000,46000,49000,34000,39000,49000,78000,77000,97000]})
pl.to_csv("clu.csv")
d.read_csv("clu.csv")
pm
