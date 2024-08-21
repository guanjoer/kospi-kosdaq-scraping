# Companies Data Scraping

**1.** `companies_data_scaping.py` 


**코스피, 코스닥에 상장되어 있는 모든 기업**의 ***시가총액***, ***매출액 증가율***, ***PER***, ***ROE***, ***PBR***, ***유보율*** 데이터를 [네이버 증권](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)에서 가져와 `xlsx` 파일로 저장시킵니다. 

---

**2.** `filtering_companies.py` 


**필터링 된 기업의 목록**만을 가져와 `xlsx` 파일에 저장합니다. 필터링 조건은 아래와 같습니다. 

- **PER 15 이하**
- **PBR 4 이하**
- **ROE 10 이상**
- **매출액 증가율 20 이상**


# Usage

**1.** `companies_data_scaping.py`는 **코스피, 코스닥에 상장된 모든 기업**을 가져옵니다. 조회하고자 하는 항목을 바꾸기 위해서는 아래의 항목 중에서 선택하여서 아래 코드의 리스트에 바꿔 넣어주시면 됩니다. 


> **시가총액, 자산총계, 부채총계, 매출액, 매출액증가율, 영업이익, 영업이익증가율, 당기순이익, 주당순이익, 보통주배당금, PER, ROE, ROA, PBR, 유보율**

```python

# 조회하고자 하는 항목(최대 6개)
want_to_select = ["시가총액", "PER", "ROE", "PBR", "매출액증가율", "유보율"]
for check_box in check_boxes:
    parent = check_box.find_element(By.XPATH, "..") 
    lable = parent.find_element(By.TAG_NAME, "label") 
    if lable.text in want_to_select:
        check_box.click() 

```
---

**2.** `filtering_companies.py`는 **필터링 된 조건에 만족하는 기업의 목록**만을 가져와 `xlsx` 파일로 저장시킵니다. 필터링 된 조건을 바꾸기 위해서는 아래 코드에서 조건을 원하시는 조건으로 바꾸시면 됩니다.

```python

if all(column in data_frame.columns for column in ["PER", "ROE", "PBR", "매출액증가율"]):
	data_frame = data_frame[(data_frame['PER'] <= 15) & 
				(data_frame['PBR'] <= 4) & 
				(data_frame['ROE'] >= 10) & 
				(data_frame['매출액증가율'] >= 20)]

```