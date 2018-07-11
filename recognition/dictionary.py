import random
str_bml=input().split(',')
tag=str_bml[0]
text=str_bml[1]
behaviour_service={'tag_1':["bml_1.bml","bml_2.bml"],'tag_2':["bml_3.bml","bml_4.bml"]}
def SelectBehaviour(behaviour_service,tag):
    emotion=behaviour_service[tag]
    return random.choice(emotion)
print(SelectBehaviour(behaviour_service,tag))
with open (SelectBehaviour(behaviour_service,tag),'r') as file:
    x=file.read()
    a=x.replace("<speech>","<speech>"+text)
print(a)
with open ('bml.bml','w') as f_file:
    f_file.write(a)
file.close()
f_file.close()