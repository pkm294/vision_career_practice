import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('data/metadata.csv')
X = df[['camera_id','angle','lighting','product_type']]
y = df['quality_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

preprocess = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['camera_id','angle','lighting','product_type'])
])

model = Pipeline([
    ('prep', preprocess),
    ('clf', DecisionTreeClassifier(max_depth=3, random_state=42))
])

model.fit(X_train, y_train)
pred = model.predict(X_test)
print(classification_report(y_test, pred))
