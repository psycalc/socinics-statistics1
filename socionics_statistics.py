import pandas as pd

# Припустимо, що ми зібрали дані від 15 українських знаменитостей і отримали їх типи за методом експерта та новим методом
respondent_ids = range(1, 16)  # ідентифікатори знаменитостей від 1 до 15
# full_names = ['Іван Петров', 'Марія Коваленко', 'Олександр Сидоров', 'Анна Василенко', 'Володимир Кравчук',
#               'Олена Шевченко', 'Ігор Литвиненко', 'Наталія Данилко', 'Максим Іванов', 'Олексій Левченко',
#               'Євгенія Тимошенко', 'Ірина Козлова', 'Василь Мороз', 'Ольга Соловей', 'Андрій Гречко']
full_names = ["Зеленський Володимир Олександрович", "Порошенко Петро Олексійович", "Ющенко Віктор Андрійович", "Кучма Леонід Данилович", "Кравчук Леонід Макарович"]
expert_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ', 'ISFP', 'ESTJ', 'INFP', 'ESFP', 'INTP',
                'ENTP', 'ISFJ', 'ESTP', 'INFJ', 'ENFJ']
new_method_types = ['INTJ', 'ENFP', 'ISTP', 'ESFJ', 'ENTJ', 'ISFP', 'ESTJ', 'INFP', 'ESFP', 'INTP',
                    'ENTP', 'ISFJ', 'ESTP', 'INFJ', 'ENFJ']

# Створимо DataFrame
df = pd.DataFrame({
    'respondent_id': respondent_ids,
    'full_name': full_names,
    'expert_type': expert_types,
    'new_method_type': new_method_types
})

# Збережемо DataFrame в csv-файл
df.to_csv('знаменитості.csv', index=False)