# Импортируем все необходимые библиотеки

import multiprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Генерация данных о погоде (одинаковая для всех методов)
def generate_temperature_data():

    dates = pd.date_range(start = '2013-01-01', end = '2023-12-31', freq = 'D')
    temperatures = np.random.normal(loc = 15, scale = 10, size = len(dates))  # Средняя температура

    return pd.DataFrame({'Date': dates, 'Temperature': temperatures})

#3. Реализация с использованием multiprocessing

def plot(data):

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Temperature'], label='Process Temperature', color='red')
    plt.title('Average Temperature (Process)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.show()

data = generate_temperature_data()

#Запуск асинхронной функции в основном потоке

if __name__ == "__main__":
    plot(data)



