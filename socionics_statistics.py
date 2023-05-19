import pandas as pd
from slang import slang

def read_csv(filename):
    return pd.read_csv(filename)

def analyze(df):
    df['is_match'] = df['expert_type'] == df['new_method_type']
    
    # Групування по школі
    school_group = df.groupby('socionics_school')['is_match'].mean() * 100
    print('Відсоток збігів по школах:\n', school_group)

    # Групування по типувальнику
    typist_group = df.groupby('типувальник')['is_match'].mean() * 100
    print('Відсоток збігів по типувальникам:\n', typist_group)


# Читаємо дані з файлів
celebrities_df = read_csv('знаменитості.csv')
socionics_schools_df = read_csv('школи_соціоніки.csv')
typing_methods_df = read_csv('методи_типування.csv')

# З'єднуємо дані за потрібними стовпцями
df = pd.merge(celebrities_df, socionics_schools_df, on='socionics_school', how='left')
df = pd.merge(df, typing_methods_df, on='typing_method', how='left')

# Аналізуємо дані
analyze(df)
