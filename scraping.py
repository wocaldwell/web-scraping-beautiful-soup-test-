import requests
from bs4 import BeautifulSoup

# the page being requested
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# HTML content of the page, formatted nicely
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# drilling down to a particular tag

# the html tag and its children
html = list(soup.children)[2]
# the body tag and its children
body = list(html.children)[3]
# the p tag
p = list(body.children)[1]
# print the contents of the p tag
print(p.get_text())




# Finding all instances of a tag at once
# Note that find_all returns a list, so we’ll have to loop through, or use list indexing, it to extract text
p_tag_list = soup.find_all('p')

for p_tag in p_tag_list:
    print(p_tag.get_text())




# Searching for tags by class and id

page_2 = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup_2 = BeautifulSoup(page_2.content, 'html.parser')
print(soup_2.prettify())

# search for any p tag that has the class outer-text
soup_2.find_all('p', class_='outer-text')

# any tag that has the class outer-text
soup_2.find_all(class_="outer-text")

# search for elements by id
first_id = soup_2.find(id="first")
print(first_id.get_text())




# searching a page via CSS selectors using the select method
# select method above returns a list of BeautifulSoup objects, just like find and find_all
div_p_list = soup_2.select("div p")
print(div_p_list)

for div_p in div_p_list:
    print(div_p.get_text())


# scrape rock quotes
quote_page = requests.get("http://www.notable-quotes.com/r/rock_n_roll_quotes.html")
souped_quote_page = BeautifulSoup(quote_page.content, 'html.parser')
# store list of quotes on page
quote_list = souped_quote_page.find_all(class_="quotation")

# print each quote
for quote in enumerate(quote_list, start=1):
    number = str(quote[0])
    text = quote[1].get_text()
    print(number + '. ' + text)