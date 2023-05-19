import pandas as pd

# Створимо DataFrame
df = pd.DataFrame({
    'expert_scores': [1, 2, 3, 4, 4, 2, 3, 1, 2, 4, 3, 1, 2, 3, 4],
    'new_method_scores': [1, 2, 3, 4, 4, 2, 3, 1, 2, 3, 3, 1, 2, 3, 4]
})

# Збережемо DataFrame в csv-файл
df.to_csv('scores.csv', index=False)