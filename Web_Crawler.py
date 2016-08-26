import urllib2


response = urllib2.urlopen('https://web.whatsapp.com/')
html = response.read()
print html

  