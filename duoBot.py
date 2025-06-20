from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

class duoBot():
    def __init__(self) -> None:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=2560")
        options.add_argument("--height=1440")
        self.browser = webdriver.Firefox(options=options)
        self.bts = {
            "continue": "._1rcV8",
            "startStory": "._3fmUm",
        }
        self.bxs = {
            0: "li._25kWt:nth-child(1) > button:nth-child(1)",
            1: "li._25kWt:nth-child(2) > button:nth-child(1)",
            2: "li._25kWt:nth-child(3) > button:nth-child(1)",
        }
        self.opts = {
            0: "span._1KFAk:nth-child(4) > span:nth-child(1) > button:nth-child(1) > span:nth-child(2) > span:nth-child(1)",
            1: "span._1KFAk:nth-child(6) > span:nth-child(1) > button:nth-child(1) > span:nth-child(2) > span:nth-child(1)",
            2: "span._1KFAk:nth-child(10) > span:nth-child(1) > button:nth-child(1) > span:nth-child(2) > span:nth-child(1)",
            3: "span._1KFAk:nth-child(12) > span:nth-child(1) > button:nth-child(1)"
        }
        self.matchListL = [
            "ul._2j-c3:nth-child(1) > li:nth-child(1) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(1) > li:nth-child(2) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(1) > li:nth-child(3) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(1) > li:nth-child(4) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(1) > li:nth-child(5) > span:nth-child(1) > button:nth-child(1)",
        ]
        self.matchListR = [
            "ul._2j-c3:nth-child(2) > li:nth-child(1) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(2) > li:nth-child(2) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(2) > li:nth-child(3) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(2) > li:nth-child(4) > span:nth-child(1) > button:nth-child(1)",
            "ul._2j-c3:nth-child(2) > li:nth-child(5) > span:nth-child(1) > button:nth-child(1)",
        ]

    def cssClick(self, path, click=True):
        btn, c = None, 0
        while not btn:
            c+=1
            try:    btn = self.browser.find_element(By.CSS_SELECTOR, path)
            except NoSuchElementException:
                time.sleep(0.1)
                if c > 500:     return btn
        if click:
            try:    btn.click()
            except ElementClickInterceptedException:    return None
        return btn

    def getCookies(self):
        cookieDict = {}
        self.browser.get("https://www.duolingo.com/?isLoggingIn=true")
        time.sleep(30)
        print("10 second warning")
        time.sleep(10)
        for cookie in self.browser.get_cookies():
            cookieDict[cookie['name']] = cookie['value']
        return cookieDict
    
    def loadCookies(self, cookies):
        self.browser.get("https://www.duolingo.com")
        for name, value in cookies.items():
            self.browser.add_cookie({'name': name, 'value': value})
        self.browser.refresh()
        time.sleep(5)

    def repeatContinue(self, n):
        for i in range(n):
            time.sleep(4)
            self.cssClick(self.bts["continue"])
    
    def buttonSpam(self, n, type = "boxes"):
        if type == "boxes":
            dict = self.bxs
        elif type == "options":
            dict = self.opts
        for i in range(n):
            self.cssClick(dict[i])
    
    def match(self):
        for i in self.matchListL:
            for j in self.matchListR:
                self.cssClick(i)
                self.cssClick(j)
                time.sleep(0.5)
                self.cssClick(j)
                self.cssClick(i)
                time.sleep(0.5)

    def storyTime(self):
        self.browser.get("https://www.duolingo.com/stories/fr-en-qu-est-ce-que-vous-voulez?mode=read")
        time.sleep(2)
        self.cssClick(self.bts["startStory"])
        self.repeatContinue(4)
        self.buttonSpam(2)
        self.repeatContinue(4)
        self.buttonSpam(3)
        self.repeatContinue(3)
        self.buttonSpam(3, type="options")
        self.repeatContinue(5)
        self.buttonSpam(3)
        self.repeatContinue(7)
        self.buttonSpam(3)
        self.repeatContinue(1)
        self.match()
        self.repeatContinue(3)

# TO GENERATE COOKIE DICT:
# swan = duoBot()
# print(swan.getCookies())
# paste output into dict below:
cookies = {}
print("Cookies secured")
duck = duoBot()
duck.loadCookies(cookies)
duck.storyTime()
duck.browser.quit()
