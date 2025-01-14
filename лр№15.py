import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Створення початкового словника
students = {
    "Іванов": {"зріст": 185, "клас": "11-А", "стать": "Ч", "середній_бал": 10.5},
    "Петров": {"зріст": 182, "клас": "11-А", "стать": "Ч", "середній_бал": 9.8},
    "Сидоров": {"зріст": 178, "клас": "11-Б", "стать": "Ч", "середній_бал": 8.9},
    "Коваленко": {"зріст": 175, "клас": "11-Б", "стать": "Ч", "середній_бал": 11.2},
    "Шевченко": {"зріст": 172, "клас": "11-А", "стать": "Ж", "середній_бал": 10.1},
    "Бондаренко": {"зріст": 170, "клас": "11-А", "стать": "Ж", "середній_бал": 9.5},
    "Мельник": {"зріст": 168, "клас": "11-Б", "стать": "Ж", "середній_бал": 10.8},
    "Павленко": {"зріст": 165, "клас": "11-Б", "стать": "Ч", "середній_бал": 9.2},
    "Ткаченко": {"зріст": 162, "клас": "11-А", "стать": "Ж", "середній_бал": 11.5},
    "Кравченко": {"зріст": 160, "клас": "11-Б", "стать": "Ж", "середній_бал": 10.3}
}

# Створення DataFrame
df = pd.DataFrame.from_dict(students, orient='index')

def analyze_students_data():
    print("\nПочатковий датафрейм:")
    print(df)
    
    # Групування за класами
    print("\nСередній зріст по класах:")
    class_height = df.groupby('клас')['зріст'].mean()
    print(class_height)
    
    # Групування за статтю
    print("\nСтатистика по статі:")
    gender_stats = df.groupby('стать').agg({
        'зріст': ['mean', 'min', 'max'],
        'середній_бал': 'mean'
    })
    print(gender_stats)
    
    # Комплексний аналіз
    print("\nКількість учнів у кожному класі за статтю:")
    class_gender_count = pd.crosstab(df['клас'], df['стать'])
    print(class_gender_count)
    
    # Візуалізація даних
    plt.figure(figsize=(12, 4))
    
    # Графік середнього зросту по класах
    plt.subplot(131)
    class_height.plot(kind='bar')
    plt.title('Середній зріст по класах')
    plt.xlabel('Клас')
    plt.ylabel('Зріст (см)')
    
    # Графік розподілу за статтю
    plt.subplot(132)
    df['стать'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Розподіл за статтю')
    
    # Графік середнього балу по класах
    plt.subplot(133)
    df.groupby('клас')['середній_бал'].mean().plot(kind='bar')
    plt.title('Середній бал по класах')
    plt.xlabel('Клас')
    plt.ylabel('Середній бал')
    
    plt.tight_layout()
    plt.show()

analyze_students_data()