import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. Загрузка данных
goog_data = pd.read_csv('GOOG.csv', parse_dates=['Date'])
icecream_data = pd.read_csv('icecreamsales.csv')

# 2. Построение диаграмм
# Диаграмма 1: Зависимость цены закрытия акций Google от объема торгов
plt.figure(figsize=(10, 6))
plt.scatter(goog_data['Volume'], goog_data['Close'], alpha=0.6, c='blue', label='Close Price')
plt.title('Зависимость цены закрытия акций Google от объема торгов', fontsize=14)
plt.xlabel('Объем торгов', fontsize=12)
plt.ylabel('Цена закрытия', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('scatter_volume_close.png')
plt.close()

# Диаграмма 2: Линейный график цен на акции Google
plt.figure(figsize=(12, 6))
plt.plot(goog_data['Date'], goog_data['Close'], label='Цена закрытия', color='green')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gcf().autofmt_xdate()
plt.title('Тренд цен акций Google', fontsize=14)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Цена закрытия', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('line_trend_google.png')
plt.close()

# Диаграмма 3: Зависимость продаж мороженого от температуры
plt.figure(figsize=(10, 6))
plt.scatter(icecream_data['Temperature'], icecream_data['Sales'], c=icecream_data['Sales'], cmap='coolwarm', s=100)
plt.colorbar(label='Объем продаж')
plt.title('Зависимость продаж мороженого от температуры', fontsize=14)
plt.xlabel('Температура (°C)', fontsize=12)
plt.ylabel('Продажи', fontsize=12)
plt.grid(alpha=0.3)
plt.savefig('scatter_temperature_sales.png')
plt.close()

print("Диаграммы успешно созданы и сохранены как изображения.")
