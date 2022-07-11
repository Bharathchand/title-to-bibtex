import requests
from habanero import Crossref
from habanero import cn	

def title2bib(title):
    title = title.lower()
    clean_title = ''.join(e for e in title if e.isalnum())
    cr = Crossref()
    res = cr.works(query_title=title, select="title,DOI", limit=5)
    for r in res['message']['items']:
        fetched_title = r['title'][0].lower()
        clean_fetched = ''.join(e for e in fetched_title if e.isalnum())
        if clean_fetched == clean_title:
            #print (type(r['DOI']))
            a = cn.content_negotiation(ids = r['DOI'], format = "bibtex")
            return a
            print (a)
            
f = open('title.txt','r')
Lines = f.readlines()



g = open ('bibtex.tsv','a')

for l in Lines:
	l = l[1:-3]
	print (l)
	g.write(l)
	g.write('\t')
	try:
		bib = title2bib(l)
		res = bib[ : -1]
		print (bib)
		g.write(res)
		#g.write('\n')
		g.write('\t')
		g.write('}')
	except TypeError:
		pass	
	g.write('\n')
	print ('\n')

