import tkinter as tk
import subprocess
import zipfile
import os

import Archive

def append_output(output_text, text):
    output_text.config(state='normal')
    output_text.insert(tk.END, text)
    output_text.config(state='disabled')
    output_text.see(tk.END)

def execute_command(event, input_var, output_text, user, arch,zip):
    command = input_var.get()
    input_var.set("")

    append_output(output_text, f" {command}\n")

    if command.startswith("echo "):
        echo_output = command[5:]
        append_output(output_text, echo_output + "\n")
        append_output(output_text, f"[{user}]: {arch.currentDir}")
        return

    elif command.startswith("cd"):
        parts = command[3:].split('/')
        for i in parts:
            if (arch.comeDirectory(i) == -1):
                append_output(output_text, f"cd: '{i}': No such file or directory" + '\n')

        append_output(output_text, f"[{user}]: {arch.currentDir}")
        return

    elif command.startswith("ls"):
        if (command[2:] == ""):
            catalog = arch.getData(command)
            for item in catalog:
                if item == 'set()':  # если каталог пуст
                    return
                else:
                    text = ' '.join(catalog)  # преобразуем мн-во в текст
                    append_output(output_text, text)
                    append_output(output_text, "\n")
                    append_output(output_text, f"[{user}]: {arch.currentDir}")
                    return
        append_output(output_text, f"[{user}]: {arch.currentDir}")
        return
    
    elif command.startswith("du"):
        if command[2:] == '':
            for info in zip.infolist():
                append_output(output_text, f"Файл: {info.filename}, Размер: {info.file_size} байт" + "\n")
                append_output(output_text, f"[{user}]: {arch.currentDir}")
            return
        else:
            names = command.split()
            text = arch.du(names[1])
            append_output(output_text, text)
            append_output(output_text, "\n")
            append_output(output_text, f"[{user}]: {arch.currentDir}")
            return

    elif command.startswith("mv"):
        names = command.split()
        if(arch.rename_file(names[1], names[2]) == -1):
            append_output(output_text, f"cannot stat  '{names[1]}': No such file or directory" + '\n')
        append_output(output_text, f"[{user}]: {arch.currentDir}")

    elif command == "exit":
        exit(0)

    else:
        append_output(output_text, f"{command}: not found!" + '\n')
        append_output(output_text, f"[{user}]: {arch.currentDir}")

def main():
    root = tk.Tk()
    root.title("Linux Terminal Emulator")
    root.geometry("600x600")
    font = ("Courier New", 12)


    output_text = tk.Text(root, bg="black", fg="white", wrap="word", state='disabled', font=font) #создание поле ввода
    output_text.pack(expand=True, fill='both')

    input_var = tk.StringVar() #переменная для вводимого текста

    input_entry = tk.Entry(root, textvariable=input_var, bg="white", fg="black", font=font) #создание поле вывода
    input_entry.pack(fill='x')

    user = os.getlogin()
    append_output(output_text, f"[{user}]: archive/")


    path_zip = 'archive.zip'
    with zipfile.ZipFile(path_zip, 'r') as zip:
        arch = Archive.Archive(zip)
        input_entry.bind('<Return>', lambda event: execute_command(event, input_var, output_text, user, arch, zip))  # привязка клавиши ENTER

    root.mainloop()  # цикл для окна

main()