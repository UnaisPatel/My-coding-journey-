import seaborn as sns 


iris_df = sns.load_dataset("iris") 
print (iris_df.columns)

species = iris_df["species"]
print(species)

petal_info = iris_df[["sepal_length" , "sepal_width" , "petal_length" , "petal_width"]]
print (petal_info)

for flower in species:
    print(flower)


small_sepal_length = iris_df[iris_df["sepal_length"] < 4.5 ]
print(small_sepal_length)

mean_sepal_width = iris_df.groupby("species")["sepal_width"].mean()
print(mean_sepal_width)

import matplotlib.pyplot as plt

plt.figure()
sns.barplot(x="species" , y="sepal_width" , data = iris_df)
plt.show()