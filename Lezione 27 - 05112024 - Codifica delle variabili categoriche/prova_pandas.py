import prova_pandas as pd

iris = pd.read_csv('iris.csv')
print(iris['species'])
print(iris.describe())

#media della serie length
media_length = iris['sepal_length'].mean()
print(media_length)

#somma della serie length
sum_length = iris['sepal_length'].sum()
print(sum_length)

unico_length = iris['sepal_length'].unique()
print(unico_length)