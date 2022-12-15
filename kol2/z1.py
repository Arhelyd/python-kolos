method_list = [method for method in dir(list) if method.startswith('__') is False]
print(method_list)

method_list = [attribute for attribute in dir(list) if callable(getattr(list, attribute)) and attribute.startswith('__') is False]
print(method_list)

f = open("demofile.txt", "r")

print(f.readlines())
