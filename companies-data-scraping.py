import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from io import StringIO

browser = webdriver.Chrome() # 크롬 브라우저 열기
browser.maximize_window() # 창 최대화

# 페이지 이동
url_kospi = "https://finance.naver.com/sise/sise_market_sum.naver?&page=" # 코스피 url
url_kosdaq = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=" # 코스닥 url
browser.get(url_kosdaq)
time.sleep(1) # 브라우저에 내용 로드 완료 위해, 1초 휴식

# 조회 항목 초기화(즉 체크된 항목 초기화)
check_boxes = browser.find_elements(By.NAME, "fieldIds")

for check_box in check_boxes:
    if check_box.is_selected(): # 만약 체크박스가 체크가 된 상태라면
        check_box.click() # 체크 해제

# 원하는 조회 항목 선택
want_to_select = ["시가총액", "PER", "ROE", "PBR", "매출액증가율", "유보율"] # 최대 6가지 선택 가능
for check_box in check_boxes:
    parent = check_box.find_element(By.XPATH, "..") # 부모 태그 선택
    lable = parent.find_element(By.TAG_NAME, "label") # 부모 태그 내 lable이라는 자식 태그 선택
    if lable.text in want_to_select: # label 태그 이름이 원하는 항목 내 존재한다면
        check_box.click() # 해당 체크 박스 선택

# 적용하기 버튼 클릭
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()
time.sleep(1) # 1초 휴식


# 코스닥에 대해서
for i in range(1, 40 + 1): # 1 ~ 40 페이지까지 해당 작업 반복 # 24.04.x 코스닥 기준 35페이지(총 1722개의 기업)까지 존재
    # 페이지 넘어가기
    browser.get(url_kosdaq + str(i))

    # 데이터 추출
    data_frame = pd.read_html(StringIO(browser.page_source))[1] # 1번째 인덱스에 해당하는 테이블 내용
    data_frame.dropna(axis='index', how='all', inplace=True) # 테이블 내 행(row)의 내용이 존재하지 않는면 삭제 후 적용
    data_frame.dropna(axis='columns', how='all', inplace=True) # 테이블 내 열(column)의 내용이 존재하지 않는면 삭제 후 적용
    if len(data_frame) == 0: # 특정 페이지 내의 내용이 존재하지 않는다면
        break # 반복 작업 끝

    # CSV 파일로 저장 # 엑셀로 파일 로드 가능
    file_name = "kospi_kosdaq_companies.csv"
    if os.path.exists(file_name): # 이미 파일이 존재한다면
        data_frame.to_csv(file_name, encoding='utf-8-sig', index=False, mode='a', header=False) # 테이블 헤더(테이블 내 맨 위 상단 제목) 내용이 존재한다면 header 추가 없이 테이블 내용만 해당 파일에 append
    else: # 파일이 존재하지 않는다면 
        data_frame.to_csv(file_name, encoding='utf-8-sig', index=False) # 테이블 header 내용 추가하여 새로운 파일로 저장.
    print("{} 페이지 완료".format(i))


# 코스피에 대해서
for i in range(1, 50 + 1): # 1 ~ 50 페이지까지 해당 작업 반복 # 24.06.x 코스피 기준 45페이지(총 2212개의 기업)까지 존재
    # 페이지 넘어가기
    browser.get(url_kospi + str(i))

    # 데이터 추출
    data_frame = pd.read_html(StringIO(browser.page_source))[1] # 1번째 인덱스에 해당하는 테이블 내용
    data_frame.dropna(axis='index', how='all', inplace=True) # 테이블 내 행(row)의 내용이 존재하지 않는면 삭제 후 적용
    data_frame.dropna(axis='columns', how='all', inplace=True) # 테이블 내 열(column)의 내용이 존재하지 않는면 삭제 후 적용
    if len(data_frame) == 0: # 특정 페이지 내의 내용이 존재하지 않는다면
        break # 반복 작업 끝

    # CSV 파일로 저장 # 엑셀로 파일 로드 가능
    file_name = "kospi_kosdaq_companies.csv"
    if os.path.exists(file_name): # 이미 파일이 존재한다면
        data_frame.to_csv(file_name, encoding='utf-8-sig', index=False, mode='a', header=False) # 테이블 헤더(테이블 내 맨 위 상단 제목) 내용이 존재한다면 header 추가 없이 테이블 내용만 해당 파일에 append
    else: # 파일이 존재하지 않는다면 
        data_frame.to_csv(file_name, encoding='utf-8-sig', index=False) # 테이블 header 내용 추가하여 새로운 파일로 저장.
    print("{} 페이지 완료".format(i))

browser.quit()