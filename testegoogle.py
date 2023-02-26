from selenium import webdriver

class Google:
    def __init__(self,driver):
        self.driver=driver
        self.url='http://google.com.br'
        self.search_bar='tsf' #id
        self.btn_search='btnK' #name
        self.btn_lucky='btnI' #name
        
        
    def navigate(self):
        self.driver.get(self.url)
    def search(self,word='None'):
        self.driver.find_element_by_id(self.search_bar).send_Keys(word)
        self.driver.find_element_by_name(self.btn_search).click()
        
gg=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
g=Google(gg)
g.navigate()
g.search('Live de Python')
