import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..


af == "C:\Users\vashista\OneDrive\python\tutorial.csv"
df=pd.read_csv(af)
print(df)


# TODO: Print the results of the .describe() method
#
# .. your code here ..
df.describe()


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print(df.ix[2:4,'clo3'])
