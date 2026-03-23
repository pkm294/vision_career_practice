import pandas as pd
from pathlib import Path

df = pd.read_csv('data/metadata_with_issues.csv')
raw_dir = Path('data/raw')

# 빈 문자열을 결측으로 통일
for col in ['quality_status', 'defect_type']:
    df[col] = df[col].replace('', pd.NA)

# 중복 파일 제거
before = len(df)
df = df.drop_duplicates(subset=['file_name'], keep='first').copy()
print('중복 제거 수:', before - len(df))

# 메타 누락 제거
before = len(df)
df = df.dropna(subset=['quality_status', 'defect_type']).copy()
print('누락 제거 수:', before - len(df))

# 실제 파일 있는 것만 유지
before = len(df)
df = df[df['file_name'].apply(lambda x: (raw_dir / x).exists())].copy()
print('없는 파일 제거 수:', before - len(df))

# 간단한 이름 규칙 체크
before = len(df)
df = df[df['file_name'].apply(lambda x: len(Path(x).stem.split('_')) >= 7)].copy()
print('이름 규칙 위반 제거 수:', before - len(df))

save_path = 'data/clean_metadata.csv'
df.to_csv(save_path, index=False)
print('저장 완료:', save_path)
print('최종 행 수:', len(df))
