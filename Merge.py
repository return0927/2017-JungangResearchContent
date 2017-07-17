import codecs, dill, threading, time, progressbar

facebook = dill.load(open("facebook_crawled.dill","rb"))
discord = []

def linemanage(line):
    list = line.split("|")
    for word in list:
        try:
            threading.Thread(target=dictadd, args=(word,)).start()
        except:
            print("",end='')
            #time.sleep(20)
            #threading.Thread(target=linemanage, args=(line,)).start()


def dictadd(word):
    global dict
    if not word in dict.keys():
        dict[word] = 0
    dict[word] += 1

dict = {}

bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
n = 0
with codecs.open("Discord Filtered.txt","r",encoding='UTF-8') as f:
    for line in f:
        n+= 1
        bar.update(n)
        try:
            threading.Thread(target=linemanage, args=(line,)).start()
        except:
            print("",end='')
            #time.sleep(20)
            #threading.Thread(target=linemanage, args=(line,)).start()

import dill
dill.dump(dict, open("out.dill","wb"))