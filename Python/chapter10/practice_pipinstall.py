## https://pypi.org/

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")    
# BeautifulSoup은 여러 parser(Ex. lxml, html.parser ..)를 지원하는데 그중에서 명확하게 html.parser를 지원한다는 것을 정해주기 위해서 features 키워드 인자를 사용한다. 
print(soup.prettify())

# pip list
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4