import pandas as pd
from slang import slang

full_names = ["Зеленський Володимир Олександрович", "Порошенко Петро Олексійович", "Ющенко Віктор Андрійович", "Кучма Леонід Данилович", "Кравчук Леонід Макарович"]

respondent_ids = range(1, len(full_names) + 1)
expert_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ']
new_method_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ']

df = pd.DataFrame({
    'respondent_id': respondent_ids,
    'full_name': full_names,
    'expert_type': expert_types,
    'new_method_type': new_method_types
})

df.to_csv('знаменитості.csv', index=False)
