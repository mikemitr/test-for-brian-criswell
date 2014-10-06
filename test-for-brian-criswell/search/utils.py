import re
import io
import requests
from lxml.html.clean import Cleaner
from lxml import etree


cleaner = Cleaner(page_structure=False, style=True)
parser = etree.HTMLParser()
word_splitter = re.compile(r"[\w']+")


def sublist(sublst, lst):
    if not (sublst and lst):
        return 0, 0

    size = len(sublst)

    for idx in (i for i, element in enumerate(lst) if element == sublst[0]):
        if lst[idx:idx + size] == sublst:
            return idx, idx + size

    return 0, 0


def http_get(url, timeout=15):
    try:
        response = requests.get(url, timeout=timeout)
    except:
        return None
    return response.text

def tokenize_html(html_page):
    words = []

    try:
        html = cleaner.clean_html(html_page)
        tree = etree.parse(io.StringIO(html), parser)
        root = tree.getroot()
    except etree.LxmlError:
        return words

    for text in root.itertext():
        words.extend(word_splitter.findall(text.lower()))

    return words


def tokenize_query(query):
    return word_splitter.findall(query.lower())


def perform_search(query, html_page, nearest=10):
    keywords = tokenize_query(query)
    words = tokenize_html(html_page)
    begin, end = sublist(keywords, words)

    if begin == end:
        return (None, None, None)

    return words[begin - nearest:begin], keywords, words[end:end + nearest]
