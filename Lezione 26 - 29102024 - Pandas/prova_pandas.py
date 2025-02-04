import pandas as pd

iris = pd.read_csv('iris.csv')
#print(type(iris))

# print(iris.head(50)) #parte da sopra
# print(iris.tail(50)) #parte da sotto
'''deviazione standard scarto quadratico medio, curva di gaus'''
#print(iris.describe())
#print(iris.info())
#print(iris['petal_width'])
#print(type(iris['petal_width']))
#print(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

#features = iris['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

label = iris['species']
features = iris.drop(['species'], axis=1)
print(label)
print(features)

#print(iris.iloc[3:20:2])
