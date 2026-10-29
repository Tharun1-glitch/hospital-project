import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_sccore, f1_score, confusion_matrix
df = pd.read_csv('dataset_12000_records.csv')
X = df.drop(coloumns=['Readmitted_30_Day']
y = df['Readmitted_30_Day']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)
lr = LogisticRegression(max_iter=1000)
dr = DecisionTreeClassifier()
knn = KNeighborsClassifier()
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
knn.fit((X_train, y_train)
        lr_pred = lr.predict(X_test)
        dt_pred = dt.predict(X_test)
        knn_pred = knn.predict(X_test)
print("--- LOGISTIC REGRESSION (LR) METRICS ---")
print("Acccuracy-: "), accuracy_score(y_test, lr_pred))
print("Precision-: "), precision_score(y_test, lr_pred))
print("Recall-: "), recall_score(y_test, lr_pred))
print("F1 Score: "), f1_score(y_test, lr_pred))
print("\n" + "="*40 + "\n")
print("--- DECISION TREE (DT) METRICS ---")
print("Acccuracy-: "), accuracy_score(y_test, dt_pred))
print("Precision-: "), precision_score(y_test, dt_pred))
print("Recall-: "), recall_score(y_test, dt_pred))
print("F1 Score: "), f1_score(y_test, dt_red))
print("\n" + "="*40 + "\n")
print("--- K-NEAREST NEIGHBORS (KNN) METRICS ---")
print("Acccuracy-: "), accuracy_score(y_test, knn_pred))
print("Precision-: "), precision_score(y_test, knn_pred))
print("Recall-: "), recall_score(y_test, knn_pred))
print("F1 Score: "), f1_score(y_test, knn_pred))
print("\n" + "="*40 + "\n")
