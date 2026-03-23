# Vision Career Practice Pack

이 패키지는 제조 비전 데이터 직무 준비용 실습 자료입니다.

## 폴더 구성
- `data/raw`: 예제 이미지
- `data/metadata.csv`: 정상 메타데이터
- `data/metadata_with_issues.csv`: 누락/중복/파일불일치 예시 포함
- `scripts`: 주차별 실습 코드

## 설치
```bash
pip install pandas opencv-python matplotlib scikit-learn pillow
```

## 실행 예시
```bash
python scripts/week01_file_listing.py
python scripts/week02_pandas_summary.py
python scripts/week04_data_validation.py
```

## 추천 학습 방식
매주 아래 3가지를 남기세요.
1. 배운 개념
2. 발견한 데이터 문제
3. 실무라면 어떻게 확장할지
