import wikipediaapi

class ContentsDisplay:
    
    def __init__(self, p_wiki):
        self.p_wiki = p_wiki
    
    def title(self):
        print(self.p_wiki.title)   
 
    def summary(self):
        print(self.p_wiki.summary[0:60])
    
    def all(self):
        print(self.p_wiki.text)
    

wiki = wikipediaapi.Wikipedia(
    language = 'ko', 
    extract_format = wikipediaapi.ExtractFormat.WIKI)
p_wiki = wiki.page('크롤링')


if p_wiki.exists():
    ContentsDisplay(p_wiki).all()
else:
    pass


