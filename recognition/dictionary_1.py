with open('start.bml') as file:
    "start.bml-file after chatbot"
    tag=str(file.readline()).split('=\'')[1].replace("'\n","")
    text=str(file.readline()).split('=\'')[1].replace("\'","")
import random
behaviour_service={'tag_1':["bml_1.bml","bml_2.bml"],'tag_2':["bml_3.bml","bml_4.bml"]}
def behaviourService(behaviour_service,tag,text):
    file=open(random.choice(behaviour_service[tag]),'r').read()
    x=file.replace("<speech>","<speech>"+text)
    return(x)
behaviourService(behaviour_service,tag,text)
