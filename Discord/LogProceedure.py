# Local Script Inclusion

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



