from pythonfuzz.main import PythonFuzz
from html.parser import HTMLParser


@PythonFuzz
def fuzz(buf):
    try:
        string = buf.decode("ascii")
        parser = HTMLParser()
        parser.feed(string)
    except UnicodeDecodeError:
        pass



if __name__ == '__main__':
    fuzz()
