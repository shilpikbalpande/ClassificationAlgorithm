import itertools
import inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier

teleCust1000tFile = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/drug200.csv'

my_data = pd.read_csv(teleCust1000tFile)

# print(my_data.size)

X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values



from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1])

# print(X[:,1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3])

X[0:5]

y = my_data["Drug"]
y[0:5]

from sklearn.model_selection import train_test_split

X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)


drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
# print(drugTree)


drugTree.fit(X_trainset,y_trainset)

predTree = drugTree.predict(X_testset)


# print (predTree [0:5])
# print (y_testset [0:5])


from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree

# dot_data = StringIO()
# filename = "drugtree.png"
# featureNames = my_data.columns[0:5]
# targetNames = my_data["Drug"].unique().tolist()
# out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# # graph.write_png(filename)
# # img = mpimg.imread(filename)
# plt.figure(figsize=(100, 200))
# plt.imshow(interpolation='nearest')
#
