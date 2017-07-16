import codecs, os, fnmatch
from time import time, strftime

def get(day, string)
    logdir = "C:\\KKuTu-Korea\\logs"
    scriptdir = os.getcwd()

    os.chdir(logdir)
    files = os.listdir()

    class toSearch:
        Day = day
        String = string


    outString = []

    for file in files:
        
        
        if fnmatch.fnmatch(file, '*-%s.log'%toSearch.Day):

            legacy = []
            
            with codecs.open(file, 'r', encoding='UTF-8') as f:
                line = f.readlines()

                for lineNum in range(len(line)):
                    if toSearch.String in line[lineNum]:
                        legacy.append("\t\tLine %d: %s" %(lineNum+1, line[lineNum].replace("\n","")))

            if len(legacy) == 0:
                pass
            else:
                outString.append("\t%s\\%s (%d hits)"%( os.getcwd(), file, len(legacy) ))
                outString += legacy

    return "\n".join(outString)
