#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import os
import pandas as pd

conf_date = '25 марта 2026 года'
participants_list_file_path = '.\p2p_s2_homework_1\участники.csv'
invitation_file_path = '.\p2p_s2_homework_1\\'
talks = [
        'Python 3.12: что нового в типизации',
        'Asyncio: под капотом событийного цикла',
        'Декораторы: от простых оберток до метапрограммирования',
        'Управление зависимостями с Poetry и PDM',
        'FastAPI: создание высокопроизводительных API',
        'Pandas для анализа больших данных',
        'Django Channels: работа с вебсокетами',
        'Магия магических методов: __init__, __call__, __getattr__',
        'Профилирование Python-кода с помощью cProfile',
        'Pytest: продвинутые фикстуры и плагины',
        'Мультипроцессорность против многопоточности',
        'SQLAlchemy 2.0: современный подход к ORM',
        'Разработка CLI-инструментов на Click и Typer',
        'Pydantic V2: валидация данных на стероидах',
        'Сборщик мусора в Python: как работает GC',
        'Микросервисы на Nameko и gRPC',
        'Celery: надежные фоновые задачи',
        'Интеграция C++ кода через Pybind11',
        'Оптимизация памяти с использованием __slots__',
        'Генераторы и итераторы: экономим ресурсы',
        'PyScript: Python в браузере',
        'Автоматизация тестирования с Selenium и Playwright',
        'Работа с изображениями через Pillow и OpenCV',
        'Разработка Telegram-ботов на Aiogram 3.x',
        'Безопасность кода: Bandit и Safety',
        'Структурное сопоставление шаблонов (match/case)',
        'Контекстные менеджеры: оператор with во всей красе',
        'Реализация паттернов проектирования на Python',
        'Streamlit: быстрые дашборды для Data Science',
        'Использование Type Hints для чистого кода',
        'Логирование с Loguru вместо стандартного logging',
        'Эффективный парсинг с Beautiful Soup и Scrapy',
        'Масштабирование Django: кэширование и БД',
        'Сравнение производительности: CPython, PyPy, Cython',
        'Обработка JSON и XML: стандартная библиотека и аналоги',
        'Написание расширений на Rust с помощью PyO3',
        'Объекты-дескрипторы: глубокое погружение',
        'Тестирование API с помощью Schemathesis',
        'Docker-контейнеризация Python-приложений',
        'CI/CD для Python: GitHub Actions и GitLab CI',
        'Основы машинного обучения с Scikit-Learn',
        'Deep Learning с PyTorch: первые шаги',
        'Интернационализация приложений (i18n) в Python',
        'Метаклассы: когда они действительно нужны',
        'Работа с сетевыми протоколами через socket',
        'Mock-объекты: как правильно имитировать окружение',
        'Чистая архитектура в Python-проектах',
        'Управление конфигурациями: Pydantic-settings и Dynaconf',
        'Проверка стилистики: Flake8, Black и Isort',
        'Рефакторинг Legacy-кода на Python'
    ]

def read_csv(def_file_path):
    with open(f'{def_file_path}', 'r', encoding='UTF-8') as file:  
        lines = file.readlines()
    for i in range(0,len(lines)):
        lines[i] = lines[i].strip('\n').split(',')
    return lines

def generate_invitations(file_path, talks_list, conference_date):
# Вариант решения через список.

    invitation_count = 0

    if os.path.exists(file_path):
        def_participants = read_csv(file_path)
    else:
        # print(f'The input file not found.')
        return 'Error: The input file not found.'

    for participant in def_participants[1:]:
        selected_talk = random.choice(talks_list)
        first_name = participant[1].split()[0]

        if participant[3] == 'Москва':
            # Текст приглашения для москвичей.
            def_invitation = (
                f'Здравствуйте, {first_name}!\n'
                f'Рады видеть участника из города {participant[3]} на нашей конференции {conference_date}.\n'
                f'Рекомендуем вам посетить доклад: «{selected_talk}».'
                f'\nПриглашаем вас посетить офлайн-часть в московском офисе!'
            )

        else:
            # Базовый текст приглашения
            def_invitation = (
                f'Здравствуйте, {first_name}!\n'
                f'Рады видеть участника из города {participant[3]} на нашей конференции {conference_date}.\n'
                f'Рекомендуем вам посетить доклад: «{selected_talk}».'
            )

        with open(f'{invitation_file_path}приглашение_{participant[1].split()[0]}_{participant[1].split()[1]}.txt', 'w', encoding='UTF-8') as text_file:
            text_file.write(def_invitation)
        print(def_invitation)
        print('-' * 30)
        invitation_count += 1

    return invitation_count

# def generate_invitations(file_path, talks_list, conference_date):
#     # Вариант решения через Pandas.

#     invitation_count = 0

#     if os.path.exists(file_path):
#         df = pd.read_csv(file_path)
#         df = df.set_index('id')
#     else:
#         # print(f'The input file not found.')
#         return 'Error: The input file not found.'

#     for id, row in df.iterrows():
#         selected_talk = random.choice(talks_list)
#         if row.город == 'Москва':
#             # Текст приглашения для москвичей.
#             def_invitation = (
#                 f'Здравствуйте, {row.имя}!\n'
#                 f'Рады видеть участника из города {row.город} на нашей конференции {conference_date}.\n'
#                 f'Рекомендуем вам посетить доклад: «{selected_talk}».'
#                 f'\nПриглашаем вас посетить офлайн-часть в московском офисе!'
#             )

#         else:
#             # Базовый текст приглашения
#             def_invitation = (
#                 f'Здравствуйте, {row.имя}!\n'
#                 f'Рады видеть участника из города {row.город} на нашей конференции {conference_date}.\n'
#                 f'Рекомендуем вам посетить доклад: «{selected_talk}».'
#             )

#         with open(f'{invitation_file_path}приглашение_{row.имя.split()[0]}_{row.имя.split()[1]}.txt', 'w', encoding='UTF-8') as text_file:
#             text_file.write(def_invitation)
#         print(def_invitation)
#         print('-' * 30)
#         invitation_count += 1

#     return invitation_count

def main():
    '''Main function of the script.'''
    print('Script execution started.')

# ====================================================================================================

    result = generate_invitations(participants_list_file_path, talks, conf_date)
    if 'Error:' in str(result):
        print(result)
    else:
        print(f'Количество подготовленных приглашений - {result}шт.')

# ====================================================================================================
    print('Script execution finished.')
    return 0

if __name__ == '__main__':
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())