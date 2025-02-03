# Трекер полезных привычек

```
В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. Заказчик прочитал книгу, 
впечатлился и обратился к вам с запросом реализовать трекер
полезных привычек.
В рамках учебного курсового проекта реализуйте бэкенд-часть 
SPA веб-приложения.
```

### Критерии приемки курсовой работы

Настроили CORS.
Настроили интеграцию с Телеграмом.
Реализовали пагинацию.
Использовали переменные окружения.
Все необходимые модели описаны или переопределены.
Все необходимые эндпоинты реализовали.
Настроили все необходимые валидаторы.
Описанные права доступа заложены.
Настроили отложенную задачу через Celery.
Проект покрыли тестами как минимум на 80%.
Код оформили в соответствии с лучшими практиками.
Имеется список зависимостей.
Результат проверки Flake8 равен 100%, при исключении миграций.
Решение выложили на GitHub
### Модели
#### Привычка:
Пользователь — создатель привычки.
Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку.
Действие — действие, которое представляет собой привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для
приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие
привычки.
### Валидаторы
Исключить одновременный выбор связанной привычки и указания вознаграждения.
Время выполнения должно быть не больше 120 секунд.
В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки.
Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
### Эндпоинты
Регистрация.
Авторизация.
Список привычек текущего пользователя с пагинацией.
Список публичных привычек.
Создание привычки.
Редактирование привычки.
Удаление привычки.

### Для запуска проекта необходимо 
Установить Poetry, установить зависимости.  
Создать .env файл для конфигурации в корне проекта.  
После установки зависимостей нужно применить миграции к базе данных.  
Запустить сервер, убедившись что установлены все инструменты, такие как Redis и PostgreSQL
