# Импортируем все необходимые библиотеки
import asyncio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Генерация данных о погоде (одинаковая для всех методов)
def generate_temperature_data():

    dates = pd.date_range(start = '2013-01-01', end = '2023-12-31', freq = 'D')
    temperatures = np.random.normal(loc = 15, scale = 10, size = len(dates))  # Средняя температура

    return pd.DataFrame({'Date': dates, 'Temperature': temperatures})

data = generate_temperature_data()

# 1.Реализация с использованием asyncio

async def plot_async(data):

    await asyncio.sleep(1)  # Эмуляция асинхронной работы

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Temperature'], label='Async Temperature', color='blue')
    plt.title('Average Temperature (Async)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.show()

# Запуск
def main():
    asyncio.run(plot_async(data))

if __name__ == "__main__":
    main()








