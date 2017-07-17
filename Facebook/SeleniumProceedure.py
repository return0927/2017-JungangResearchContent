import codecs, bs4, re


korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')

body = codecs.open("export.html","r",encoding="UTF-8").read()
result = korean.findall(body)

import dill
dill.dump(result, open("facebook_crawled.dill","wb"))