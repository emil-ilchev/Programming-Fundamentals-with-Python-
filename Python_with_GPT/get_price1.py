import requests
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import time

# URL на уебсайта
url = "https://www.porssisahkoa.fi/"


def fetch_and_save_price():
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
            current_price = element.get_text(strip=True)
            print(f"Текущата цена на електроенергията е: {current_price}")

            # Получаване на текущата дата и час
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            # Записване на датата, часа и текущата цена в текстов файл
            with open("C:\\Users\\emili\\Desktop\\price.txt", 'a', encoding='utf-8') as file:
                file.write(f'{timestamp} - {current_price}\n')
                print("Цената беше записана")
        else:
            print("Елементът за текущата цена не е намерен.")
    except Exception as e:
        print(f"Възникна грешка: {e}")


# Планиране на задачата за изпълнение на всеки кръгъл час
schedule.every().hour.at(":00").do(fetch_and_save_price)

print("Скриптът започна. Натиснете Ctrl+C за да го прекратите.")

# Запазване на скрипта да работи постоянно
while True:
    schedule.run_pending()
    time.sleep(1)
