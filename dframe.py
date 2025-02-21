import pandas as pd
data={"Name" : ["abc","def","ghi"],
      "Age" : [25,26,27],
      "Stipend" : [80000,90000,98000]
      }
df=pd.DataFrame(data)
print(df)