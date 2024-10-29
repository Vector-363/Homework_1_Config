import os
import zipfile

from Tools.scripts.stable_abi import itemclass
from select import select

class Archive:
    def __init__(self, zip):
        self.zip = zip
        self.namelist = zip.namelist()
        self.currentDir = zip.namelist()[0]
        self.rootDir = zip.namelist()[0]

        datalist = zip.infolist()
        self.infodict = {}
        for data in datalist:
            if (data.is_dir()):
                self.infodict[data.filename[:-1]] = data
            else:
                self.infodict[data.filename] = data

        self.setNamePath = {}
        for name in self.namelist:
            if name == self.currentDir:
                continue
            modules = cutPath(name)
            self.setNamePath[name] = modules

    def getData(self, commands):
        catalog = self.chooseItemInDir(self.currentDir)
        return catalog

    def catenate(self, path):
        try:
            dir = self.clearPatn(path)
        except Exception as e:
            print(e)
            return
        try:
            with self.zip.open(dir) as myfile:
                print(myfile.read())
        except Exception as e:
            print(f"{dir} is not file")       
            
    def chooseItemInDir(self, directory):
        partsPath = cutPath(directory)
        border = len(partsPath)
        lastDir = partsPath[border - 1]
        items = set()
        for key in self.setNamePath:
            choosenPath = self.setNamePath[key]
            if len(choosenPath) > border:
                if choosenPath[border - 1] == lastDir:
                    modules = self.setNamePath[key]
                    items.add(modules[border])
        return items

    def comeDirectory(self, path):
        if path == "/":
            self.currentDir = self.rootDir
            print(rootDir)

        elif path == "..":
            path = self.currentDir
            parts = path.split("/")
            newPath = ''
            if len(parts) == 2:
                newPath = self.rootDir
            for i in range(len(parts) - 2):
                newPath += parts[i] + '/'
            self.currentDir = newPath

        else:
            dir = self.clearPatn(path)
            if (dir in self.namelist) and not "." in dir:
                self.currentDir = dir
                return
            else:
                return -1

    def clearPatn(self, path):
        dir = ''
        path = self.normalizePath(path)
        if path[0] == "/" and path[1:] in self.namelist:
            dir = path[1:]
        elif path[0] != "/":
            dir = os.path.join(self.currentDir, path)
        else:
            raise ValueError(f"Cannot access '{path}': No such file or directory")
        return dir

    def normalizePath(self, path):
        if path[len(path) - 1] != '/' and not "." in path:
            path += '/'
        return path

    def rename_file(self, old_dir_name, new_dir_name):
        for item in self.namelist:
            if(self.currentDir + old_dir_name + '/' == item):
                for key in self.setNamePath:
                    for part in self.setNamePath[key]:
                        if(part == new_dir_name):
                            self.namelist = [name.replace(self.currentDir + old_dir_name + '/', self.currentDir + new_dir_name + '/' + old_dir_name + '/') for name in self.namelist]

                            updated_dict = {}
                            for key, value in self.setNamePath.items():
                                # Проверяем, содержит ли ключ исходную директорию
                                if old_dir_name in key:
                                    # Заменяем исходную директорию на целевую
                                    new_key = key.replace(old_dir_name, new_dir_name + '/' + old_dir_name)
                                    # Обновляем путь в значениях
                                    new_value = [new_dir_name if part == old_dir_name else part for part in value]
                                    new_value.append(old_dir_name)
                                    updated_dict[new_key] = new_value
                                else:
                                    # Если ключ не содержит исходную директорию, оставляем его без изменений
                                    updated_dict[key] = value
                            self.setNamePath = updated_dict;
                            return;
                # переименовывание директории
                new_setNamePath = {}
                for key in self.setNamePath:
                    # Заменяем в ключе
                    new_key = key.replace(old_dir_name, new_dir_name)
                    # Заменяем в значениях списка
                    new_value = [part.replace(old_dir_name, new_dir_name) for part in self.setNamePath[key]]
                    new_setNamePath[new_key] = new_value  # Копируем обновленные значения
                self.setNamePath = new_setNamePath

                self.namelist = [name.replace(old_dir_name, new_dir_name) for name in self.namelist]
                return;
        return -1;

    def du(self, file_name):
        for info in self.zip.infolist():
            if (info.filename == self.currentDir + file_name + "/"):
                return f"Файл: {info.filename}, Размер: {info.file_size} байт"
        return f"du: cannot access [{file_name}]: No such file or directory"
               

def cutPath(path):
    modules = []
    modules = path.split("/")
    if modules[len(modules) - 1] == '':
        modules.pop()
    return modules
