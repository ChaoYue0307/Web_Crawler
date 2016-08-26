import urllib2

def get_page_html(page_url):
    response = urllib2.urlopen(page_url)
    html = response.read()
    return html


url = "https://www.google.com.sg"
page = get_page_html(url)
print page

  