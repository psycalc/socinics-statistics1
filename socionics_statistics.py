import pandas as pd
from slang import slang

def create_df(respondent_ids, full_names, expert_types, new_method_types, socionics_schools, typing_methods):
    return pd.DataFrame({
        'respondent_id': respondent_ids,
        'full_name': full_names,
        'expert_type': expert_types,
        'new_method_type': new_method_types,
        'socionics_school': socionics_schools,
        'typing_method': typing_methods
    })

full_names = ["Зеленський Володимир Олександрович", "Порошенко Петро Олексійович", "Ющенко Віктор Андрійович", "Кучма Леонід Данилович", "Кравчук Леонід Макарович"]
respondent_ids = range(1, len(full_names) + 1)
expert_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ']
new_method_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ']
socionics_schools = ['Школа 1', 'Школа 2', 'Школа 3', 'Школа 4', 'Школа 5']
typing_methods = ['Метод 1', 'Метод 2', 'Метод 3', 'Метод 4', 'Метод 5']

df = create_df(respondent_ids, full_names, expert_types, new_method_types, socionics_schools, typing_methods)

# Створюємо DataFrame для шкіл соціоніки та їх методів типування
school_typing_methods = {
    'Школа 1': ['Метод 1', 'Метод 2'],
    'Школа 2': ['Метод 3', 'Метод 4'],
    'Школа 3': ['Метод 5', 'Метод 6'],
    'Школа 4': ['Метод 7', 'Метод 8'],
    'Школа 5': ['Метод 9', 'Метод 10']
}

schools_df = pd.DataFrame(list(school_typing_methods.items()), columns=['socionics_school', 'typing_methods'])

# З'єднуємо два DataFrame
df = pd.merge(df, schools_df, on='socionics_school', how='left')

df.to_csv('знаменитості.csv', index=False)
