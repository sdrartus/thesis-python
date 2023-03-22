import processText
import main

def cleanText(mess):
    proc = processText.processText(mess)
    pas = main.filter_profanity(proc)
    return pas
