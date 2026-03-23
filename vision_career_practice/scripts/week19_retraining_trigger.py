baseline = {
    'overall_accuracy': 0.95,
    'ng_recall': 0.92,
    'dim_lighting_ng_recall': 0.88,
}

current = {
    'overall_accuracy': 0.93,
    'ng_recall': 0.84,
    'dim_lighting_ng_recall': 0.60,
}

rules = []
if current['overall_accuracy'] < baseline['overall_accuracy'] - 0.02:
    rules.append('전체 정확도 2%p 이상 하락')
if current['ng_recall'] < baseline['ng_recall'] - 0.05:
    rules.append('불량 재현율 5%p 이상 하락')
if current['dim_lighting_ng_recall'] < 0.75:
    rules.append('dim 조명 조건에서 불량 재현율 임계값 미만')

print('재학습 필요 여부:', 'YES' if rules else 'NO')
print('사유:')
for r in rules:
    print('-', r)
