from telebot.types import Message
from telebot import TeleBot
import langdetect
from langdetect.language import Language
import iso639
import detect_artificial


def start(msg: Message, *, bot: TeleBot) -> None:
    bot.reply_to(
        msg, "/start used\n"
    )


def detect(msg: Message, *, bot: TeleBot) -> None:
    reference_message_set = detect_artificial.prepare_message(msg)
    files_list =  ["Qwenya_words.txt",
                   "Sindarin_words.txt",
                   "Hen_llinge_words.txt",
                   "Volapuek_words.txt.",
                   "Na'vi_words.txt"]
    isartif = 0
    for file in files_list:
        reference_file_set = detect_artificial.prepare_dict(file)
        lang_counter = detect_artificial.is_artificial(
            reference_message_set=reference_message_set, reference_file_set=reference_file_set
        )
        if lang_counter >= 60:
            language_name = str(file)
            reply = language_name[:-10]
            isartif += 1
    if isartif < 1:
        guesses: list[Language] = langdetect.detect_langs(msg.text)  # Получает определенные langdetectом языки
        reply = ""
        for guess in guesses:
            code, prob = guess.lang, guess.prob
            lang = iso639.Language.from_part1(code)  # Получает язык по ISO 639-1 коду
            lang_name = str(lang.name)
            fact_reply = detect_artificial.facts(language_f=lang_name)
            reply += "<b>{language}</b>: <code>{probability:.2%}</code>\n" "{fact}\n".format(
                language=lang.name,
                probability=prob,
                fact=fact_reply
            )
    bot.reply_to(
        msg,
        reply,
    )
