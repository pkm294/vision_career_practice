from pathlib import Path
import cv2


BASE_DIR = Path(__file__).resolve().parent.parent

# raw_dir = Path('../data/raw')

raw_dir = BASE_DIR / 'data' / 'raw'
src_dir= BASE_DIR / 'data' / 'raw'



# src_dir = Path('data/raw')
# out_dir = Path('data/processed/resized_128')
out_dir.mkdir(parents=True, exist_ok=True)

for p in src_dir.glob('*.jpg'):
    img = cv2.imread(str(p))
    if img is None:
        print('읽기 실패:', p.name)
        continue
    resized = cv2.resize(img, (128, 128))
    cv2.imwrite(str(out_dir / p.name), resized)

print('저장 완료:', out_dir)
