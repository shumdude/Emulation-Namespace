import os, json, mimetypes, click


class JSONCreator:
    def __init__(self):
        # self.path = path
        self.data = {}

    def recursion_function(self, some_dir: str, go_inside=None) -> None:
        if go_inside is None:
            go_inside = self.data

        walk = os.walk(some_dir)  # генератор древа каталогов и прочего
        folder_name = os.path.basename(some_dir)  # имя папки, в которой находимся
        go_inside[folder_name] = {}  # создаём в части data эл-т, где ключ - папка в которой находимся
        go_inside = go_inside[folder_name]  # go_inside - это внутренняя часть словаря, в которым находимся

        for dir_path, dir_names, file_names in walk:
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                go_inside[file_name] = {
                    "type_file": self.type_file(file_path),
                    "size": self.size_file(file_path)
                }
            for dir_name in dir_names:
                new_path = os.path.join(dir_path, dir_name)
                self.recursion_function(new_path, go_inside)
            break

    @staticmethod
    def size_file(path_to_file):  # здесь потом хочется использовать match case для красоты и удобства
        if mimetypes.guess_type(path_to_file)[0] == "application/octet-stream":
            postfix = " bites"
            size_file = str(os.path.getsize(path_to_file))
        elif mimetypes.guess_type(path_to_file)[0] == "text/plain":
            postfix = " lines"
            size_file = str(sum(1 for line in open(path_to_file)))
        result = size_file + postfix
        return result

    @staticmethod
    def type_file(path_to_file):
        if mimetypes.guess_type(path_to_file)[0] == "text/plain":
            type_file = "text"
        elif mimetypes.guess_type(path_to_file)[0] == "application/octet-stream":
            type_file = "binary"
        return type_file


jc = JSONCreator()
jc.recursion_function("C:\\Test")
with open("data.json", "w") as w:
    json.dump(jc.data, w, indent=4)


@click.command()
@click.option('--input_path', prompt='Please, enter the PATH')
def start_CLI(input_path):
    jc = JSONCreator()
    jc.recursion_function(input_path)
    json_string = json.dumps(jc.data, indent=4)
    click.echo(f"{json_string}")


start_CLI()
