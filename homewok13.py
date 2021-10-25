path = "./in.txt"
reader = open(path, mode="r")
content = reader.read()
numbers = sorted([int(number) for number in content.split()])
string_numbers = " ".join(map(str, numbers))
reader.close()
path = "./out.txt"
writer = open(path, mode='w')
result = writer.write(string_numbers)
writer.close()