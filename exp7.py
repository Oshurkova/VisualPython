import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Год': [2010, 2011, 2012, 2013, 2014, 2015, 2016],
    'Продажи': [100, 150, 200, 250, 300, 350, 400]
}
df = pd.DataFrame(data)

df.plot(x='Год', y='Продажи', marker='s', color='skyblue', linestyle='-.')

plt.title('Динамика продаж по годам')
plt.xlabel('Год')
plt.ylabel('Продажи')

plt.grid(True)

plt.show()