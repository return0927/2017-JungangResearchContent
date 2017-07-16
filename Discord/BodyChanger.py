import codecs, os, re

def Split(string):
    if "Message Deleted" in string: authorSplitter = "Author : "; messageSplitter = " | Content : "
    elif "Message Editted" in string: authorSplitter = " / Author : "; messageSplitter = " | Before : "; afterMessageSplitter = " | After : "
    elif "]" in string and "Author" in string and "Message" in string: authorSplitter = "Author: "; messageSplitter = " | Message: "
    else:
        return "Splitted Line", string
    date = string.split(" ]   ")[0]
    author = string.split(authorSplitter)[1].split(messageSplitter)[0]
    message = string.split(messageSplitter)[1] if not "afterMessageSplitter" in locals() else string.split(afterMessageSplitter)[1]
    return date, author, message

os.chdir("./Logs")
dir = os.listdir()
#filter = "2017.\d+.\d+ \d+:\d+:\d+"
filter = "^[0-9][0-9][0-9][0-9][.][0-9][0-9][.][0-9][0-9][ ][0-9][0-9][:][0-9][0-9][:][0-9][0-9]"

for file in dir:
    print("="*10, file, "="*10)
    with codecs.open(file, "r", encoding="UTF-8") as f:
        #print(  f.read().replace("\n","|||")  )
        print(re.sub(filter, "\n", f.read().replace("\n","")))
