import requests
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import time

# URL на уебсайта
url = "https://www.porssisahkoa.fi/"

# ESP32/ESP8266 IP (замени с реалния IP адрес)
ESP_IP = "http://192.168.68.61"  # Примерен адрес

def fetch_and_control():
    try:
        # Изпращане на GET заявка към уебсайта
        response = requests.get(url)
        response.raise_for_status()  # Проверка дали заявката е успешна

        # Парсване на HTML съдържанието на страницата
        soup = BeautifulSoup(response.content, 'html.parser')

        # Намиране на елемента чрез CSS селектор
        element = soup.select_one("body > div:nth-of-type(1) > div:nth-of-type(2) > main > div:nth-of-type(3) > div > div:nth-of-type(2)")

        # Проверка дали е намерен елементът и извличане на текста му
        if element:
            current_price = element.get_text(strip=True).replace(',', '.')
            current_price = float(current_price)  # Превръщане в число
            print(f"Текущата цена на електроенергията е: {current_price} цента")

            # Получаване на текущата дата и час
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            # Записване на цената в текстов файл
            with open("C:\\Users\\emili\\OneDrive\\Desktop\\price.txt", 'a', encoding='utf-8') as file:
                file.write(f'{timestamp} - {current_price} цента\n')

            # Управление на ESP32/ESP8266
            if current_price < 5:
                print("Цената е под 5 цента! Включване на релето...")
                requests.get(f"{ESP_IP}/relay/on")
            else:
                print("Цената е над 5 цента. Изключване на релето...")
                requests.get(f"{ESP_IP}/relay/off")

        else:
            print("Елементът за текущата цена не е намерен.")

    except Exception as e:
        print(f"Възникна грешка: {e}")

# Планиране на задачата за изпълнение на всеки 5 минути
schedule.every(5).minutes.do(fetch_and_control)

print("Скриптът стартира. Натиснете Ctrl+C за спиране.")

while True:
    schedule.run_pending()
    time.sleep(1)
