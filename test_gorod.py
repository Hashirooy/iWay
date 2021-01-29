from selenium import webdriver
import time
import allure
class TestChitaygorod:
    def setup(self):
        self.browser = webdriver.Chrome()

    def teardown(self):
        self.browser.quit()

    @allure.feature('Test chitGorod')
    @allure.story('Search field')
    def test_chitgorod(self):
        
        browser = self.browser.get('https://www.chitai-gorod.ru/')
        self.browser.title == "Читай-город — интернет-магазин книг"
        searchField = self.browser.find_element_by_name('q')
        searchField.send_keys('Тестирование')
        buttonSearch = self.browser.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[3]/div/form/button')
        buttonSearch.click()
        time.sleep(5)
        cardTree = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[3]')
        cardTreePrice = cardTree.get_attribute('data-productprice')
        cardTreeTitle = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[3]/div[2]/a/div[1]').text
        cardOne = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[2]')
        cardOnePrice = cardOne.get_attribute('data-productprice')
        cardOneTitle =self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[2]/div[2]/a/div[1]').text
        cardTwo = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[1]')
        cardTwoPrice = cardTwo.get_attribute('data-productprice')
        cardTwoTitle = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[1]/div[2]/a/div[1]').text
        buttOne = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[1]/div[2]/div[3]/button').click()
        buttTwo = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[2]/div[2]/div[3]/button').click()
        buttTree = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[3]/div[2]/div[3]/button').click()
        time.sleep(5)
        sumAllBook = int(cardOnePrice) + int(cardTwoPrice) + int(cardTreePrice)
        time.sleep(5)
        buttTree = self.browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div[2]/div[5]/div[3]/div[2]/div[3]/button').click()
        allBook = self.browser.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[3]/div/div[2]/div/a[1]/span[2]')
        basketOneBook = self.browser.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[1]').text
        basketTwoBook = self.browser.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[1]').text
        basketTreeBook = self.browser.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[1]/div[3]/div[3]/div/div[1]/div[1]/div[1]').text
        basketSum = self.browser.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[2]/div/div/div[2]/div[2]/span')
        assert int(basketSum.text) == sumAllBook
        assert allBook.text == '3'
        assert basketOneBook == cardTwoTitle and basketTwoBook == cardOneTitle and basketTreeBook == cardTreeTitle
        delBook = self.browser.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[1]/div[3]/div[3]/div/div[3]/div[2]').click()
        time.sleep(3)
        assert allBook.text == '2'
        assert(int(basketSum.text)) == sumAllBook - int(cardTreePrice)
        


