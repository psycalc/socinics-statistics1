import pandas as pd

df = pd.read_csv('types.csv')
df['is_match'] = df['expert_type'] == df['new_method_type']

match_percentage = df['is_match'].sum() / len(df) * 100
print(f'Відсоток збігів: {match_percentage}%')
