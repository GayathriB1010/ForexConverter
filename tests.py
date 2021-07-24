from app import app
from unittest import TestCase

class ForexConverterTestCase(TestCase):
    def test_forexConverterForm(self):
        with app.test_client() as client:
            res = client.get("/forex_form")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<h1>Forex Converter</h1>',html)

    def test_result(self):
        form_inputs = {"convertFrom":"USD",
                        "convertTo":"USD",
                        "amount":"1"}
        with app.test_client() as client:
            res = client.post("/result",data=form_inputs)
            self.assertEqual(res.status_code,200)
            html = res.get_data(as_text=True)
            self.assertIn('<p>The Result is: US$1.0</p>',html)

    def test_result2(self):
        form_inputs = {"convertFrom":"USD",
                        "convertTo":"USD",
                        "amount":" "}
        with app.test_client() as client:
            res = client.post("/result",data=form_inputs)
            self.assertEqual(res.status_code,302)
            self.assertEqual(res.location,'http://localhost/forex_form')

    def test_result3(self):
        form_inputs = {"convertFrom":" ",
                        "convertTo":"USD",
                        "amount":"50"}
        with app.test_client() as client:
            res = client.post("/result",data=form_inputs)
            self.assertEqual(res.status_code,302)
            self.assertEqual(res.location,'http://localhost/forex_form')

    def test_result4(self):
        form_inputs = {"convertFrom":"YYY",
                        "convertTo":"XXX",
                        "amount":"50"}
        with app.test_client() as client:
            res = client.post("/result",data=form_inputs)
            self.assertEqual(res.status_code,302)
            self.assertEqual(res.location,'http://localhost/forex_form')
        
   
    
