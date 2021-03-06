## Пульт охраны банка

#### Это внутренний репозиторий для сотрудников банка «Сияние».
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.
***
#### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные
Cоздайте в репозитории файл __.env__ и подставьте данные в файл.

1.  переменная `DATABASE_URL`:
    Запросите доступ к БД у менеджера вашего банка.
1.  переменная `DEBUG`: укажите `DEBUG="false"`

    При установке `DEBUG="true"` указывает на вывод отладочной информации(логи) на странице браузера.

1.  переменная `SECRET_KEY`:  Это секретный ключ, применяемый для защиты от CRSF 
([межсайтовая подделка запроса](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0_%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0 "CRSF: межсайтовая подделка запроса")).
   
    Для создания такого числа воспользуйтесь файлом secret_string.py.   
 
    Запустите скрипт командой  ```python secret_string.py``` 
 
    скопируйте полученное число и подставьте в переменную `SECRET_KEY`.

Пример файла __.env__
```
DATABASE_URL='postgres://user:password@host:port/dbname'
SECRET_KEY='REPLACE_ME'
DEBUG=false
```
### Запуск
* Откройте командную строку.
* Зайдите в репозиторий.
* Запустите скрипт командой  ```python manage.py runserver 0.0.0.0:8000. ```
* В своём браузере запустите сайт по ссылке http://localhost:8000/ или http://127.0.0.1:8000/

#### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
