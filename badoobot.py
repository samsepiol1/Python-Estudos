from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
class Badoo:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://badoo.com/pt/"
    def nav(self):
        self.driver.get(self.url)
    def actions(self):
        return self.driver.find_element_by_xpath('//div[@class="auth-button auth-button--fcbk"]').click()
    def login_feicc(self):
        self.url1="https://www.facebook.com"
        self.driver.get(self.url1)
        barra_pesquisa1=self.driver.find_element_by_id('email')
        barra_pesquisa1.send_keys('steve.jkl5@gmail.com')
        barra_pesquisa2=self.driver.find_element_by_id('pass')
        barra_pesquisa2.send_keys('imac88246948')
        barra_pesquisa3=self.driver.find_element_by_id('u_0_2')
        barra_pesquisa3.send_keys(Keys.ENTER)
    def Search_Girl_Guys(self):
        elen=self.driver.find_element_by_xpath('//a[@class="sidebar-menu__item"]').click()
        print(elen)
        return elen
    def Like_Act(self):
        elen2=self.driver.find_element_by_xpath('//div[@class="profile-header__info"]').click()
        return elen2
    def Show_Info(self):
        sauce=self.driver.page_source
        soup=BeautifulSoup(sauce,'lxml')
        for span in soup.find('span', class_ = 'js-location-label').get_text():
            print(span)
            
    def Like_Girl_or_Guy(self):
        elen=self.driver.find_element_by_xpath('i//[@class=]')
        

        
        
        
        
gg=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
c=Badoo(gg)
c.login_feicc()
time.sleep(2)
c.nav()
time.sleep(1)
c.actions()
time.sleep(60)
c.Like_Act()
time.sleep(30)
c.Show_Info()
time.sleep(2)
