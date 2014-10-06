from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from .utils import http_get, tokenize_html, tokenize_query, perform_search


class UtilsTest(TestCase):
    def test_http_get(self):
        pass

    def test_tokenize_html(self):
        html = """
        <!doctype html>
        <title>Oh, hai!</title>
        <h1>Test case of the good, nice html5 text</h1>
        <p>Lorem ipsum, blah blah... Well, You know.</p>
        """
        tokens = [
            'oh', 'hai', 'test', 'case', 'of', 'the', 'good', 'nice', 'html5',
            'text', 'lorem', 'ipsum', 'blah', 'blah', 'well', 'you', 'know'
        ]

        self.assertEqual(tokenize_html(html), tokens)

        html = """
        <!doctype lol>
        <html>
            <head>
                <Title>Oh man, that's awful</title>
                <style>
                    * {
                        background: red;
                        color: yellow;
                    }
                </style>
            </head>
            <body>
                <!-- some annoying comment -->
                <a href="magnet:?xl=9663676416&dn=Boku&xt=...&mt=...">
                    <b>
                        MAKE SURE NOBODY IS AROUND YOU WHEN WATCHING IT!
                    </a>
                </b>
                <br>
                stray text goes here
            </body>
        """
        tokens = ['oh', 'man', "that's", 'awful', 'make', 'sure', 'nobody',
                  'is', 'around', 'you', 'when', 'watching', 'it', 'stray',
                  'text', 'goes', 'here']

        self.assertEqual(tokenize_html(html), tokens)

    def test_tokenize_query(self):
        tokens = tokenize_query("Hello, World!")
        self.assertEqual(tokens, ["hello", "world"])

    def test_perform_search(self):
        html = """
            <!doctype html>
            <h1>PROJECT DETAILS</h1>
            <p>We want you to build a very basic Django application that simply
            allows users to search a given URL for a given string. If the given
            string exists on the given URL, the app will return a successful
            response, and show the 10 words before and after the matched string
            (the surrounding text). All searches should be saved to the
            database.</p>
            <p>The app should also include a "view all" page, that shows each
            search string, the URL, and either "not found" or "successful"
            depending on the response.</p>
            <p>Example use case: Someone wants to use this simple application
            to search for the phrase "Bill Gates" on Yahoo Finance. They type
            "Bill Gates" into a form field, and type
            "https://finance.yahoo.com" into the second form field and click
            "Submit". If the phrase "Bill Gates" is found on the page, the
            application returns a success message, and also returns the text
            surround the search phrase.</p>
            <h1>REQUIREMENTS</h1>
            <ul>
                <li>Django 1.7</li>
                <li>Use the django-cookiecutter skeleton to setup the project
                quickly: <a>...</a>
                </li>
                <li>Deploy the working app to Heroku so we can verify it works
                as intended (docs here: <a>...</a>, the free default dyno is
                fine)</li>
                <li>Push your finished code to a public repository for review
                (Bitbucket or Github)</li>
            </ul>
            <h2>Desired Options:</h2>
            <ul>
                <li>The max_length for the string input should be 100 chars.
                Proper escaping should be considered.</li>
                <li>The homepage should just link to the search page, no
                homepage styling or content is necessary.</li>
            </ul>
            <p>And that's it! This is just a simple app so we can get an idea
            of your coding style, efficiency, and how familiar you are with
            some other tools we commonly use. If you are a seasoned Django
            developer, this should be very easy.</p>
        """
        query = "Bill Gates"
        begin = ['to', 'use', 'this', 'simple', 'application', 'to', 'search',
                 'for', 'the', 'phrase']
        keywords = ['bill', 'gates']
        end = ['on', 'yahoo', 'finance', 'they', 'type', 'bill', 'gates',
               'into', 'a', 'form']

        self.assertEqual((begin, keywords, end), perform_search(query, html))

