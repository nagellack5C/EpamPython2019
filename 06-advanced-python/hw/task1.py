"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной,
например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""


class PrintableFolder:
    def __init__(self, name, content=None):
        if not isinstance(name, str):
            raise TypeError("Please supply a string as entity name")
        if content and not isinstance(content,
                                      (PrintableFolder, PrintableFile, list)):
            raise TypeError("Content must be list of files/folders"
                             "or a single file/folder")
        if isinstance(content, list) and len(content) < 1:
            raise ValueError("List cannot be empty")
        self.name = name
        self.content = content

    def __str__(self, lvl=0):
        text = "|   " * lvl
        if lvl > 0:
            text += "|-> "
        text += f"V {self.name}\n"
        if self.content:
            for obj in self.content:
                text += obj.__str__(lvl + 1)
        return text

    def __contains__(self, item):
        if not self.content:
            return False
        elif item == self.content:
            return True
        elif isinstance(self.content, (list, PrintableFolder)):
            if item in self.content:
                return True
            else:
                for folder in filter(lambda f: isinstance(f, PrintableFolder),
                                     self.content):
                    if item in folder:
                        return True
        return False


class PrintableFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Please supply a string as entity name")
        self.name = name

    def __str__(self, lvl=0):
        text = "|   " * lvl
        if lvl > 0:
            text += "|-> "
        text += self.name + "\n"
        return text


if __name__ == "__main__":
    file1 = PrintableFile("file1")
    file2 = PrintableFile("file2")
    file3 = PrintableFile("file3")
    file4 = PrintableFile("file4")
    file5 = PrintableFile("file5")

    folder1 = PrintableFolder("folder1")
    folder2 = PrintableFolder("folder2", [file1])
    folder3 = PrintableFolder("folder3", [folder1, file3, file2])
    folder4 = PrintableFolder("folder4", [folder2])
    folder5 = PrintableFolder("folder5", [folder4, file4, folder3])
    print(folder5)
    print(file1 in folder5)

    test_file = PrintableFile("test_file")
    test_dir1 = PrintableFolder("folder1", test_file)
    test_dir2 = PrintableFolder("folder2", test_dir1)
    if test_file in test_dir2:
        print(")))")