# Homework_1_Config

Командная строка на python (вариант №26)

[ссылка](https://github.com/Vector-363/Homework_1_Config/tree/main/Command_line)

Постановка задачи: 

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
tar. Эмулятор должен работать в режиме GUI.

Ключами командной строки задаются:
• Путь к архиву виртуальной файловой системы.
• Путь к стартовому скрипту.
Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. mv.
2. du.
3. echo.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 2 теста.

Интерфейс и пример работы нескольких команд
![image](https://github.com/user-attachments/assets/a6ac06dc-bb2f-4c5a-9f08-847bdcc8992d)
