import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve, PrecisionRecallDisplay

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_scores = model.predict_proba(X_test)[:, 1]

precision, recall = precision_recall_curve(y_test, y_scores)

display = PrecisionRecallDisplay(precision=precision, recall=recall)
display.plot()
plt.title('Precision-Recall кривая для модели Random Forest')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()