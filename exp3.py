import matplotlib.pyplot as plt

regions = ['Новая Англия', 'Северо-восток', 'Средний Запад']
sales = [882703, 532648, 714406]
plt.bar(regions, sales)
plt.xlabel("Регионы")
plt.ylabel("Продажи")
plt.title("Годовой объем продаж по регионам")
plt.show()