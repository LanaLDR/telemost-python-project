# Тестирование сайта mybook
[https://telemost.yandex.ru/](https://telemost.yandex.ru/)

### Используемые технологии
<p align="left">
  <img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png">
  <img height="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg">
  <img height="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg">
  <img height="30" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4">
  <img height="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg">
</p>

### Настройка окружения
Перед запуском тестов необходимо создать файл `.env` в корне проекта:

1. Скопируйте файл `.env.example`: `cp .env.example .env`
2. Заполните файл `.env` актуальными значениями для доступа к Selenoid. Пример:
```commandline
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
```

### Команды запуска тестов:
Запуск всех тестов:
```
pytest tests
```
Запуск тестового файла:
```commandline
pytest tests/<test_file_name>
```
Запуск конкретного теста:
```commandline
pytest tests/<test_file_name>::<test_function_name>
```
Построение отчета после выполнения тестов:
```
allure serve allure-results
```

### Примеры отчета

Удаленный запуск в Jenkins:

![Jenkins Build](readme_media/jenkins_stat.jpeg)

Общая страница отчета в Allure:

![Allure Overview](readme_media/allure_overview.jpeg)

Станица теста с логами браузера, скриншотом при завершении теста и видео прохождения теста:

![Allure Test Details](readme_media/allure_behaviors.jpeg)

Отчет в телеграм через бота:

![Telegram report](readme_media/telegram_notification.jpeg)
