from bs4 import BeautifulSoup

recognition_result=open("bml.bml",mode="r")
soup=BeautifulSoup(recognition_result,"lxml")
text_0=[str(x).replace("<speech>","").replace("</speech>","") for x in soup.select("speech")]
text_1=[str(x).replace("<figure name=\"","").replace("</figure>","").replace("\">","") for x in soup.select("figure")]
text_2=[str(x).replace("<mouth ing=\"","").replace("</mouth>","").replace("\">","") for x in soup.select("mouth")]
text_3=[str(x).replace("<brows ing=\"","").replace("</brows>","").replace("\">","") for x in soup.select("brows")]
print(text_0,text_1,text_2,text_3)

