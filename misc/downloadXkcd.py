#! python3
# downloadXkcd.py - Downloads every single XKCD comic. From Automate the Boring Stuff



import requests, os, bs4, lxml

url = 'https://xkcd.com' #Starting url
os.makedirs('xkcd', exist_ok=True) #store comments in ./xkcd/
while not url.endswith('#'):
    #Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    
    #parse text
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    #Find the URL of comic
    comicElem = soup.select('#comic img')
    if comicElem ==[]:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        #Download the image 
        print('Downloading image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        #Save image
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close() 
        #previous url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' +prevLink.get('href')
    
print("Done.")