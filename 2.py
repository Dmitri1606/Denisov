import pandas as pd
import matplotlib.pyplot as plt

# Шаг 1: Считываем данные из Excel
file_path = 'Книга 3 (1) (4).xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

# Проверяем структуру данных
mean_Clas = df['Clas'].mean()

a=len(df)
for i in  df['Clas']:
    res= i-mean_Clas
    cvad=res**2



total_sum = cvad.sum()

print(total_sum/a)