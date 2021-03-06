from bs4 import BeautifulSoup

def dictionary_result(str_f):
    #str_f - variable after work def behaviourService
    soup=BeautifulSoup(str_f,'lxml')
    text_0=[str(x).replace("<speech>","").replace("</speech>","") for x in soup.select("speech")]
    text_1=[str(x).replace("<figure name=\"","").replace("</figure>","").replace("\">","") for x in soup.select("figure")]
    text_2=[str(x).replace("<mouth img=\"","").replace("</mouth>","").replace("\">","") for x in soup.select("mouth")]
    text_3=[str(x).replace("<brows img=\"","").replace("</brows>","").replace("\">","") for x in soup.select("brows")]
    text_4=[str(x).replace("<pupils percent=\"","").replace("</pupils>","").replace("\">","") for x in soup.select("pupils")]
    dict={'speech':text_0,'figure':text_1,'mouth':text_2,'brows':text_3,'pupils':text_4}
    return(dict)