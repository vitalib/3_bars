# Ближайшие бары 
Prints bars with maximum and minimum quantity of seats, 
displays information about the bar that is closes to given
gps coordinates.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <filepath> # possibly requires call of python3 executive instead of just python

Smallest bar:
Name : БАР. СОКИ
Address : Дубравная улица, дом 34/29
PublicPhone : [{'PublicPhone': '(495) 258-94-19'}]
SeatsCount : 0

Biggest bar:
Name : Спорт бар «Красная машина»
Address : Автозаводская улица, дом 23, строение 1
PublicPhone : [{'PublicPhone': '(905) 795-15-84'}]
SeatsCount : 450

Please input yr gps coordinates: 37.31 23.221
The closest bar for you is: 
Name : Бар «Ракета»
Address : вблизи посёлка ЛМС, дом 1Б/Н
PublicPhone : [{'PublicPhone': '(495) 676-85-55'}]
SeatsCount : 30
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
