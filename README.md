# scrapy_parser_pep

Собирает информацию о PEP с официального сайта. Переходит по каждой ссылке PEP и сохраняет: Имя, статус, номер pep. Эта информация записывается в "pep"- csv файл. 
В pipelines происходит подсчет всех статусов и вывод этой информации в "status_summary" - csv файл. 
Файлы сохраняются в дирректорию results.

## Установка
git clone https://github.com/MikhailSavenko/scrapy_parser_pep

## Установка зависимостей
pip install -r requirements.txt

## Использование
scrapy crawl pep