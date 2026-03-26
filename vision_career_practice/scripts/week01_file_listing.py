from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

# raw_dir = Path('../data/raw')
raw_dir = BASE_DIR / 'data' / 'raw'
image_paths = sorted(raw_dir.glob('*.jpg'))
print(f'총 이미지 수: {len(image_paths)}')

records = []
for p in image_paths:
    # 예시 파일명: L1_camA_front_bright_OK_IMG_0001.jpg
    parts = p.stem.split('_')
    if len(parts) < 7:
        print(f'규칙 위반 파일명: {p.name}')
        continue
    line_no, camera_id, angle, lighting, quality_status = parts[0], parts[1], parts[2], parts[3], parts[4]
    image_id = '_'.join(parts[5:])
    records.append({
        'file_name': p.name,
        'line_no': line_no,
        'camera_id': camera_id,
        'angle': angle,
        'lighting': lighting,
        'quality_status': quality_status,
        'image_id': image_id,
    })

df = pd.DataFrame(records)
print(df.head())
print('조명별 개수')
print(df['lighting'].value_counts())
