import pandas as pd
from sklearn.metrics import accuracy_score, recall_score

df = pd.read_csv('data/metadata.csv').copy()

# 예시용 가짜 예측
pred = []
for _, row in df.iterrows():
    if row['quality_status'] == 'NG' and row['lighting'] == 'dim':
        pred.append('OK')
    elif row['quality_status'] == 'NG' and row['camera_id'] == 'camB':
        pred.append('OK')
    else:
        pred.append(row['quality_status'])

df['pred_quality'] = pred

print('--- lighting별 성능 ---')
for lighting, g in df.groupby('lighting'):
    acc = accuracy_score(g['quality_status'], g['pred_quality'])
    ng_true = (g['quality_status'] == 'NG').astype(int)
    ng_pred = (g['pred_quality'] == 'NG').astype(int)
    rec = recall_score(ng_true, ng_pred, zero_division=0)
    print(lighting, {'accuracy': round(acc,3), 'ng_recall': round(rec,3), 'n': len(g)})

print('
--- camera별 성능 ---')
for cam, g in df.groupby('camera_id'):
    acc = accuracy_score(g['quality_status'], g['pred_quality'])
    ng_true = (g['quality_status'] == 'NG').astype(int)
    ng_pred = (g['pred_quality'] == 'NG').astype(int)
    rec = recall_score(ng_true, ng_pred, zero_division=0)
    print(cam, {'accuracy': round(acc,3), 'ng_recall': round(rec,3), 'n': len(g)})
