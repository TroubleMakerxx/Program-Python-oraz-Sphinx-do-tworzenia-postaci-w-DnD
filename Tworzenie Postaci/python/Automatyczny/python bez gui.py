import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pydotplus
from sklearn import tree
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pd.read_csv("csv.csv", delimiter=';')

label_encoder = LabelEncoder()
df['wybierz_rase'] = label_encoder.fit_transform(df['wybierz_rase'])
df['wybierz_klase'] = label_encoder.fit_transform(df['wybierz_klase'])
df['postac'] = label_encoder.fit_transform(df['postac'])

features = ['wybierz_rase', 'wybierz_klase']
X = df[features]
y = df['postac']

dtree = DecisionTreeClassifier()
dtree.fit(X, y)

prediction = dtree.predict([[1, 5]])

predicted_character = label_encoder.inverse_transform(prediction)
print("Przewidywana postać:", predicted_character)

data = tree.export_graphviz(dtree, out_file=None, feature_names=features, class_names=label_encoder.inverse_transform(df['postac'].unique()))
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
