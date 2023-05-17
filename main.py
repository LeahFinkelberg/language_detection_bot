from os import getenv
from typing import Final

import telebot
from dotenv import load_dotenv

import handlers


def setup_bot(bot: telebot.TeleBot) -> None:
    bot.register_message_handler(
        handlers.start,  # путь к функции-обработчику
        pass_bot=True,  # передать обработчику объект бота
        commands=["start"],  # список команд для обработки

    )  # Регистрирует обработчик для команды /start
    bot.register_message_handler(
        handlers.detect,
        pass_bot=True,
    )


def main():
    load_dotenv()  # Загружает переменные окружения из файла .env
    token: Final[str] = getenv("TOKEN")  # Получает значение переменной окружения TOKEN
    bot = telebot.TeleBot(token=token, parse_mode="html")  # Создаёт бота с токеном token
    setup_bot(bot)  # Настройка бота
    bot.infinity_polling()  # Запуск бота


if __name__ == '__main__':  # Если этот файл запущен (не импортирован)
    main()  # запустить основную функцию
