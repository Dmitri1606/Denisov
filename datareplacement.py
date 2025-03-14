import pandas as pd
df_excel = pd.read_excel('Книга 3.xlsx')
print(df_excel)

f=int(input("ведите значение координат по вертикали начиная с 0:"))
y=int(input("ведите значение координат по горизонтали начиная с 0:"))
e=str(input("Ведите на что хотите заменить значение:"))
# Чтение Excel-файла




value = df_excel.iloc[0, 3]
print(value)

a=df_excel.iat[f, y] = e

print(a)
print(df_excel)