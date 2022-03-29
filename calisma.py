list_methods = []
tuple_methods = []
string_methods = []
set_methods = []
dict_methods = []
int_method = []
header = ["List Method",
          "Tuple Method",
          "String Method",
          "Set Method",
          "Dict Method",
          "Int Method"]
lists = [list_methods,tuple_methods,string_methods,set_methods,dict_methods,int_method]
HEADER = '\033[92m'
ENDC = '\033[0m'
BOLD = '\033[1m'
def add(method,list_name):
    for m in dir(method):
        if m.startswith("__"):
            continue
        else:
            list_name.append(m)

add(list,list_methods)
add(tuple,tuple_methods)
add(dict,dict_methods)
add(set,set_methods)
add(str,string_methods)
add(int,int_method)
max_len = 0
for head in lists:
    if len(head)>max_len:
        max_len = len(head)
lenght = []
with open("method.txt","w") as file:
    for i in lists:
        lenght.append(len(i))

    for i in range(len(header)):
        print(f"{HEADER + BOLD}{header[i]} ({lenght[i]}){ENDC}", end="")
        print(" " * (25 - len(header[i])), end="")
        file.write(f"{header[i]} ({lenght[i]})")
        file.write(" " * (25 - len(header[i])))
    for i in range(max_len):
        print()
        file.write("\n")
        for method in lists:
            if i >= len(method):
                print("-------", end="")
                print(" " * 23, end="")
                file.write("-------")
                file.write(" " * 23)
            else:
                print(method[i], end="")
                print(" " * (30 - len(method[i])), end="")
                file.write(method[i])
                file.write(" " * (30 - len(method[i])))
