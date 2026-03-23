import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv('data/metadata.csv')
out_dir = Path('data')

for col in ['lighting', 'camera_id', 'defect_type']:
    counts = df[col].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind='bar')
    plt.title(f'{col} distribution')
    plt.ylabel('count')
    plt.tight_layout()
    save_path = out_dir / f'{col}_distribution.png'
    plt.savefig(save_path)
    plt.close()
    print('saved:', save_path)
