import pandas as pd
data=pd.read_excel("excell.xlsx")
# # read upper 5
# print(data.head(5))
# # read lower 5
# print(data.tail(5))

# # give info
# print(data.info())

# # describe: mean count max etc
# print(data.describe())

# #  which is null
# print(data.isnull())


# #  which is null
# print(data.isnull().sum())

# is dublicate?
print(data.duplicated())

# how many dublicate?
print(data.duplicated().sum())
