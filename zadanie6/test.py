import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://localhost:3000/')
        self.assertIn('Przetargi - strona główna', self.browser.title)
        

class LinksTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title_new(self):
        self.browser.get('http://localhost:3000/')
        links=self.browser.find_elements("tag name", "a")
        self.assertEqual(8, len(links))
        names=["http://localhost:3000/","http://localhost:3000/tenders/open","http://localhost:3000/tenders/closed","http://localhost:3000/add"]*2
        for (name,link) in zip(names,links):
            self.assertEqual(name,link.get_attribute("href"))


class LinksNamesTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://localhost:3000/')
        
        self.assertEqual('http://localhost:3000/',self.browser.find_element("link text","Strona główna").get_attribute("href"))
        self.assertEqual('http://localhost:3000/tenders/open',self.browser.find_element("link text","Lista trwających przetargów").get_attribute("href"))
        self.assertEqual('http://localhost:3000/tenders/closed',self.browser.find_element("link text","Lista zakończonych przetargów").get_attribute("href"))
        self.assertEqual('http://localhost:3000/add',self.browser.find_element("link text","Dodaj przetarg").get_attribute("href"))


class MainTextTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_main_text(self):
        self.browser.get('http://localhost:3000/')
        text=self.browser.find_element("tag name", "p")
        self.assertEqual("Witaj w aplikacji internetowej umożliwiającej ogłaszanie i udział w przetargach.", text.text)


class AddEmptyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_add_empty(self):
        self.browser.get('http://localhost:3000/add')
        name_text_field=self.browser.find_element("id", "name")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.assertEqual("http://localhost:3000/add",self.browser.current_url)
        self.assertEqual("Dodaj przetarg",self.browser.find_element("tag name", "h1").text)

    
    
class AddRequiredTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_add_required(self):
        self.browser.get('http://localhost:3000/add')
        
        test_field=self.browser.find_element("id", "name")
        self.assertTrue(test_field.get_attribute("required"))

        test_field=self.browser.find_element("id", "institution")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("id", "description")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("id", "start_date")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("id", "start_hour")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("id", "end_date")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("id", "end_hour")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("name", "max_value")
        self.assertTrue(test_field.get_attribute("required"))


        
                
class AddReturnTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_add_return(self):
        self.browser.get('http://localhost:3000/add')
        
        self.assertEqual('http://localhost:3000/',self.browser.find_element("link text","## powrót do strony głownej ##").get_attribute("href"))


class TendersOpenTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_tenders_open(self):
        self.browser.get('http://localhost:3000/tenders/open')
        
        text=self.browser.find_element("tag name", "h1")
        self.assertEqual("Trwające przetargi",text.text)
        self.assertEqual("Trwające przetargi",self.browser.title)
        
        text=self.browser.find_element("tag name", "h2")
        self.assertEqual("Lista zakończonych przetargów",text.text)

        link_closed=self.browser.find_element("link text","Lista zakończonych przetargów").get_attribute("href")
        self.assertEqual("http://localhost:3000/tenders/closed",link_closed)


class TendersOpenTableTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_tenders_open_table(self):
        self.browser.get('http://localhost:3000/tenders/open')
        
        head=self.browser.find_elements("xpath","//table/thead/tr[1]/th")
        self.assertEqual(4,len(head))
        self.assertEqual("Id",head[0].text)
        self.assertEqual("Nazwa przedmiotu przetargu",head[1].text)
        self.assertEqual("Data i godzina rozpoczęcia zbierania ofert",head[2].text)
        self.assertEqual("Data i godzina zakończenia zbierania ofert",head[3].text)

        
class TendersClosedTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_tenders_closed(self):
        self.browser.get('http://localhost:3000/tenders/closed')
        
        text=self.browser.find_element("tag name", "h1")
        self.assertEqual("Zakończone przetargi",text.text)
        self.assertEqual("Zakończone przetargi",self.browser.title)
        
        text=self.browser.find_element("tag name", "h2")
        self.assertEqual("Lista trwających przetargów",text.text)

        link_open=self.browser.find_element("link text","Lista trwających przetargów").get_attribute("href")
        self.assertEqual("http://localhost:3000/tenders/open",link_open)


class TendersClosedTableTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_tenders_closed_table(self):
        self.browser.get('http://localhost:3000/tenders/closed')
        
        head=self.browser.find_elements("xpath","//table/thead/tr[1]/th")
        self.assertEqual(2,len(head))
        self.assertEqual("Id",head[0].text)
        self.assertEqual("Nazwa",head[1].text)


class AddTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_add(self):
        self.browser.get('http://localhost:3000/add')
        
        self.browser.find_element("id", "name").send_keys("Przetarg")
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2020-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2020-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.assertEqual("http://localhost:3000/add",self.browser.current_url)
        
        self.assertEqual("Sukces!",self.browser.find_element("tag name", "h1").text)
        self.assertEqual("Sukces!",self.browser.title)
        self.assertEqual("Dodanie przetragu o następujących danych zakończyło się sukcesem:",self.browser.find_element("tag name", "h2").text)
        
        
class AddOpenTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_add_open(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")
        self.assertEqual(4,len(body))
        self.assertEqual(name,body[1].text)
    
     
class DetailsTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_details(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")
        self.assertEqual(4,len(body))
        self.assertEqual(name,body[1].text) 
        
        link = self.browser.find_element("link text",name)
        link.click()
        
        self.assertEqual("Informacje szczegółowe o trwającym przetargu",self.browser.find_element("tag name", "h1").text)
        self.assertEqual("Informacje szczegółowe o trwającym przetargu",self.browser.title)


class DetailsTextTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_details_text(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        expected_names=["Nazwa przedmiotu przetargu:", "Nazwa instytucji zamawiającej:", "Opis przedmiotu przetargu:", "Data rozpoczęcia przetagu:", "Godzina rozpoczęcia przetagu:", "Data zakończenia przetagu:", "Godzina zakończenia przetagu:"]  
        names=self.browser.find_elements("tag name", "h3")
        for (name,expected_name) in zip(names,expected_names):
            self.assertEqual(expected_name,name.text)
        


class DetailsButtonTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_details_button(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        button=self.browser.find_element("tag name", "button")
        button.click()
        
        self.assertIn("http://localhost:3000/offer/",self.browser.current_url)
        self.assertEqual("Dodaj ofertę w przetargu",self.browser.find_element("tag name", "h1").text)


class OfferEmptyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_offer_empty(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        button=self.browser.find_element("tag name", "button")
        button.click()
        
        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.assertIn("http://localhost:3000/offer/",self.browser.current_url)
        self.assertEqual("Dodaj ofertę w przetargu",self.browser.find_element("tag name", "h1").text)

    
class OfferRequiredTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_offer_required(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        button=self.browser.find_element("tag name", "button")
        button.click()
        
        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        test_field=self.browser.find_element("id", "name")
        self.assertTrue(test_field.get_attribute("required"))
        
        test_field=self.browser.find_element("name", "value")
        self.assertTrue(test_field.get_attribute("required"))
        
        
        
class OfferAddTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_offer_add(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        button=self.browser.find_element("tag name", "button")
        button.click()
        
        self.browser.find_element("id", "name").send_keys("Składający")
        self.browser.find_element("name", "value").send_keys("10023")
        
        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.assertIn("http://localhost:3000/offer/",self.browser.current_url)
        
        self.assertEqual("Sukces!",self.browser.find_element("tag name", "h1").text)
        self.assertEqual("Sukces!",self.browser.title)
        self.assertEqual("Dodanie oferty o następująch danych do przetargu zakończyło się sukcesem:",self.browser.find_element("tag name", "h2").text)
        
        
class OfferAddNegativeTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_offer_add_negative(self):
        self.browser.get('http://localhost:3000/add')
        
        name="Przetarg"
        
        self.browser.find_element("id", "name").send_keys(name)
        self.browser.find_element("id", "institution").send_keys("Instytucja")
        self.browser.find_element("id", "description").send_keys("Opis przetargu")
        self.browser.find_element("id", "start_date").send_keys("2000-02-22")
        self.browser.find_element("id", "start_hour").send_keys("01:06")
        self.browser.find_element("id", "end_date").send_keys("2999-05-22")
        self.browser.find_element("id", "end_hour").send_keys("05:06")
        self.browser.find_element("name", "max_value").send_keys("12345")

        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.browser.get('http://localhost:3000/tenders/open')
        
        body=self.browser.find_elements("xpath","//table/tbody/tr[1]/td")

        link = self.browser.find_element("link text",name)
        link.click()
        
        button=self.browser.find_element("tag name", "button")
        button.click()
        
        self.browser.find_element("id", "name").send_keys("Składający")
        self.browser.find_element("name", "value").send_keys("-12345")
        
        button=self.browser.find_element("css selector", "input[value='Prześlij']")
        button.click()
        
        self.assertEqual("Dodaj ofertę w przetargu",self.browser.find_element("tag name", "h1").text)
        self.assertEqual("Dodaj ofertę w przetargu",self.browser.title)
        
        


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(OfferAddNegativeTestCase("test_offer_add_negative"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    
    unittest.main(verbosity=2)
    
    
    
    
    