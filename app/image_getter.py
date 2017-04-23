import requests
from bs4 import BeautifulSoup
import urlparse

url = "https://www.walmart.com/ip/54649026"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")




def getImages():

    images = [];
    

    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        # print og_image['content']
        # print ''
        images = add_unique(og_image['content'],images)
        
    # This will look for a link tag with a rel attribute set to 'image_src'
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        # print thumbnail_spec['href']
        # print ''
        images = add_unique(thumbnail_spec['href'],images)
    
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
    #   print image % urlparse.urljoin("", img["src"])
    #   print urlparse.urljoin("", img["src"])
    #   print ''
       images = add_unique(urlparse.urljoin("", img["src"]),images) 
    #   images.append(urlparse.urljoin("", img["src"]))
       
    return images
    
    
def add_unique(string, lst):
    
    if string not in lst:
        lst.append(string)
        
    
    return lst
    
    

