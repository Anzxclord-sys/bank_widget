# Виджет банковских операций

Учебный проект на Python для обработки банковских операций клиента.

## Что реализовано в проекте

В папке src находятся три модуля:
1. masks.py - функции для маскировки номеров карт и счетов звездочками.
2. widget.py - общая функция для маскировки и функция перевода даты в формат ДД.ММ.ГГГГ.
3. processing.py - функции для фильтрации операций по статусу и сортировки по дате.

## Как установить

Склонировать репозиторий по ссылке:
```
git clone [https://github.com/Anzxclord-sys/bank_widget.git](https://github.com/Anzxclord-sys/bank_widget.git)
```

Установить зависимости через poetry:
```
poetry install
```

## Примеры запуска функций

Пример работы функций из нового модуля processing:
```python
from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

# Вывод только выполненных операций (EXECUTED)
print(filter_by_state(data))

# Сортировка операций по дате (от новых к старым)
print(sort_by_date(data))
```