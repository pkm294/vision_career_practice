import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('data/metadata.csv').copy()

# 예시용 가짜 예측: dim 조명에서 일부 NG를 놓치도록 설정
pred = []
for _, row in df.iterrows():
    if row['quality_status'] == 'NG' and row['lighting'] == 'dim':
        pred.append('OK')
    else:
        pred.append(row['quality_status'])

df['pred_quality'] = pred
print('Confusion matrix')
print(confusion_matrix(df['quality_status'], df['pred_quality'], labels=['OK','NG']))
print('
Classification report')
print(classification_report(df['quality_status'], df['pred_quality'], labels=['OK','NG']))
