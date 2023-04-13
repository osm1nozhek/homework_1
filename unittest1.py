import unittest
def Parse(query: str) -> dict:
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
print(Parse('https://example.com/path/to/page?name=Dima&color=purple&age=18'))
class TestParse(unittest.TestCase):
    def test_name(self):
        res = Parse('https://example.com/path/to/page?name=ferret')
        self.assertEqual(res, {'name': 'ferret'})

    def test_color(self):
        res = Parse('https://example.com/path/to/page?color=purple')
        self.assertEqual(res, {'color': 'purple'})

    def test_age(self):
        res = Parse('https://example.com/path/to/page?age=18')
        self.assertEqual(res, {'age': '18'})

    def test_empty1(self):
        res = Parse('http://example.com/')
        self.assertEqual(res, {})

    def test_empty2(self):
        res = Parse('http://example.com/?')
        self.assertEqual(res, {})

    def test_combination1(self):
        res = Parse('https://example.com/path/to/page?name=ferret&age=18')
        self.assertEqual(res, {'name': 'ferret', 'age': '18'})

    def test_combination2(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple'})


    def test_combination3(self):
        res = Parse('https://example.com/path/to/page?color=purple&age=18')
        self.assertEqual(res, {'color': 'purple', 'age': '18'})

    def test_combination4(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple&age=18')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple', 'age': '18'})

    def test_combination5(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple&age=18&')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple', 'age': '18'})


if __name__ == '__main__':
    unittest.main()
