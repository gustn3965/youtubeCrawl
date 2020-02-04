
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd

url = "https://www.youtube.com/watch?v=D1dlajbv3s8"
url = "https://youtu.be/D1dlajbv3s8?t=1051"
url = "https://youtu.be/D1dlajbv3s8?t=3774"
# url = "https://www.youtube.com/watch?v=tU2QUbL5EaI "
driver = webdriver.Chrome("chromedriver.exe")
# driver = webdriver.Chrome("/Users/hyunsu/Downloads/chromedriver")
sys.stdout = open('output.txt','w', -1,"utf-8")
driver.get(url)
driver.implicitly_wait(1)
last_height = driver.execute_script("return document.body.scrollHeight")
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")




# driver.commo
# last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
driver.implicitly_wait(4)
time.sleep(5.0)
time.sleep(20.0)


video = driver.find_element_by_xpath("//*[@id='ytd-player']")
# for i in range(1000) :
#     video.click()
#     video.click()
#     video.send_keys(Keys.ARROW_RIGHT)
#
#     time.sleep(2)





time.sleep(30.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)
time.sleep(120.0)

video.click()

#
# print("로그인!!!")
chatframe = driver.find_element_by_css_selector('iframe')

chatframe.send_keys(Keys.ARROW_RIGHT)

print(chatframe.get_attribute('id'))

chatframe = driver.find_element_by_xpath('//iframe')
print(chatframe.get_attribute('id'))

chatframe = driver.find_element_by_css_selector('iframe')
print(chatframe)

# print(len(chatframe))
# for iframe in chatframe:
#     print(iframe.get_attribute('name'))


driver.switch_to.frame('chatframe')


time.sleep(5.0)
html_source = driver.page_source
# print(html_source)
# driver.close()
soup = BeautifulSoup(html_source , 'lxml')

# print("---------")
print(soup)

# print(soup)
# print(soup)

youtube_userIDs = []
youtube_userTime = []
youtube_userDate = []
youtube_comments = []
youtube_pay = []

# chetList  = soup.select('yt-live-chat-text-message-renderer')

userId = soup.select('yt-live-chat-author-chip > span#author-name ')
userTime = soup.select('yt-live-chat-text-message-renderer > div#content > span#timestamp')
userText = soup.select('yt-live-chat-text-message-renderer > div#content >  span#message  ')
print('채팅 한 인원 id  : ',len(userId))
print('채팅 한 인원 tim : ',len(userTime))
print('채팅 한 인원 tx  : ',len(userText))


payUserAmount = soup.select('div#purchase-amount-column > div#purchase-amount')
payUserText = soup.select('yt-live-chat-paid-message-renderer > div#card > div#content > div#message')
payUserTime = soup.select('yt-live-chat-paid-message-renderer > div#card > div#header > div#header-content > span#timestamp')
payUserID =   soup.select('yt-live-chat-paid-message-renderer > div#card > div#header > div#header-content > div#header-content-primary-column > div#author-name')
# payUserID4 = soup.select('yt-live-chat-paid-message-renderer > div#card > div#header > div#header-content > div#purchase-amount-column')

print("후원한 인원d : ", len(payUserID))
print("후원한 인원tx : ", len(payUserText))
print("후원한 인원ti : ", len(payUserTime))
print("후원한 인원p : ", len(payUserAmount))

for i in range(len(userId)) :
    print(userId[i].text)
    print(userTime[i].text)
    print(userText[i].text)
    youtube_userIDs.append(userId[i].text)
    youtube_userTime.append(userTime[i].text)
    youtube_comments.append(userText[i].text)
    youtube_pay.append('no')


print('-----------')
for i in range(len(payUserID)) :
    print(payUserID[i].text)
    print(payUserAmount[i].text)
    print(payUserText[i].text)
    print(payUserTime[i].text)
    youtube_userIDs.append(payUserID[i].text)
    youtube_userTime.append(payUserTime[i].text)
    youtube_comments.append(payUserText[i].text)
    youtube_pay.append(payUserAmount[i].text)



pd_data = {"ID":youtube_userIDs, "Time" : youtube_userTime,"Date": youtube_userTime, "Comment":youtube_comments,"Pay" : youtube_pay }
youtube_pd = pd.DataFrame(pd_data)
# print(youtube_pd)
youtube_pd.to_csv('youtube채팅3.csv',index= False , encoding= 'utf-8-sig')



# youtube_time = soup.select('div#header-author > yt-formatted-string > a')
# youtube_comments = soup.select('yt-formatted-string#content-text')

# print(driver.find_element_by_xpath("ytd-comment-thread-renderer[1]/ytd-comment-renderer/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]").text)
# driver.find_element_by_xpath("//*[@id='ytd-player']").click()
# print(len(driver.find_elements_by_xpath("//yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer")))
# print(driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[1]/div[1]/span[2]").text)
# print(driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[2]/div[1]/span[2]").text)

# //*[@id="CkUKGkNNV2gxTk9GNE9ZQ0ZZOTNtQW9kQTVJRTRnEidDSi01OHVxRTRPWUNGWXlqV0FvZEVlVUxqdzE1Nzc4MDA3MDE2NjA%3D"]
# sys.stdout = open('output.txt','w', -1,"utf-8")
# driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[3]

# /div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string").click()

# /html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-viewer-engagement-message-renderer/div
# 20개가 나와야함.
# driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
# /html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[1]/div[1]/span[2]
# /html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[2]/div[1]
time.sleep(1.0)
# driver.execute_script("window.scrollTo(document.documentElement.scrollHeight, 0);")

#
# a = driver.find_elements_by_xpath('html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer')
#
# print(len(a))
# # time.sleep(0.5)
# # a[2].find_element_by_xpath(
# #     "div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string").click()
# b = driver.find_elements_by_xpath(
#     "//*[@id='replies']/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button")
# print(len(b))
#
# for i in b :
#     time.sleep(0.2)
#     i.click()


