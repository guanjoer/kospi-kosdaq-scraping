# 코스피 & 코스닥 데이터 스크래핑 및 필터링

해당 프로젝트는 [네이버 증권](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)에서 코스피와 코스닥에 상장된 기업의 데이터를 스크래핑하고, 해당 데이터를 **Streamlit**을 이용하여 4가지 지표(`ROE`, `PBR`, `PER`, `Sales Growth Rate`)를 사용자가 필터링하여 필터링 된 주식 목록을 대시보드에 보여주는 도구를 제공합니다.

<!-- This project provides a tool for scraping **KOSPI** and **KOSDAQ** stock market data from [Naver Finance](https://finance.naver.com/sise/sise_market_sum.naver?&page=1) and displaying it in an interactive **Streamlit** dashboard. The data is **filtered** based on various financial metrics such as `ROE`, `PBR`, `PER`, and `sales growth rate`, allowing users to interactively refine their stock selection criteria. -->

## Features

- **KOSPI & KOSDAQ 데이터 스크래핑**: 네이버 증권으로부터 **시가 총액**, **ROE**, **PBR**, **PER**, **매출액 증가율**, **유보율** 데이터를 스크래핑하여 가져옵니다.
- **`CSV` 및 `JSON` 파일:** 스크래핑 한 주식 데이터는 `CSV` 파일로 저장이 되며, 또한 **Streamlit**에서의 편한 조작을 위해 `CSV` 파일을 `JSON` 파일로 변환시키는 기능을 제공합니다.
- **데이터 필터링 기능:** Streamlit의 사이드 바를 통해 **ROE, PBR, PER, 매출액 증가율** 총 4가지의 지표를 사용자가 원하는 기준에 맞게 필터링이 가능합니다.
- **Streamlit Dashboard:** 필터링 된 주식 목록과 모든 주식 목록을 Streamlit Dashboard를 통해 보여줍니다. 

<!-- - **Scraping KOSPI & KOSDAQ Data**: Fetches financial data such as `market capitalization`, `PER`, `ROE`, `PBR`, `sales growth rate`, and `reserve ratio` from the Naver Finance website.
- **CSV and JSON Export**: The scraped data is saved as a `CSV` file, which is also converted into `JSON` for easier manipulation and presentation in the dashboard.
- **Interactive Data Filtering**: Users can filter stocks based on financial metrics like `ROE`, `PBR`, and `sales growth rate` using **Streamlit's sidebar sliders**.
- **Streamlit Dashboard**: Presents both the filtered and full datasets interactively through a clean and simple dashboard. -->

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/guanjoer/kospi-kosdaq-scraping.git
   cd kospi-kosdaq-scraping
   ```

2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```

3. **Run the application:**
	```bash
	streamlit run app.py
	```

## Usage

1. **주식 데이터 스크래핑:** `app.py`를 실행하면 **"Update to Latest Data"** 버튼이 존재하고, 만약 최신 데이터가 아닐 경우, 해당 버튼을 눌러 네이버 증권으로부터 스크래핑을 진행하여 최신 데이터로 교체할 수 있습니다. 스크래핑을 진행하여 저장된 CSV 파일은 `csv_files/ `디렉토리에 저장됩니다.

2. **주식 목록 필터링:** 사이드 바의 **ROE, 매출액 증가율, PBR, PER** 지표를 사용자가 필터링 할 수 있고, 필터링 된 주식 목록은 **"FILTERED STOCK LIST""** 섹션에 표시됩니다.

3. **모든 주식 목록:** **"FILTERED STOCK LIST"** 섹션 아래에 **"ALL STOCK LIST"** 섹션이 존재하고, 해당 섹션에 필터링이 되지 않은, 코스피와 코스닥의 모든 주식 목록이 표시됩니다.

<!-- 1. **Scrape Stock Data:** When you first load the app, you will have the option to update to the latest data by clicking the "Update to Latest Data" button. This will scrape data from Naver Finance and save it as a CSV file in the `csv_files/` directory.

2. **Filter Stocks:** Use the sliders in the sidebar to filter stocks based on specific criteria like ROE, sales growth rate, PBR, and PER.

3. **View Filtered and Full Data:**

- Filtered stock data based on the criteria is displayed under "Filtered Stock List".
- The all stock list, without filtering, is displayed under "All Stock List". -->

## Examples

1. `streamlit run app.py`로 애플리케이션 실행

2. (1)을 통해 필터링 기준을 선택하고, 선택한 주식 목록은 (2)에 표시된다. 만약 현재 최신 데이터가 아니라면 (3) 버튼을 눌러 데이터 업데이트를 진행

<img src="images/3.png" alt="Streamlit Dashboard 1" width="70%" />

3. 필터링 된 주식 목록이 아닌 모든 주식 목록을 보고 싶다면 아래의 **ALL STOCK LIST** 에서 확인

<img src="images/4.png" alt="Streamlit Dashboard 2" width="70%" />


## Project Structure

- **app.py:** 스크래핑, 데이터 변환, 필터링 기능, 대시보드를 제공하는 **Main Script** 입니다.
- **csv_files/:** 스크래핑을 진행하여 저장된 `CSV` 파일들이 저장되는 디렉토리입니다.
- **requirements.txt:** 해당 프로젝트에 필요한 Python 패키지들의 목록을 포함하고 있습니다.

<!-- - **app.py:** The main script that handles scraping, data conversion, and dashboard display.
- **csv_files/:** Directory where the scraped CSV files are saved.
- **requirements.txt:** Contains the list of required Python packages for this project. -->

<!-- ## How It Works

### Scraping Process

The application uses Selenium to automate web scraping from the Naver Finance website. The scraped data is processed into a DataFrame using Pandas and saved as a CSV file in the `csv_files/` directory.

### Data Conversion

The `CSV` file is converted into a `JSON` format for easy manipulation in the Streamlit dashboard.

### Streamlit Dashboard

Streamlit is used to create an interactive dashboard. Users can filter the stocks by adjusting the sliders for ROE, sales growth, PBR, and PER values.

## Requirements

- Python 3.7+
- Required Python packages (listed in requirements.txt):
	- `pandas`
	- `selenium`
	- `streamlit`
	- `webdriver-manager` -->

## License

This project is licensed under the MIT License

<!--
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

``` -->