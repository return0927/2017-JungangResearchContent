import json, codecs

class settings:
    def get():
        with codecs.open("settings.json", "r", encoding="UTF-8") as f:
            string = " ".join([str(x).replace("\r", "").replace("\n", "").replace("\t", "") for x in f.readlines()])
        return json.loads(string)

    def save(string):
        try:
            with codecs.open("settings.json", "w", encoding='UTF-8') as f:
                f.write(string)
            return None
        except Exception as ex:
            return str(ex)

