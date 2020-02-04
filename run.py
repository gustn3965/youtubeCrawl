import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd

saveNoPayName = "youtubeNoPay.csv"
savePayName = "youtubePay.csv"


# 현재 동영상 시간 가져오기.
def makeNumber(driver):
    driver2 = driver
    tex = driver2.find_element_by_xpath("//*[@id='movie_player']/div[23]/div[2]/div[1]/div/span[1]").text
    if len(tex.split(":")) == 2:
        minute = tex.split(":")[0]
        second = tex.split(":")[1]
        number = int(minute) * 60 + int(second)
        print(minute, '분', second, '초')
        return number
    else:
        hour = tex.split(":")[0]
        minute = tex.split(":")[1]
        second = tex.split(":")[2]
        number = int(hour) * 3600 + int(minute) * 60 + int(second)
        print(hour, '시간', minute, '분', second, '초')
        return number

# 유저아이디가 약 250개 넘어가면 차례대로 사라지므로
# 넘는다면 영상중지하고 저장.
def checkMaxList(driver):
    driver3 = driver
    html_source = driver3.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    userId = soup.select('yt-live-chat-author-chip > span#author-name ')
    if len(userId) > 200:
        driver3.switch_to_default_content()
        driver3.find_element_by_xpath("//*[@id='ytd-player']").click()
        print('userId 갯수 : ', len(userId))

        makeCSV(soup)

        return True

# 기존에 저장한 데이터와 비교하며 쌓아간다.

def checkRepeatNoPay(data2) :
    try :
        data1 = pd.read_csv(saveNoPayName, index_col=False, encoding='utf-8-sig')

        ind = 0
        for i in range(len(data2)):
            if data1.iloc[-1][0] == data2.iloc[i][0] and data1.iloc[-1][1] == data2.iloc[i][1]:
                print(i)
                ind = i
        data2 = data2.iloc[ind+ 1:]
        data2.to_csv(saveNoPayName, header=False, index=False, encoding='utf-8-sig', mode='a')
    except :
        print("저")
        data2.to_csv(saveNoPayName, header=False, index=False, encoding='utf-8-sig', mode='a')

def checkRepeatPay(data2) :
    try :
        data1 = pd.read_csv(savePayName, index_col=False, encoding='utf-8-sig')

        ind = 0
        for i in range(len(data2)):
            if data1.iloc[-1][0] == data2.iloc[i][0] and data1.iloc[-1][1] == data2.iloc[i][1]:
                print(i)
                ind = i
        data2 = data2.iloc[ind+ 1:]
        data2.to_csv(savePayName, header=False, index=False, encoding='utf-8-sig', mode='a')

    except :
        print("저")
        data2.to_csv(savePayName, header=False, index=False, encoding='utf-8-sig', mode='a')


# 데이터를 만든다.
def makeCSV(soup):
    youtube_userIDs = []
    youtube_userTime = []
    youtube_comments = []
    # youtube_pay = []

    youtube_pay_userIDs = []
    youtube_pay_userTime = []
    youtube_pay_comments = []
    youtube_pay = []

    userId = soup.select('yt-live-chat-author-chip > span#author-name ')
    userTime = soup.select('yt-live-chat-text-message-renderer > div#content > span#timestamp')
    userText = soup.select('yt-live-chat-text-message-renderer > div#content >  span#message  ')

    payUserAmount = soup.select('div#purchase-amount-column > div#purchase-amount')
    payUserText = soup.select('yt-live-chat-paid-message-renderer > div#card > div#content > div#message')
    payUserTime = soup.select(
        'yt-live-chat-paid-message-renderer > div#card > div#header > div#header-content > span#timestamp')
    payUserID = soup.select(
        'yt-live-chat-paid-message-renderer > div#card > div#header > div#header-content > div#header-content-primary-column > div#author-name')

    for i in range(len(userId)):
        youtube_userIDs.append(userId[i].text)
        youtube_userTime.append(userTime[i].text)
        youtube_comments.append(userText[i].text)
        # youtube_pay.append('no')

    for i in range(len(payUserID)):
        youtube_pay_userIDs.append(payUserID[i].text)
        youtube_pay_userTime.append(payUserTime[i].text)
        youtube_pay_comments.append(payUserText[i].text)
        youtube_pay.append(payUserAmount[i].text)

    pd_data = {"ID": youtube_userIDs, "Time": youtube_userTime, "Comment": youtube_comments}
    youtube_pd = pd.DataFrame(pd_data)

    # 기존 데이터 확인
    checkRepeatNoPay(youtube_pd)

    pd_data_pay = {"ID": youtube_pay_userIDs, "Time": youtube_pay_userTime, "Comment": youtube_pay_comments,
                   "Pay": youtube_pay}
    youtube_pd_pay = pd.DataFrame(pd_data_pay)

    # 기존 데이터 확인
    checkRepeatPay(youtube_pd_pay)



# 크롤링 시작
def startCrawl(url, driver):
    driver1 = driver


    time.sleep(1)
    print("url 변경 - ", url)
    driver1.get(url)
    driver1.implicitly_wait(1)

    time.sleep(3.0)
    driver1.switch_to.frame('chatframe')

    # 초과하는지 보고, 맞다면 데이터만들고 쓰고, 다시 크롤링 시작. ( 무한루프 )
    for i in range(600):
        time.sleep(2)
        if checkMaxList(driver1) == True:
            num = makeNumber(driver1)
            print(num)
            url2 = "https://youtu.be/D1dlajbv3s8?" + "t=" + str(num)
            print('초과되서 다시 시작. ', url2)

            startCrawl(url2, driver1)




driver = webdriver.Chrome("chromedriver.exe")
# 원하는 주소
driver.get("https://youtu.be/D1dlajbv3s8?t=1")
driver.implicitly_wait(1)
time.sleep(3.0)

# 로그인 클릭
driver.find_element_by_xpath(
    "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button").click()

time.sleep(2.0)
# 아이디 입력
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("id")
driver.find_element_by_xpath("//*[@id='identifierNext']").click()

# 비번 입력
time.sleep(2.0)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("password")
driver.find_element_by_xpath("//*[@id='passwordNext']").click()
time.sleep(3.0)

startCrawl("https://youtu.be/D1dlajbv3s8?t=1", driver)