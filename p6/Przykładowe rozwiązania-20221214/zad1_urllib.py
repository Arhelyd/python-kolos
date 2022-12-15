from urllib.request import urlopen, Request
from re import match
from xml.dom import minidom


response = urlopen(Request('http://www.money.pl/rss/',
                   headers={'User-Agent': 'MyAgent'}))

money_xml = response.read()
xmldoc = minidom.parseString(money_xml)

items = xmldoc.getElementsByTagName("item")
for item in items:
    titles = item.getElementsByTagName("title")
    print(titles[0].firstChild.wholeText)

    descs = item.getElementsByTagName("description")
    tekst = descs[0].firstChild.wholeText
    matchObj = match(r'<.*>(.*)', tekst.strip())
    if matchObj:
        print(f"   {(matchObj.group(1))}")

    links = item.getElementsByTagName("link")
    print(f"    {(links[0].firstChild.wholeText)}\n")
