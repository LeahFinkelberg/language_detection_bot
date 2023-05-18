from telebot.types import Message
from telebot import TeleBot
import langdetect
from langdetect.language import Language
import iso639


def start(msg: Message, *, bot: TeleBot) -> None:
    bot.reply_to(msg, "/start used")


def detect(msg: Message, *, bot: TeleBot) -> None:
    guesses: list[Language] = langdetect.detect_langs(msg.text)  # Получает определенные langdetectом языки
    reply = ""
    for guess in guesses:
        code, prob = guess.lang, guess.prob
        lang = iso639.Language.from_part1(code)  # Получает язык по ISO 639-1 коду
        reply += "<b>{language}</b>: <code>{probability:.2%}</code>\n".format(
            language=lang.name,
            probability=prob,
        )
    bot.reply_to(
        msg,
        reply,
    )
