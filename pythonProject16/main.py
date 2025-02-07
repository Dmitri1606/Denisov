import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('Книга 3 (1).xlsx')

# Посмотреть первые 5 строк
print(df_excel.head(5))

# Посмотреть последние 5 строк
print(df_excel.tail(5))

# Посмотреть рандомные 5 строк
print(df_excel.sample(n=5))

