def parse(query: str) -> dict:
    dict1={}
    find =query[query.rfind("/")+1:]
    list1 =["name","color","age"]
    for i in find:
        if not i.isalnum() :
            find=find.replace(i," ")
    a=find.split(" ")
    for el in a:
        if el in list1:
            dict1[el]=a[a.index(el)+1]

    return dict1
import unittest

class TestParse(unittest.TestCase):

    def test_name(self):
        res=parse('https://example.com/path/to/page?name=ferret')
        self.assertEqual(res,{'name': 'ferret'})
# print(parse('https://example.com/path/to/page?name=ferret&color=purple'))
# print(parse('https://example.com/path/to/page?name=ferret&color=purple&'))
# print(parse('http://example.com/'))
# print(parse('http://example.com/?'))
# print(parse('https://example.com/path/to/page?name=ferret&color=purple&age=18'))
# print(parse('http://example.com/?name=Dima'))