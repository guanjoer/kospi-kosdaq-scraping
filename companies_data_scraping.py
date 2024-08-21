import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from io import StringIO
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y_%m_%d")

browser = webdriver.Chrome()
browser.maximize_window() 

url_kospi = "https://finance.naver.com/sise/sise_market_sum.naver?&page=" # 코스피 url
url_kosdaq = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=" # 코스닥 url
browser.get(url_kosdaq)
time.sleep(1)

# 조회 항목 초기화(즉 체크된 항목 초기화)
check_boxes = browser.find_elements(By.NAME, "fieldIds")

for check_box in check_boxes:
    if check_box.is_selected(): # 만약 체크박스가 체크가 된 상태라면
        check_box.click()

# 조회하고자 하는 항목(최대 6개)
want_to_select = ["시가총액", "PER", "ROE", "PBR", "매출액증가율", "유보율"]
for check_box in check_boxes:
    parent = check_box.find_element(By.XPATH, "..") # 부모 태그
    lable = parent.find_element(By.TAG_NAME, "label") # 부모 태그 내 lable이라는 자식 태그
    if lable.text in want_to_select: # label 태그 이름이 조회하고자 하는 항목 내 존재한다면
        check_box.click() 

# 적용하기 버튼
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()
time.sleep(1)

# 데이터를 저장할 빈 데이터프레임 생성
final_data = pd.DataFrame()

# 코스닥
# 1 ~ 40 페이지 # 24.06월 기준 코스닥 기업 정보는 35페이지(총 1722개의 기업)까지 존재
for i in range(1, 40 + 1):
    browser.get(url_kosdaq + str(i))

    # 데이터 추출
    # 페이지 소스 코드 내 테이블 중 두번째 테이블(인덱스 1)
    data_frame = pd.read_html(StringIO(browser.page_source))[1]

    # 결측값 제거 # 테이블 내 행 또는 열의 내용이 모두 결측값 일 때 기존의 data frame 수정
    data_frame.dropna(axis='index', how='all', inplace=True) 
    data_frame.dropna(axis='columns', how='all', inplace=True)

    # 특정 페이지 내의 내용이 존재하지 않는다면
    if len(data_frame) == 0: 
        break # 반복 작업 끝

    final_data = pd.concat([final_data, data_frame], ignore_index=True)  # 데이터프레임에 추가
    print("[+] 코스닥 {} 페이지 완료".format(i))

# 코스피
# 1 ~ 50 페이지 # 24.06월 기준 코스피의 기업 정보는 45페이지(총 2212개의 기업)까지 존재
for i in range(1, 50 + 1):
    browser.get(url_kospi + str(i))

    data_frame = pd.read_html(StringIO(browser.page_source))[1]
    data_frame.dropna(axis='index', how='all', inplace=True) 
    data_frame.dropna(axis='columns', how='all', inplace=True)

    if len(data_frame) == 0: 
        break 

    final_data = pd.concat([final_data, data_frame], ignore_index=True)
    print("[+] 코스피 {} 페이지 완료".format(i))

# 엑셀 파일로 저장
file_name = f"public_companies_{formatted_date}.xlsx"
final_data.to_excel(file_name, index=False)

browser.quit()
