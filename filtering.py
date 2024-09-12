import streamlit as st
import pandas as pd
import json
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y_%m_%d")

# JSON 파일 로드
def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

# 데이터 로드
df = load_data(f'data_{formatted_date}.json')

# 숫자 데이터를 실수형으로 변환
df['ROE'] = pd.to_numeric(df['ROE'], errors='coerce')
df['PBR'] = pd.to_numeric(df['PBR'], errors='coerce')
df['PER'] = pd.to_numeric(df['PER'], errors='coerce')
df['유보율'] = pd.to_numeric(df['유보율'], errors='coerce')

df_filtered = df.drop(['N', '현재가', '전일비', '액면가'], axis=1)

# Streamlit 애플리케이션 제목
st.title('KOSPI & KOSDAQ 주식 필터링 대시보드')

# 사용자로부터 필터링 기준 선택
st.sidebar.header('필터링 기준 선택')

roe_threshold = st.sidebar.slider('ROE (이상)', min_value=0, max_value=100, value=20, step=1)
sales_growth_threshold = st.sidebar.slider('매출액 증가율 (이상)', min_value=0, max_value=100, value=25, step=1)
pbr_threshold = st.sidebar.slider('PBR (이하)', min_value=0.0, max_value=10.0, value=3.0, step=0.1)
per_threshold = st.sidebar.slider('PER (이하)', min_value=0, max_value=100, value=20, step=1)

# 선택한 기준을 이용한 필터링
filtered_df = df_filtered.copy()


# 조건에 맞는 데이터를 필터링
filtered_df = filtered_df[filtered_df['ROE'] >= roe_threshold]
filtered_df = filtered_df[filtered_df['매출액증가율'].str.rstrip('%').astype(float) >= sales_growth_threshold]
filtered_df = filtered_df[filtered_df['PBR'] <= pbr_threshold]
filtered_df = filtered_df[filtered_df['PER'] <= per_threshold]

# 종목명 선택 필터
# selected_stock = st.selectbox('종목을 선택하세요', filtered_df['종목명'].unique())

# 선택한 종목의 데이터 보여주기
# st.subheader(f'선택한 종목: {selected_stock}')
# stock_data = filtered_df[filtered_df['종목명'] == selected_stock]
# st.write(stock_data[['종목명', 'ROE', 'PBR', '매출액증가율', 'PER', '시가총액', '유보율']])


# 필터링 및 모든 데이터: %, 억 단위 추가
filtered_df['ROE'] = filtered_df['ROE'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
filtered_df['유보율'] = filtered_df['유보율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
filtered_df['매출액증가율'] = filtered_df['매출액증가율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
filtered_df['시가총액'] = filtered_df['시가총액'].apply(lambda x: f"{int(float(x))}억" if pd.notnull(x) else "")

df['시가총액'] = df['시가총액'].apply(lambda x: f"{int(float(x))}억" if pd.notnull(x) else "")
df['ROE'] = df['ROE'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
df['유보율'] = df['유보율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")
df['매출액증가율'] = df['매출액증가율'].apply(lambda x: f"{x}%" if pd.notnull(x) else "")

# 필터링 데이터 테이블 출력
st.subheader('필터링된 데이터')
st.write(filtered_df)

# 전체 데이터
st.subheader('전체 데이터')
st.write(df)
