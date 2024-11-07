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

Тестирование команд:
1. ls и cd

![image](https://github.com/user-attachments/assets/72082d20-1e6d-4c9e-b402-e76c93819895)

3. echo

![image](https://github.com/user-attachments/assets/f3e1ffc8-8a96-48b4-9ac9-ace498ce4caa)

4. mv

![image](https://github.com/user-attachments/assets/4ce72795-5028-4de2-a27f-52cc6b6fa3fe)

5. du

![image](https://github.com/user-attachments/assets/fb55aec4-1682-47d3-983f-005990283346)


Также результаты автоматического тестирования:
Ссылка на код тестрования: https://github.com/Vector-363/Homework_1_Config/blob/main/Command_line/.venv/TestSystem.py
![image](https://github.com/user-attachments/assets/b77e6f05-180e-444c-9470-40e068053fab)

