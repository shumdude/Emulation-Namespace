n = int(input())
emulation_namespace = {'global': {}, 'global_values': {}}
values = {}
count = 0


def create(namespace, parent, dictionary=emulation_namespace):
    if parent in dictionary:
        dictionary[parent][namespace] = {}
        dictionary[parent][namespace + '_values'] = {}
    else:
        for key in dictionary.keys():
            create(namespace, parent, dictionary=dictionary[key])
    return None


def add(namespace, var, dictionary=emulation_namespace):
    if namespace in dictionary:
        global count
        dictionary[namespace + '_values'][var] = str(count)
        count += 1
    else:
        for key in dictionary.keys():
            add(namespace, var, dictionary=dictionary[key])
    return None


def get():
    return None


for i in range(n):
    cmd, name, arg = input().split()
    if cmd == 'create':
        create(name, arg)
    if cmd == 'add':
        add(name, arg)



print(emulation_namespace)
