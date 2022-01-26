# Шаблон для выполнения тестового задания №2

> Привет! `Тут приветственная пламенная речь`

---

## Техническое задание /запилить постман/

Необходимо разработать калькулятор ипотечных предложений. [Пример](https://www.sravni.ru/ipoteka/?mortgagePurpose=1&creditAmount=11849421&initialAmount=1500000&mortgageTerm=120)

----

### Пользовательский сценарий
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer
2. Первоночальный взнос, в рублях без копеек . Тип данных: integer
3. Срок, в годах. Тип данных: integer

В ответ ему приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка. Тип данных: string
2. Ипотечная ставка, в процентах. Тип данных: float
3. Платеж по ипотеке, в рублях без копеек.  Тип данных: integer
----
### Технические подробности
Исходя из выше описанного пользовательского сценария, нужно:
1. Написать модель для хранения ипотечных предложений.
2. Написать ViewSet для реализации функционала вывода ипотечных предложений.
3. Фильтрацию ипотечных предложений, по введенным параметрам.
4. Реализовать функционал, который будет расчитывать платеж у всех валидных ипотечных предложений.
5. *Сортировку ипотечных предложений по ставке и по платежу. 


Задание со * является не обязательным, это дополнительный функционал, на реализацию которого, нам было бы интересно посмотреть.

----

### Используемый стек
1) Django. Обязательно
2) [DRF](https://www.django-rest-framework.org/). Обязательно
3) [django-filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html). По желанию

----

### Важно! Для облегчения проверки задания, ваше решение будет проверено интеграционным тестированием. Прохождение тестов является не обязательным условием сдачи задания.

----

#### Для начала работы, сделайте форк репозитория (и сделайте его приватным), склонируйте его и начинайте разработку.

Удачи!

PS. Если не получается разобраться с docker, то ничего страшного. Просто разработайте сервис без него, как вам удобнее.

----
### Локальный запуск приложения
#### Что бы поднять контейнеры
```shell
docker stop $(docker ps -aq)
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```
#### Что бы зайти внутрь контейнера бекенда
```shell
docker-compose exec backend sh
```
Сервис будет доступен по ссылке [http://localhost:8000/admin/login/?next=/admin/](http://localhost:8000/admin/login/?next=/admin/)

----
О выполнении задания можно уведомить по почте a.kuzmenko@idaproject.com
Так же можете задать вопросы лично мне (Telegram): @egor1344
