from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
# driver.implicitly_wait(15) #묵시적 대기, 작업 완료까지만 대기(15초까지 걸리는 거 아님)
time.sleep(5) #5초 대기
driver.get('https://google.co.kr')
time.sleep(5) 
driver.get('https:youtube.com/c/반원')
time.sleep(5)
driver.back() #뒤로 가기
time.sleep(5) 
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5) 
driver.forward()
# driver.fullscreen_window() #풀스크린
# time.sleep(5) 
# driver.set_window_rect(100,100,800,800) #창 크기 정하기
# time.sleep(5) 
# driver.maximize_window() #창 최대화
# time.sleep(5) 
driver.quit() #우리가 닫음







