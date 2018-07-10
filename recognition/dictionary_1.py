tag=input()
text=input()
import random
behaviour_service={'tag_1':["bml_1.bml","bml_2.bml"],'tag_2':["bml_3.bml","bml_4.bml"]}
def behaviourService(behaviour_service,tag,text,filename):
    file=open(random.choice(behaviour_service[tag]),'r').read()
    new_file=open(filename,'w')
    new_file.write(file.replace("<speech>","<speech>"+text))
    print(file.replace("<speech>","<speech>"+text))
behaviourService(behaviour_service,tag,text,'bml.bml')