import requests
import time
from datetime import datetime
import pytz

# Ваші дані
BOT_TOKEN = '8182550137:AAEqkHikGqHcD9AqoVbm1YMtbvnXnDIWhnw'
CHAT_ID = '-1003099609244'  # Новий ID супергрупи


def send_message(chat_id, text):
    """
    Функція для відправки повідомлення
    """
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'  # Додаємо підтримку HTML форматування
        }
        response = requests.post(url, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Помилка відправки: {e}")
        return False


def send_morning_message():
    """
    Функція, яка відправляє повідомлення з посиланнями
    """
    morning_message = """
<b>Доброго ранку!</b> 

Заповніть будь ласка присутність працівників на об'єкті за цим посиланням:
🔗 <a href="https://forms.gle/uuGcZ5FWxSkbeF3D6">Форма присутності працівників</a>

І фото об'єкта за цим посиланням:
📸 <a href="https://forms.gle/JgCX9p1ujPo5q52t7">Форма фото об'єкта</a>

<code>Дякуємо за оперативність!</code>
"""

    try:
        success = send_message(CHAT_ID, morning_message)
        if success:
            current_time = datetime.now(pytz.timezone('Europe/Kiev')).strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Повідомлення успішно відправлено!")
            return True
        else:
            print("Не вдалося відправити повідомлення")
            return False
    except Exception as e:
        print(f"Загальна помилка: {e}")
        return False


def check_time_and_send():
    """
    Перевіряє час і відправляє повідомлення о 10:00
    """
    kiev_tz = pytz.timezone('Europe/Kiev')
    current_time = datetime.now(kiev_tz)

    print(f"Перевірка часу: {current_time.strftime('%H:%M:%S')}")

    # Для тестування - змініть на поточний час
    if current_time.hour == 10 and current_time.minute == 0:  # О 10:00 ранку
        print("Час співпав! Відправляю повідомлення...")
        send_morning_message()

    # Додаткова перевірка для демонстрації роботи
    if current_time.minute % 5 == 0:  # Кожні 5 хвилин для логування
        print(f"Бот працює. Наступна перевірка о 10:00")


def main():
    """
    Головна функція
    """
    print("=" * 60)
    print("🤖 Morning Bot запущено!")
    print("⏰ Час роботи: щодня о 10:00 за київським часом")
    print("📍 ID групи:", CHAT_ID)
    print("=" * 60)

    # Тестова відправка при запуску
    print("Відправляю тестове повідомлення...")
    test_message = "🤖 <b>Бот успішно запущений та працює!</b>\n✅ Готовий відправляти повідомлення щодня о 10:00"
    success = send_message(CHAT_ID, test_message)

    if success:
        print("✅ Тестове повідомлення успішно відправлено!")
        print("✅ Бот готовий до роботи!")
    else:
        print("❌ Помилка відправки тестового повідомлення")
        print("❌ Перевірте токен та ID чату")

    print("Для зупинки натисніть Ctrl+C")
    print("-" * 60)

    # Головний цикл
    while True:
        try:
            check_time_and_send()
            time.sleep(30)  # Перевіряємо кожні 30 секунд
        except KeyboardInterrupt:
            print("\n" + "=" * 60)
            print("🛑 Бот зупинено вручну!")
            print("=" * 60)
            break
        except Exception as e:
            print(f"❌ Помилка в головному циклі: {e}")
            time.sleep(60)


if __name__ == '__main__':
    main()