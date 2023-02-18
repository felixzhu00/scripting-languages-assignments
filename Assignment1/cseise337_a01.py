#Problem 1
def is_chaotic(input):
    dic = {}
    for value in input:
        if value in dic.keys():
            dic[value] += 1
        else:
            dic[value] = 1
    app = set([value for value in dic.values()])
    if len(dic) == len(app):
        return 'TOHRU'
    else:
        return 'ELMA'

#Problem 2
def is_balanced(input):
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    stack = []
    for bracket in input:
        if bracket in opening:
            stack.append(bracket)
        else:
            if bracket == closing[opening.index(stack[-1])]:
                stack.pop()
    return len(stack) == 0

#Problem 3
def winning_function(items, func1, func2):
    if list((map(func1, items))).count(True) == list((map(func2, items))).count(True):
        return "TIE"
    elif(list((map(func1, items))).count(True) > list((map(func2, items))).count(True)):
        return func1.__name__
    else:
        return func2.__name__

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

#Problem 4
class FS_Item():
    def __init__(self, name):
        self.name = name

class Folder(FS_Item):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add_items(self, item):
        self.items.append(item)

class Files(FS_Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

def load_fs(ls_output):
    root = None
    current_dir = None
    with open(ls_output, 'r') as input:
        for line in input:
            file_arr = line.split("\n\n")[0].split()
            if(len(line.split("\n\n")[0].split()) == 1):
                path_arr = line.split("\n\n")[0].split()[0][:-1].split("/")
                if(root == None):
                    root = Folder(path_arr[-1])
                    current_dir = root
                elif(current_dir.name != path_arr[-2]):
                    current_dir = root
                    if(len(path_arr) > 1):
                        for directory in path_arr[1:]:
                            index = list(map(lambda x : x.name, current_dir.items)).index(directory)
                            current_dir = current_dir.items[index]
                else:
                    index = list(map(lambda x : x.name, current_dir.items)).index(path_arr[-1])
                    current_dir = current_dir.items[index]
            if(len(line.split("\n\n")[0].split()) > 2 and file_arr[0][0] != 'd'):
                name = file_arr[-1]
                size = file_arr[4]
                new_file = Files(name, size)
                current_dir.add_items(new_file)
            if(len(line.split("\n\n")[0].split()) > 2 and file_arr[0][0] == 'd'):
                name = file_arr[-1]
                new_folder = Folder(name)
                current_dir.add_items(new_folder)
    return root    

#Problem 5
def decode(ct):
    string = ""
    shift = 0
    for value in ct:
        ordinal = ord(value)
        if((ordinal >= 97 and ordinal <= 122)):
            lexical = ordinal - 97
            calcu = lexical -(59 if shift == 0 else 0) - shift
            while(not((calcu >= 97 and calcu <= 122))):
                calcu += 26
            string += chr(calcu)
            shift += calcu
        else:
            string += value
    return string




# #Test 1
# print( is_chaotic("aabbcd"))
# print(is_chaotic('aaaabbbccd'))
# print(is_chaotic('abaacccdee'))
# print('\n')

# #Test 2
# print(is_balanced("{[(])}"))
# print(is_balanced("[{}()]"))
# print('\n')

# #Test 3
# print(winning_function([2,3,4,5,6,8],odd, even))
# print('\n')

# #Test 4

# def print_tree(root, level = 0):
#     print("        " * level, root.name)
#     if(type(root) == type(Folder("test"))):
#         for child in root.items:
#             print_tree(child, level + 1)
   
# tree = load_fs("lsoutput.txt")
# print_tree(tree)
# print('\n')

# #Test 5
# print(decode("sidnkw"))
# print(decode("i uz zwgd jqf"))
# print('\n')