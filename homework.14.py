path = "./in.txt"
reader = open(path, mode="r")
content = reader.read()
words = [word for word in content.split()]
res = " ".join(list(filter(lambda word: len(word) >= 5, words))) # по условию больше, но сделала >= 5, чтоб совпадало с заданным примером вывода
reader.close()
path = "./out.txt"
writer = open(path, mode='w')
result = writer.write(res)
writer.close()





