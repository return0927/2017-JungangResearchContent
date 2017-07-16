# Local Script Inclusion

# Global Script Inclusion
import json, codecs, os
import pickle


# Settings
if not "settings.pickle" in os.listdir():
    # No setting file found, Create one
    class Setting:
        logDir = "./Logs/"
        logExt = "logs"

    pickle.dump(Setting, open("settings.pickle","wb"))
else:
    pickle.load(open("settings.pickle","rb"))