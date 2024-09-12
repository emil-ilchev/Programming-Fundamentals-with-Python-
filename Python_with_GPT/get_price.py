import requests
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import time
import csv

# URL на уебсайта
url = "https://www.porssisahkoa.fi/"


# Функция за записване на данни в CSV файл
def save_to_csv(timestamp, current_price):
    with open("C:\\Users\\emili\\OneDrive\\Desktop\\electricity_prices.csv", 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, current_price])
        print("Цената беше записана в CSV файла")


# Функция за извличане и записване на текущата цена
def fetch_and_save_price():
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.select_one(
            "body > div:nth-of-type(1) > div:nth-of-type(2) > main > div:nth-of-type(3) > div > div:nth-of-type(2)")

        if element:
            current_price = element.get_text(strip=True)
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            save_to_csv(timestamp, current_price)
        else:
            print("Елементът за текущата цена не е намерен.")
    except requests.exceptions.RequestException as e:
        print(f"Проблем с мрежата: {e}")
    except Exception as e:
        print(f"Възникна грешка: {e}")


# Планиране на задачата за изпълнение на всеки кръгъл час
schedule.every().hour.at(":00").do(fetch_and_save_price)

print("Скриптът започна. Натиснете Ctrl+C за да го прекратите.")

# Запазване на скрипта да работи постоянно
while True:
    schedule.run_pending()
    time.sleep(1)
