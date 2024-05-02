import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

unique_values = data['whoAmI'].unique() #задал список для названий столбцов в будущей one hot таблице

for value in unique_values:
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0) 
# если значение, взятое в whoAmI, равняется зачению из unique_values, 
# взятому как заголовок стоблца, то возвращается 1; если нет — 0. так форимруются данные в one hot виде.


data = data.drop('whoAmI', axis=1) # удаляю исходный столбец 'whoAmI'

print(data.head())