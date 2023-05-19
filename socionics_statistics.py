import pandas as pd

# Припустимо, що ми зібрали дані від 15 анонімних респондентів і отримали їх типи за методом експерта та новим методом
respondent_ids = range(1, 16) # респонденти від 1 до 15
expert_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ', 'ISFP', 'ESTJ', 'INFP', 'ESFP', 'INTP', 'ENTP', 'ISFJ', 'ESTP', 'INFJ', 'ENFJ']
new_method_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ', 'ISFP', 'ESTJ', 'INFP', 'ESFP', 'INTP', 'ENTP', 'ISFJ', 'ESTP', 'INFJ', 'ENFJ']

# Створимо DataFrame
df = pd.DataFrame({
    'respondent_id': respondent_ids,
    'expert_type': expert_types,
    'new_method_type': new_method_types
})

# Збережемо DataFrame в csv-файл
df.to_csv('types.csv', index=False)
