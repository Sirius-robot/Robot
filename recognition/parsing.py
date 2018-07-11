# -*- coding: utf-8 -*-

from lxml import etree
	
def parseXML(xmlFile):
	with open(xmlFile, encoding = 'utf-8') as f_obj:
		xml = f_obj.read().encode('utf-8')
	root = etree.fromstring(xml)	
	l=[]
	for variant in root.getchildren():
		if not variant.text:
			text = "None"
		else:
			l.append(variant.text)
		print(l[0])

if __name__ == "__main__":
    parseXML("text.xml")