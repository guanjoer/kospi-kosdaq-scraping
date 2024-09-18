# KOSPI & KOSDAQ Stock Data Scraping and Filtering Dashboard

<!-- 해당 프로젝트는 [네이버 증권](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)에서 코스피와 코스닥에 상장된 기업의 데이터를 스크래핑하고, 해당 데이터를 **Streamlit**을 이용해 대시보드로 보여주는 도구를 제공합니다.

해당 도구는**ROE**, **PBR**, **PER**, **매출액 증가율**을 기준으로 주식 목록을 필터링 할 수 있으며, 앞선 4개의 재무 데이터 외 기업의 **유보율**, **시가 총액** 등의 데이터를 보여줍니다. -->

This project provides a tool for scraping **KOSPI** and **KOSDAQ** stock market data from [Naver Finance](https://finance.naver.com/sise/sise_market_sum.naver?&page=1) and displaying it in an interactive **Streamlit** dashboard. The data is **filtered** based on various financial metrics such as `ROE`, `PBR`, `PER`, and `sales growth rate`, allowing users to interactively refine their stock selection criteria.

## Features

- **Scraping KOSPI & KOSDAQ Data**: Fetches financial data such as `market capitalization`, `PER`, `ROE`, `PBR`, `sales growth rate`, and `reserve ratio` from the Naver Finance website.
- **CSV and JSON Export**: The scraped data is saved as a `CSV` file, which is also converted into `JSON` for easier manipulation and presentation in the dashboard.
- **Interactive Data Filtering**: Users can filter stocks based on financial metrics like `ROE`, `PBR`, and `sales growth rate` using **Streamlit's sidebar sliders**.
- **Streamlit Dashboard**: Presents both the filtered and full datasets interactively through a clean and simple dashboard.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kospi-kosdaq-scraping.git
   cd kospi-kosdaq-scraping
   ```

2. **Install dependencies:** Install the required Python libraries by running:
	```bash
	pip install -r requirements.txt
	```

3. **Run the application:** Start the Streamlit application with the following command:
	```bash
	streamlit run app.py
	```

## Usage

1. **Scrape Stock Data:** When you first load the app, you will have the option to update to the latest data by clicking the "Update to Latest Data" button. This will scrape data from Naver Finance and save it as a CSV file in the `csv_files/` directory.

2. **Filter Stocks:** Use the sliders in the sidebar to filter stocks based on specific criteria like ROE, sales growth rate, PBR, and PER.

3. **View Filtered and Full Data:**

- Filtered stock data based on the criteria is displayed under "Filtered Stock List".
- The full stock list, without filtering, is displayed under "Full Stock List".

## Project Structure

- **onefile.py:** The main script that handles scraping, data conversion, and dashboard display.
- **csv_files/:** Directory where the scraped CSV files are saved.
- **requirements.txt:** Contains the list of required Python packages for this project.

## How It Works

### Scraping Process

The application uses Selenium to automate web scraping from the Naver Finance website. The scraped data is processed into a DataFrame using Pandas and saved as a CSV file in the csv_files/ directory.

### Data Conversion

The CSV file is converted into a JSON format for easy manipulation in the Streamlit dashboard.

### Streamlit Dashboard

Streamlit is used to create an interactive dashboard. Users can filter the stocks by adjusting the sliders for ROE, sales growth, PBR, and PER values.

## Requirements

- Python 3.7+
- Required Python packages (listed in requirements.txt):
	- `pandas`
	- `selenium`
	- `streamlit`
	- `webdriver-manager`

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