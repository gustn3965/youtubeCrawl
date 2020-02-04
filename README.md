# youtubeCrawl
Crawl youtube realtime chetting in the past 

# 유튜브 과거 실시간 채팅 크롤링하기.


# 현재 문제점 
- html구조가 바뀔 경우 에러 발생.
- 현금기부한 유저의 데이터는 겹치는 문제. 
- 영상이 다 끝난 후에는 에러 발생하기도 함. ( 대신 데이터는 저장. ) 



# 원리 

유튜브 프리미엄 아이디로 로그인한 후,

요청개수를 초과할 경우 영상 멈추고, 데이터 저장, 다시 영상 시작, 반복

영상을 시청하는 만큼 채팅을 가져오므로, 6시간동영상일 경우 6시간 프로그램 돌려야함.
처음에 영상 시작할때 재생속도를 2배로 할 경우 많이 단축됌. 

채팅데이터는  chatframe안에 있으므로 변경해줘야함. 

```
driver1.switch_to.frame('chatframe')
```



# 조건
Chromedriver.exe ( 폴더안에 있음. ) 

유튜브 프리미엄 아이디 있어야함. ( 중간에 광고 등 이유로 ) 



# 사용방법 
run.py 에서 최상단 saveNoPayName, savePayName 이름 변경 

하단에  # 원하는 주소 변경 
```
driver.get("https://youtu.be/D1dlajbv3s8?t=1")
```

하단에 id, password 변경 .

```
# 아이디 입력
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("id")
driver.find_element_by_xpath("//*[@id='identifierNext']").click()

# 비번 입력
time.sleep(2.0)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("password")
```

영상시작할 때 재생속도 2배로 변경 
