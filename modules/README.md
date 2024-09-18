**1.** `kospi_kosdaq_scraping.py` 


**코스피, 코스닥에 상장되어 있는 모든 기업**의 ***시가총액***, ***매출액 증가율***, ***PER***, ***ROE***, ***PBR***, ***유보율*** 데이터를 [네이버 증권](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)에서 가져와 `csv` 파일로 저장시킵니다. 

---

**2.** `filtering_with_excel.py` 


**필터링 된 기업의 목록**만을 가져와 `xlsx` 파일에 저장합니다. 필터링 조건은 아래와 같습니다. 

- **PER 15 이하**
- **PBR 4 이하**
- **ROE 10 이상**
- **매출액 증가율 20 이상**

---

**3.** `filtering_with_streamlit.py`


`streamlit`을 이용하여 **4개의 지표**를 이용하여 주식 목록을 필터링하여 보여줍니다. 해당 지표는 아래와 같습니다.

- **ROE(이상)**
- **매출액 증가율(이상)**
- **PBR(이하)**
- **PER(이하)**