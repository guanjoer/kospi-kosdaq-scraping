import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from io import StringIO
import pandas as pd
import csv
import json
from datetime import datetime
import streamlit as st


now = datetime.now()
formatted_date = now.strftime("%Y_%m_%d")
directory = "./csv_files"
csv_file = f"{directory}/public_companies_{formatted_date}.csv"
json_file = f"data_{formatted_date}.json"
default_json_file = "data.json"  # 기본 JSON 파일

# 1. 기업 데이터 스크래핑 후 CSV 파일로 저장
@st.cache_data
def scrape_companies_data():
    if not os.path.exists(directory):
        os.makedirs(directory)

    browser = webdriver.Chrome()
    browser.maximize_window()

    url_kospi = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
    url_kosdaq = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page="
    browser.get(url_kosdaq)
    time.sleep(1)

    check_boxes = browser.find_elements(By.NAME, "fieldIds")
    for check_box in check_boxes:
        if check_box.is_selected():
            check_box.click()

    want_to_select = ["시가총액", "PER", "ROE", "PBR", "매출액증가율", "유보율"]
    for check_box in check_boxes:
        parent = check_box.find_element(By.XPATH, "..")
        label = parent.find_element(By.TAG_NAME, "label")
        if label.text in want_to_select:
            check_box.click()

    btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
    btn_apply.click()
    time.sleep(1)

    final_data = pd.DataFrame()

    for i in range(1, 40 + 1):
        browser.get(url_kosdaq + str(i))
        data_frame = pd.read_html(StringIO(browser.page_source))[1]
        data_frame.dropna(axis='index', how='all', inplace=True)
        data_frame.dropna(axis='columns', how='all', inplace=True)
        if len(data_frame) == 0:
            break
        final_data = pd.concat([final_data, data_frame], ignore_index=True)

    for i in range(1, 50 + 1):
        browser.get(url_kospi + str(i))
        data_frame = pd.read_html(StringIO(browser.page_source))[1]
        data_frame.dropna(axis='index', how='all', inplace=True)
        data_frame.dropna(axis='columns', how='all', inplace=True)
        if len(data_frame) == 0:
            break
        final_data = pd.concat([final_data, data_frame], ignore_index=True)

    final_data.to_csv(csv_file, index=False, encoding='utf-8-sig')
    browser.quit()
    return csv_file

# 2. CSV 파일을 JSON으로 변환
def csv_to_json(csv_f, json_f):
    with open(csv_f, mode='r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]

    with open(json_f, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"CSV to JSON conversion completed! {json_f}")

# 3. Streamlit을 통해 필터링 된 기업 목록 보여주기
def show_dashboard(json_file):
    def load_data(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return pd.DataFrame(data)

    df = load_data(json_file)

    df['ROE'] = pd.to_numeric(df['ROE'], errors='coerce')
    df['PBR'] = pd.to_numeric(df['PBR'], errors='coerce')
    df['PER'] = pd.to_numeric(df['PER'], errors='coerce')
    df['유보율'] = pd.to_numeric(df['유보율'], errors='coerce')

    df_filtered = df.drop(['N', '현재가', '전일비', '액면가'], axis=1)

    st.sidebar.header('필터링 기준 선택')

    roe_threshold = st.sidebar.slider('ROE (이상)', min_value=0, max_value=100, value=20, step=1)
    sales_growth_threshold = st.sidebar.slider('매출액 증가율 (이상)', min_value=0, max_value=100, value=25, step=1)
    pbr_threshold = st.sidebar.slider('PBR (이하)', min_value=0.0, max_value=15.0, value=3.0, step=0.1)
    per_threshold = st.sidebar.slider('PER (이하)', min_value=0, max_value=100, value=20, step=1)

    filtered_df = df_filtered.copy()
    filtered_df = filtered_df[filtered_df['ROE'] >= roe_threshold]
    filtered_df = filtered_df[filtered_df['매출액증가율'].str.rstrip('%').astype(float) >= sales_growth_threshold]
    filtered_df = filtered_df[filtered_df['PBR'] <= pbr_threshold]
    filtered_df = filtered_df[filtered_df['PER'] <= per_threshold]

    filtered_df['ROE'] = filtered_df['ROE'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
    filtered_df['유보율'] = filtered_df['유보율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
    filtered_df['매출액증가율'] = filtered_df['매출액증가율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
    filtered_df['시가총액'] = filtered_df['시가총액'].apply(lambda x: f"{int(float(x))}억" if pd.notnull(x) else "")

    df['시가총액'] = df['시가총액'].apply(lambda x: f"{int(float(x))}억" if pd.notnull(x) else "")
    df['ROE'] = df['ROE'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
    df['유보율'] = df['유보율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
    df['매출액증가율'] = df['매출액증가율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")

    st.subheader('FILTERED STOCK LIST')
    st.write(filtered_df)

    df_full = df.drop(['N', '현재가', '전일비', '액면가'], axis=1)

    st.subheader('ALL STOCK LIST')
    st.write(df_full)


def main():
    st.title("KOSPI & KOSDAQ STOCK DASHBOARD")

    if st.button('Update to Latest Data'):
        csv_file = scrape_companies_data()
        csv_to_json(csv_file, json_file)
        os.replace(json_file, default_json_file)
        st.success(f"Updated with The Latest Data!")

    # Display default JSON file(data.json)
    if os.path.exists(default_json_file):
        last_modified_time = datetime.fromtimestamp(os.path.getmtime(default_json_file))
        
        if last_modified_time.date() == datetime.now().date():
            st.success("It is Currently Displaying The Latest Data.")
        else:
            st.info("Displaying the default data. Hit the button to get the latest data.")

        show_dashboard(default_json_file)
    else:
        st.warning(f"The {default_json_file} file does not exist, please scrape the data.")

if __name__ == "__main__":
    main()
