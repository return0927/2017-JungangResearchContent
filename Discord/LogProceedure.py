# Local Script Inclusion
from LogStrSplit import LogSplit

# Global Script Inclusion
import json, codecs, os
import dill as pickle


# Settings
if not "settings.dill" in os.listdir():
    # No setting file found, Create one
    class Setting:
        logDir = "./Logs/"
        logExt = "logs"
    pickle.dump(Setting, open("settings.dill","wb"), pickle.HIGHEST_PROTOCOL)
else:
    Setting = pickle.load(open("settings.dill","rb"))



logDir = os.listdir(Setting.logDir)

os.chdir(Setting.logDir)
for file in logDir:
    print("="*10,file,"="*10)
    with codecs.open(file, 'r', encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            #print(line[:-1])
            print(LogSplit.split(line[:-1]))