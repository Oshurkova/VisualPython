import matplotlib.pyplot as plt

regions = ['Новая Англия', 'Северо-восток', 'Средний Запад']
sales = [882703, 532648, 714406]
plt.pie(sales, labels=regions, autopct='%1.1f%%')
plt.title('Продажи по регионам')
plt.show()