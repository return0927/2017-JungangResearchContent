import codecs, os, progressbar

os.chdir("./Logs")
files = os.listdir()
files.remove("out.txt")

filter = input()
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)


count = 0
for file in files:
    data  = codecs.open(file, "r", encoding="UTF-8").readlines()
    for line in data:
        count += line.count(filter)
        bar.update(count)