import urllib
import time

#scrape the main Wikipedia page of the historians in the list; this could be read in from an external file

#list of historians to be fetched

historians = ['%C3%89lie_Hal%C3%A9vy', 'A._E._Waite', 'A._H._M._Jones', 'A._J._P._Taylor', 'A._J._Taylor', 'A._L._Rowse', 'A._R._B._Haldane', 'A._R._B._Haldane', 'A._T._Q._Stewart']
url_stem = 'https://en.wikipedia.org/wiki/'

for historian in historians:

    full_url = url_stem + historian
    print("trying to get: " + full_url)#just to check it's working OK; it can fail if internet connection has a blip
    try:
        content = urllib.urlopen(full_url).read()
        f = open(historian + '.txt', 'w')
        f.write(content)
        f.close()
        time.sleep(3) # a pause between downloads is polite; 3 seconds might be excessive
    except ValueError:
        print("could not get "+historian)
        pass

              
