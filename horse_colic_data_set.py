# -*- coding: utf-8 -*-
"""Horse_Colic_Data_Set.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WEBf073iV05l0hogkFfu7nIPv3OUEV2F
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# from sklearn.preprocessing import Imputer
# imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

import warnings
warnings.filterwarnings('ignore')

horse_data = pd.read_csv('../DataSets/horse.csv')
horse_data.head()

horse_data.info()

horse_data.dropna(axis = 1, thresh=250, inplace = True)
horse_data.info()

horse_data.head()

for column in list(horse_data.columns):
    if(horse_data[column].dtype not in ['object']):
        horse_data[column].fillna(horse_data[column].median(), inplace=True)
    else:
        horse_data[column].fillna(horse_data[column].mode()[0], inplace=True)

horse_data.info()

horse_data.head()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
for column in list(horse_data.columns):
    if(horse_data[column].dtype not in ['object']):
        horse_data[column] = scaler.fit_transform(horse_data[[column]])
horse_data.head()

for column in list(horse_data.columns):
    if(horse_data[column].dtype in ['object']):
        print(horse_data[column].unique())

# Outlier removal

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
for column in list(horse_data.columns):
    if(horse_data[column].dtype in ['object']):
        horse_data[column] = encoder.fit_transform(horse_data[[column]])
horse_data.head()

feature_data = horse_data.copy()
feature_data.drop(columns=['outcome'], inplace=True)
target_data = pd.DataFrame(horse_data['outcome'])
target_data.info()

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA()
lda_data = lda.fit_transform(feature_data, target_data)

lda_data

X = lda_data.copy()
y = target_data.copy()

for model in models:
    print(model)
    model_score_train=[]
    model_score_test=[]
    for i,(train,value) in enumerate(k_fold.split(X, y)):
        model.fit(X[train],y.iloc[train])
        pred=model.predict(X[value])
        model_score_train.append(model.score(X[train],y.iloc[train]))
        model_score_test.append(model.score(X[value],y.iloc[value]))
        print(model.score(X[train],y.iloc[train]),model.score(X[value],y.iloc[value]))
    print('\n\n\n')
    print(sum(model_score_train)/len(model_score_train), sum(model_score_test)/len(model_score_test))
    print('\n\n\n')

from sklearn.decomposition import PCA

pca = PCA(0.95)
pca_data = pca.fit_transform(feature_data, target_data)
pca.explained_variance_ratio_

pca_data.shape

from sklearn.feature_selection import RFE

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Model building
logistic_regression = LogisticRegression()
knn = KNeighborsClassifier()
decision_tree = DecisionTreeClassifier()
svm = SVC()
models = [logistic_regression, knn, decision_tree, svm]

from sklearn.model_selection import KFold

k_fold = KFold(n_splits=5,shuffle=False,random_state=40)

X = feature_data.copy()
y = target_data.copy()

for model in models:
    print(model)
    model_score_train=[]
    model_score_test=[]
    for i,(train,value) in enumerate(k_fold.split(X, y)):
        model.fit(X.iloc[train],y.iloc[train])
        pred=model.predict(X.iloc[value])
        model_score_train.append(model.score(X.iloc[train],y.iloc[train]))
        model_score_test.append(model.score(X.iloc[value],y.iloc[value]))
        print(model.score(X.iloc[train],y.iloc[train]),model.score(X.iloc[value],y.iloc[value]))
    print('\n\n\n')
    print("Train data score:", sum(model_score_train)/len(model_score_train), "Test data score:", sum(model_score_test)/len(model_score_test))
    print('\n\n\n')

horse_data.groupby(by='outcome').count()

X = pca_data.copy()
y = target_data.copy()

for model in models:
    print(model)
    model_score_train=[]
    model_score_test=[]
    for i,(train,value) in enumerate(k_fold.split(X, y)):
        model.fit(X[train],y.iloc[train])
        pred=model.predict(X[value])
        model_score_train.append(model.score(X[train],y.iloc[train]))
        model_score_test.append(model.score(X[value],y.iloc[value]))
        print(model.score(X[train],y.iloc[train]),model.score(X[value],y.iloc[value]))
    print('\n\n\n')
    print(sum(model_score_train)/len(model_score_train), sum(model_score_test)/len(model_score_test))
    print('\n\n\n')

from sklearn.feature_selection import RFE

X = feature_data.copy()
y = target_data.copy()

selector_log_reg = RFE(logistic_regression, 7)
selector_log_reg = selector_log_reg.fit(X, y)
selector_log_reg.support_

selector_dec_tree = RFE(decision_tree, 7)
selector_dec_tree = selector_dec_tree.fit(X, y)
selector_dec_tree.support_

feature_data.columns

# 2,4,6,8,9,10,12
X_log_reg = feature_data[['age', 'pulse', 'capillary_refill_time', 'packed_cell_volume', 'total_protein', 'surgical_lesion', 'lesion_2']]

# 3,4,5,7,8,9,11
X_dec_tree = feature_data[['hospital_number', 'pulse', 'mucous_membrane', 'peristalsis', 'packed_cell_volume', 'total_protein', 'lesion_1']]

model_score_train=[]
model_score_test=[]
model = logistic_regression
print(model)
X = X_log_reg
for i,(train,value) in enumerate(k_fold.split(X, y)):
    model.fit(X.iloc[train],y.iloc[train])
    pred=model.predict(X.iloc[value])
    model_score_train.append(model.score(X.iloc[train],y.iloc[train]))
    model_score_test.append(model.score(X.iloc[value],y.iloc[value]))
    print(model.score(X.iloc[train],y.iloc[train]),model.score(X.iloc[value],y.iloc[value]))
print('\n\n\n')
print(sum(model_score_train)/len(model_score_train), sum(model_score_test)/len(model_score_test))
print('\n\n\n')

model_score_train=[]
model_score_test=[]
model = decision_tree
print(model)
X = X_dec_tree
for i,(train,value) in enumerate(k_fold.split(X, y)):
    model.fit(X.iloc[train],y.iloc[train])
    pred=model.predict(X.iloc[value])
    model_score_train.append(model.score(X.iloc[train],y.iloc[train]))
    model_score_test.append(model.score(X.iloc[value],y.iloc[value]))
    print(model.score(X.iloc[train],y.iloc[train]),model.score(X.iloc[value],y.iloc[value]))
print('\n\n\n')
print(sum(model_score_train)/len(model_score_train), sum(model_score_test)/len(model_score_test))
print('\n\n\n')

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X_dec_tree,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(n_estimators=20)
random_forest.fit(X_train, y_train)
random_forest.score(X_test, y_test)

X = feature_data.copy()
y = target_data.copy()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

random_forest = RandomForestClassifier(n_estimators=20)
random_forest.fit(X_train, y_train)
random_forest.score(X_test, y_test)

random_forest = RandomForestClassifier(n_estimators=20)
random_forest.fit(X_train, y_train)
random_forest.score(X_test, y_test)

from sklearn.ensemble import AdaBoostClassifier

X_train,X_test,y_train,y_test=train_test_split(pca_data,y,test_size=0.2,random_state=42)

for model in [logistic_regression, decision_tree]:
    ada_boost = AdaBoostClassifier(base_estimator=model)
    ada_boost.fit(X_train, y_train)
    print(ada_boost.score(X_test, y_test))

X_train,X_test,y_train,y_test=train_test_split(lda_data,y,test_size=0.2,random_state=42)

for model in [logistic_regression, decision_tree]:
    ada_boost = AdaBoostClassifier(base_estimator=model)
    ada_boost.fit(X_train, y_train)
    print(ada_boost.score(X_test, y_test))