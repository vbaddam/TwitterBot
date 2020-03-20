from selenium import webdriver
from time import sleep
from id import username, password


class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https:twitter.com')

        sleep(4)
        btn = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
        btn[0].click()

        email_id = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        email_id[0].send_keys(username)

        password = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        password[0].send_keys(password)

        login = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        login[0].click()
        
        for _ in range(100):
            tweet = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a/div')
            tweet[0].click()
            sleep(4)

            tw_content = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            tw_content[0].send_keys('#SSMB27 Please be careful and be isolated')

            send_tweet = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
            send_tweet[0].click()

            sleep(4)

if __name__ == "__main__":
    bot = TwitterBot()
    bot.login()