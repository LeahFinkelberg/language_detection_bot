# language_detection_bot

Описание
Detect language bot -- это бот, который распознает языки по введенному тексту. Он умеет: 1) определять язык с помощью библиотеки langdetect (55 языков, которые изначально были в библиотеке + языки, которые мы туда добавили), 2) определять 5 искусственных языков* (волапюк, на'ви, квенья, синдарин, хен ллинге), сверяясь с файлами словарей этих языков; в ответ он выдает название языка на английском; 3) выдавать интересные факты об определенных языках
*словари были найдены и "очищены" от всех остальных языков (например, нет словарей квенья-квенья, но есть словари Клингонский-английский), но бот пока не определяет эти языки

Использование
- Надо запустить код в файле main.py и найти в телеграме бота https://t.me/langdetectbot. Начать работу бота надо командой /start. После этого можно вводить ему текст (фразу, слово).
- Если вы хотите узнать факт о языке введите команду /facts и название языка на английском (или код языка).

Структура репозитория
- main.py -- код для создания, регистрации и запуска бота
- handlers.py -- команды бота: start и, собственно, определение языка, использующее библиотеку langdetect и файлы со словарями искусственных языков
- requirements.txt -- список использованных библиотек
- в директории dict -- код для создания словарей искусственных слов из файлов с английскими переводами и аозданные словари
- в директории extend -- файлы с кодом для добавления новых языков в langdetect и файлы с добавленными языками

Ресурсы
- Библиотеки: pyTelegramBotAPI, langdetect, python-dotenv, python-iso639, telebot
- Ресурсы (для кода):
   - https://serverfault.com/questions/7503/how-to-determine-if-a-bash-variable-is-empty
   - http://web.archive.org/web/20200501190525/https://stereo.lu/detecting-luxembourgish-using-a-spam-filter-and-wikipedia
   - https://github.com/shuyo/language-detection/issues/84
   - https://github.com/optimaize/language-detector/issues/73
   - https://code.google.com/archive/p/language-detection/
   - https://matiascodesal.com/blog/how-use-git-repository-pip-dependency/
   - https://peps.python.org/pep-0440/#version-specifiers
   - https://packaging.python.org/en/latest/glossary/#term-Version-Specifier
   - https://pip.pypa.io/en/stable/reference/requirement-specifiers/
   - https://github.com/Mimino666/langdetect/issues/5
   - https://docs.python.org/3/library/sqlite3.html?highlight=sqlite#sqlite3.threadsafety
   - https://www.reddit.com/r/Python/comments/ursa30/comment/i8zpovr/
   - https://github.com/jacksonllee/iso639/blob/main/src/iso639/language.py
   - https://github.com/Mimino666/langdetect/tree/a1598f1afcbfe9a758cfd06bd688fbc5780177b2
   - https://github.com/Mimino666/langdetect/blob/a1598f1afcbfe9a758cfd06bd688fbc5780177b2/langdetect/detector.py#L48
   - https://wiki.installgentoo.com/index.php/Interjection
   - https://pytba.readthedocs.io/ru/latest/sync_version/index.html
   - https://pytba.readthedocs.io/ru/latest/quick_start.html
   - https://pytba.readthedocs.io/ru/latest/formatting.html
   - https://core.telegram.org/api/entities
   - https://github.com/Mimino666/langdetect/tree/master/langdetect
   - https://pytba.readthedocs.io/ru/latest/sync_version/index.html#telebot.TeleBot.register_message_handler
   - https://pypi.org/project/python-dotenv/
   - https://core.telegram.org/bots/samples

Участники:
Маша Моисеева, Лея Финкельберг, Аля Широкова
