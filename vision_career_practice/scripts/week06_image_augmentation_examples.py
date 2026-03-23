from pathlib import Path
import cv2
import numpy as np

src = sorted(Path('data/raw').glob('*.jpg'))[0]
img = cv2.imread(str(src))
out_dir = Path('data/processed')
out_dir.mkdir(parents=True, exist_ok=True)

# 밝기 증가
bright = cv2.convertScaleAbs(img, alpha=1.0, beta=40)
cv2.imwrite(str(out_dir / 'bright_example.jpg'), bright)

# 블러
blur = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imwrite(str(out_dir / 'blur_example.jpg'), blur)

# 노이즈
noise = np.random.normal(0, 12, img.shape).astype(np.int16)
noisy = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
cv2.imwrite(str(out_dir / 'noisy_example.jpg'), noisy)

print('증강 예제 저장 완료:', out_dir)
