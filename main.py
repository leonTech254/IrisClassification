import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("./iris.csv")

print(iris.shape)

print(iris.columns)

#displaying the number of flowers present for a specific species

noOfFlowers=iris['variety'].value_counts()

print(noOfFlowers)

# ploting a graph
iris.plot(kind='scatter',x='sepal.length',y='sepal.width')
# plt.show()


sns.set_style("whitegrid")
sns.FacetGrid(iris,hue='variety')\
.map(plt.scatter,"sepal.length","sepal.width")\
    .add_legend();
plt.show()



