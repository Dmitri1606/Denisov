import pandas as pd
#
#
# # Чтение Excel-файла
df_excel = pd.read_excel('Книга 3 (1).xlsx')
#
 # Посмотреть первые 5 строк
print(df_excel.head(5))

# Посмотреть последние 5 строк
print(df_excel.tail(5))

# Посмотреть рандомные 5 строк
print(df_excel.sample(n=5))

# Посмотреть одну строку
print(df_excel.iloc[:, 1])

# Посмотреть её среднее значение
average_value = df_excel.iloc[:, 1].mean()
print(average_value)



