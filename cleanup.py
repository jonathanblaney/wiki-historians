from bs4 import BeautifulSoup
import re
import glob

# this cleans up the scraped HTML files in situ and ovewrites the original content

list = glob.glob(r'*.txt') #get all the appropriate txt files from the directory
 
for historian in list: 
    f = open(historian)
    content = f.read()
    f.close
    
    print(content)
	
	
    soup = BeautifulSoup(content, 'html.parser')
    cleaner_content = soup.get_text()#strip out the HTML elements
    clean_content = cleaner_content.encode('utf-8')#switch encoding, otherwise there are write problems later
    #manual cleaning steps:
    clean_content = re.sub(r"\[edit\]", "", clean_content)
    clean_content = re.sub(r"\nmw\..+", "", clean_content)
    clean_content = re.sub(r"\n/\*.+", "", clean_content)
    clean_content = re.sub(r"\n{", "", clean_content)
    clean_content = re.sub(r"\n}", "", clean_content)
    clean_content = re.sub(r"\nif\(window.+", "", clean_content)
    clean_content = re.sub(r"\na:lang.+", "", clean_content)
    clean_content = re.sub(r"document\.write.+", "", clean_content)
    clean_content = re.sub(r".+Jump to.+navigation.+search", "", clean_content)
    clean_content = re.sub(r"\n\n", "\n", clean_content)
    clean_content = re.sub(r"\n\n", "\n", clean_content)
    clean_content = re.sub(r"\n\n", "\n", clean_content)
    clean_content = re.sub(r"\n\n", "\n", clean_content)
    f = open(historian, 'w')
    f.write(clean_content)
    f.close()
 
    


