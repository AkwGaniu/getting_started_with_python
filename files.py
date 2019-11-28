# Working with files
file = open('testing.txt', 'r')
for line in file.readlines():
    print(line)
file.close()

new_file = open('index.html', 'a')
new_file.write("\n<p>Some paragraph in HTML document</p>")
new_file.close()
