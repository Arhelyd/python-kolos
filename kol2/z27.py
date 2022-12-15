from urllib.request import Request, urlopen
request_object = Request('http://python.org/', headers={'User-Agent': 'Mozilla'})
response = urlopen(request_object)
html=response.read()
print(html)