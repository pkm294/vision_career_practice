from pathlib import Path
import pandas as pd

df = pd.read_csv('data/metadata_with_issues.csv')
raw_dir = Path('data/raw')

print('--- 누락값 검사 ---')
print(df[['quality_status','defect_type']].isna().sum())
print((df[['quality_status','defect_type']] == '').sum())

print('
--- 중복 파일명 검사 ---')
dup = df[df['file_name'].duplicated(keep=False)].sort_values('file_name')
print(dup[['image_id','file_name']])

print('
--- 실제 파일 존재 여부 ---')
df['file_exists'] = df['file_name'].apply(lambda x: (raw_dir / x).exists())
print(df['file_exists'].value_counts())
print(df.loc[~df['file_exists'], ['image_id','file_name']])

print('
--- 파일명 규칙 검사 ---')
def valid_name(name: str) -> bool:
    stem = Path(name).stem
    parts = stem.split('_')
    return len(parts) >= 7

bad = df[~df['file_name'].apply(valid_name)]
print(bad[['image_id','file_name']])
