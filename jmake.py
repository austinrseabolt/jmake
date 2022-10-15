import sys
import os 
from bs4 import BeautifulSoup

with open(sys.argv[1], 'r') as html_file:
    soup = BeautifulSoup(html_file.read(), features='html.parser')

    #Add Load Static Tag
    head = soup.find('head')
    head.insert_before("{% load static %}")

    #Link Css/Links
    for link in soup.find_all("link", {"href":True}):
        if not "https" in str(link['href']):

            if "?v=" in link['href']:
                strippedlink = link['href'].split("?v=", 1)[0]
                link['href'] = strippedlink


            if "../" in link['href']:
                cleanedlink = link['href'].replace("../", "")
                newlink = str((str('"{% static "/') + cleanedlink + str('"%}"')))
                newlink = newlink[1:-1]
                link['href'] = newlink
            else:
                newlink = str((str('"{% static "/') + link['href'] + str('"%}"')))
                newlink = newlink[1:-1]
                link['href'] = newlink
                
        else:
            pass
    
        print('LINK: ' + link['href'])
    
    #Link Scripts
    for source in soup.find_all("script", {"src":True}):
        if not "https" in str(source['src']):

            if "?v=" in source['src']:
                strippedsrc = source['src'].split("?v=", 1)[0]
                source['src'] = strippedsrc

            if "../" in source['src']:
                cleanedsrc = source['src'].replace("../", "")
                newsrc = str((str('"{% static "/') + cleanedsrc + str('"%}"')))
                newsrc = newsrc[1:-1]
                source['src'] = newsrc
            else:
                newsrc = str((str('"{% static "/') + source['src'] + str('"%}"')))
                newsrc = newsrc[1:-1]
                source['src'] = newsrc
        
        print('SCRIPT: ' + source['src'])
    
    #Link Images
    for img in soup.find_all("img"):
        if not "https" in str(img['src']):
            if "../" in img['src']:
                cleanedsrc = img['src'].replace("../", "")
                newsrc = str((str('"{% static "/') + cleanedsrc + str('"%}"')))
                newsrc = newsrc[1:-1]
                img['src'] = newsrc
            else:
                newsrc = str((str('"{% static "/') + img['src'] + str('"%}"')))
                newsrc = newsrc[1:-1]
                img['src'] = newsrc
        print('IMG: ' + img['src'])

        

    # Store prettified version of modified html
    new_text = soup.prettify()

# Write new contents to test.html
with open('output.html', mode='w') as new_html_file:
    new_html_file.write(new_text)