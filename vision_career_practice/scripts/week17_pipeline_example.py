from pathlib import Path
import shutil
import pandas as pd

raw_dir = Path('data/raw')
processed_dir = Path('data/processed/pipeline_demo')
processed_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv('data/metadata.csv')

# 예시: approved 샘플만 복사
approved = df[df['review_status'] == 'approved']
for name in approved['file_name']:
    src = raw_dir / name
    dst = processed_dir / name
    if src.exists():
        shutil.copy2(src, dst)

print('복사 완료 수:', len(list(processed_dir.glob('*.jpg'))))
print('저장 위치:', processed_dir)
