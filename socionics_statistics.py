# pandas
import pandas as pd
# Завантажуємо дані з файлів
celebrities_df = pd.read_csv('celebrities.csv')
schools_df = pd.read_csv('школи_соціоніки.csv')
typists_df = pd.read_csv('типувальники.csv')
methods_df = pd.read_csv('методи_типування.csv')

# Об'єднуємо дані
df = pd.concat([schools_df, typists_df])

# Аналізуємо збіги між експертами та новим методом
df['is_match'] = df['typed_type'].fillna('') == df['typing_method'].fillna('')

# Розраховуємо відсоток збігів за школами та типувальниками
school_match_percentages = df.groupby('socionics_school')['is_match'].mean() * 100
typist_match_percentages = df.groupby('typist')['is_match'].mean() * 100

print(f'Відсоток збігів по школах:\n{school_match_percentages}')
print(f'Відсоток збігів по типувальникам:\n{typist_match_percentages}')
