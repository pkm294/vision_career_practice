import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# raw_dir = Path('../data/raw')
raw_dir = BASE_DIR / 'data' / 'metadata.csv'
df = pd.read_csv(raw_dir)
print('전체 행 수:', len(df))
print('양품/불량 분포')
print(df['quality_status'].value_counts())
print('불량 유형 분포')
print(df['defect_type'].value_counts())
print('카메라별 x 품질 분포')
print(pd.crosstab(df['camera_id'], df['quality_status']))
print('조명별 x 품질 분포')
print(pd.crosstab(df['lighting'], df['quality_status']))
