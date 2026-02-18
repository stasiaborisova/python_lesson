# Lesson 10 — Allure Report

## Описание проекта

В проект добавлена интеграция Allure для формирования отчета по автотестам.

Тесты реализованы с использованием:
- pytest
- Selenium
- PageObject
- Allure

Все тесты размечены:
- шагами (allure.step)
- декораторами (@allure.feature, @allure.title, @allure.description, @allure.severity)

---

## Установка зависимостей

Перед запуском необходимо установить зависимости:
pip install selenium pytest allure-pytest

Также необходимо установить Allure CLI.

---

## Запуск тестов с генерацией отчета

В терминале выполнить:
pytest lesson_10 --alluredir=allure-results

После выполнения появится папка:
allure-results

---

## Просмотр отчета

Для просмотра отчета выполнить:
allure serve allure-results

После этого откроется браузер с отчетом Allure.