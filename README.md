
  <h1 align="center">Приложение для мероприятий</h1>

### Инструкция по работе с проектом
#### Клонирование репозитория помощью консольной команды:
```bash
git clone <URL репозитория>`
```
#### Запуск контейнера с приложением
```bash
docker-compose build
docker-compose up
```
#### Данные приложения
При запуске приложения из контейнера, в БД заносятся данные с помощью консольных команд. Данные содержат информацию о пользователях, организациях и мероприятиях. 

#### SuperUser
* email: admin@admin.admin
* password: admin

### Эндпойнты
* http://127.0.0.1:8000/api/login/ - POST-запрос на получение JWT-токенов пользователем
* http://127.0.0.1:8000/api/create_organization/ - POST-запрос для создания организации
* http://127.0.0.1:8000/api/create_event/ - POST-запрос для создания мероприятия
* http://127.0.0.1:8000/api/events_with_users/ - GET-запрос для вывода списка всех мероприятий с вложенной информацией об организациях и пользователях.
* http://127.0.0.1:8000/api/filtered_events/ - GET-запрос для вывода списка всех мероприятий с возможностью сортировки и фильтрации по дате, поиску по названию, пагинации