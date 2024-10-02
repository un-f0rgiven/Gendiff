### Hexlet tests and linter status:
[![Actions Status](https://github.com/un-f0rgiven/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/un-f0rgiven/python-project-50/actions)
[![Maintainability](https://codeclimate.com/github/un-f0rgiven/python-project-50/badges/gpa.svg)](https://codeclimate.com/github/un-f0rgiven/python-project-50/maintainability)
[![Test Coverage](https://codeclimate.com/github/un-f0rgiven/python-project-50/badges/coverage.svg)](https://codeclimate.com/github/un-f0rgiven/python-project-50/test_coverage)

**Учебный проект - Вычислитель отличий**
Программа вычисляет различия между двумя файлами. 
Диф строится на основе того, как изменилось содержимое во втором файле относительно первого. 
Поддерживаются форматы JSON, YAML.
Программа позволяет выводить информацию в 4 видах:
    различия файлов со вложенными структурами
    описывает различия текстом
    выводит в структурированном виде
    сравнивает плоские файлы

**Требования**
OS Linux
Python 3.9 и выше

**Установка и запуск**
Установка приложения производится через команду:
*make package-install*
Удаление производится через команду:
*make package-uninstall*
Запуск производится через команду:
*gendiff [-h] [-f FORMAT] first_file second_file*

*-h* - выводит справку

*-f, --format* - задаёт формат вывода информации. Доступных форматов 4:
    stylish - формат, заданный по умолчанию. Отображает различия файлов со вложенными структурами
    plain - описывает различия текстом
    json - выводит различия в структурированном виде
    flat - сравнение плоских файлов

*first_file* - указать путь к первому файлу. Поддерживаются форматы JSON, YAML
*second_file* - указать путь к первому файлу. Поддерживаются форматы JSON, YAML

### Asciinema Сравнение плоских файлов (JSON)
https://asciinema.org/a/n8iRPyzYczGco8LL2htVwL6GR

### Asciinema Сравнение плоских файлов (YAML)
https://asciinema.org/a/sn90foIDsVqhND4RhusrNIvY3

### Asciinema Рекурсивное сравнение (JSON)
https://asciinema.org/a/AHpwHm3E4QzPP9ZPCv2nTF8Na

### Asciinema Рекурсивное сравнение (YAML)
https://asciinema.org/a/t4VOcK2u1pXV9L4inhDfyrTla

### Asciinema Плоский формат (JSON)
https://asciinema.org/a/QXksHESVfa2o6J0Gc4PMTTslh

### Asciinema Плоский формат (YAML)
https://asciinema.org/a/W4omD6vajzBadRP8uWNJAtuYe

### Asciinema Вывод в JSON (JSON)
https://asciinema.org/a/3PSoLR9ndB1kmONX5bK0u1L7c

### Asciinema Вывод в JSON (YAML)
https://asciinema.org/a/hc9td1biaD7cDoagVtdzFgNhA