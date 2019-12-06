import requests
from bs4 import BeautifulSoup
import os

number = 1

for i in range(1, 826):
    url = "https://expressobeans.com/public/search.php?class=1&ipp=100&page={}" # We have 825 pages (with 100 posters each) to crawl through. Expecting 82448 total unique results.
    response = requests.get(url.format(i))
    
    if not response.ok:
        continue

    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    
    filename = "ebresults.txt"

    if os.path.exists(filename):
        append_or_write = 'a'
    else:
        append_or_write = 'w'

    results = open("ebresults.txt", append_or_write)
    for link in soup.find_all('a'):
        links = link.get('href')
        results.write(links + '\n')
        results.close # This file has a bunch of bullshit in it because I don't know how to code properly. I use bash to refine the results and write to a new shiny file, which is shared in a snippet.

    number += 1
