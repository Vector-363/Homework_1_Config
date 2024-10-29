import Archive
import zipfile

def echo(commnand):
    echo_output = commnand[5:]
    return echo_output

def test_echo():
    result = echo("echo 938")
    assert result == "938"
    result = echo("echo user")
    assert result == "user"
    result = echo("echo SystemError  363")
    assert result == "SystemError  363"

def ls(command):
    path_zip = 'archive.zip'
    with zipfile.ZipFile(path_zip, 'r') as zip:
        arch = Archive.Archive(zip)
        if (command[2:] == ""):
            catalog = arch.getData(command)
            for item in catalog:
                if item == 'set()':  # если каталог пуст
                    return
                else:
                    text = ' '.join(catalog)  # преобразуем мн-во в текст
                    return text
        return

def test_ls():
    result = ls("ls")
    files = {"readme.txt", "user", "data", "money", "system"}
    assert set(result.split()) == files

    result = ls("ls ")
    assert result == None

def cd(command):
    path_zip = 'archive.zip'
    with zipfile.ZipFile(path_zip, 'r') as zip:
        arch = Archive.Archive(zip)
        parts = command[3:].split('/')
        for i in parts:
            if (arch.comeDirectory(i) == -1):
                return f"cd: '{i}': No such file or directory"
        return

def test_cd():
    result = cd("cd user")
    assert result == None

    result = cd("cd ip")
    assert result == f"cd: 'ip': No such file or directory"

    result = cd("cd ..")
    assert result == None

    result = cd("cd user/../ip")
    assert result == f"cd: 'ip': No such file or directory"

def du(command):
    path_zip = 'archive.zip'
    with zipfile.ZipFile(path_zip, 'r') as zip:
        arch = Archive.Archive(zip)
        if command[2:] == '':
            for info in zip.infolist():
                return f"Файл: {info.filename}, Размер: {info.file_size} байт"
        else:
            names = command.split()
            text = arch.du(names[1])
            return text

def test_du():
    result = du("du")
    assert result == "Файл: archive/, Размер: 0 байт"

    result = du("du user")
    assert result == ("Файл: archive/user/, Размер: 0 байт")

    result = du("du ip")
    assert result =="du: cannot access [ip]: No such file or directory"

def mv(command):
    path_zip = 'archive.zip'
    with zipfile.ZipFile(path_zip, 'r') as zip:
        arch = Archive.Archive(zip)

        names = command.split()
        if (arch.rename_file(names[1], names[2]) == -1):
            return f"cannot stat  '{names[1]}': No such file or directory"

        catalog = arch.getData("ls")
        for item in catalog:
            if item == 'set()':  # если каталог пуст
                return
            else:
                text = ' '.join(catalog)  # преобразуем мн-во в текст
                return text

        names = command.split()

def test_mv():
    result = mv("mv user vip")
    files = {"readme.txt", "vip", "data", "money", "system"}
    assert set(result.split()) == files

    result = mv("mv ip user")
    assert result == "cannot stat  'ip': No such file or directory"

    result = mv("mv system user")
    files = {"readme.txt", "user", "data", "money"}
    assert set(result.split()) == files

test_mv()
test_du()
test_cd()
test_ls()
test_echo()

print("Все тесты пройдены!")