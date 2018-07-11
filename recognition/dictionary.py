import random

behaviour_service={'tag_1':["bml_1.bml","bml_2.bml"],'tag_2':["bml_3.bml","bml_4.bml"]}

def behaviourService(behaviour_service,tag,text):
    #tag-key for search necessary array in dictionary; text- speech for robot(result of work chatbot)"
    file=open(random.choice(behaviour_service[tag]),'r').read()
    y=file.replace("<speech>","<speech>"+text)
    #y-str with finish commands for robot(speech,gesture)"
    return(y)
