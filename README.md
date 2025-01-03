# 한국 주식 데이터 스크래핑 및 필터링

해당 도구는 [네이버 증권](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)에서 코스피와 코스닥에 상장된 기업의 데이터를 스크래핑하고, 해당 데이터를 `Python`의 **Streamlit**을 이용하여 5가지 지표(`ROE`, `PBR`, `PER`, `PSR`, `Sales Growth Rate`)를 사용자가 필터링하여, 필터링 된 주식 목록을 대시보드에 보여주는 기능을 제공한다.


## Features

- **KOSPI & KOSDAQ 데이터 스크래핑**: 네이버 증권으로부터 **시가 총액**, **ROE**, **PBR**, **PSR**, **PER**, **매출액**, **매출액 증가율** 데이터 스크래핑
- **`CSV` 및 `JSON` 파일:** 스크래핑 한 주식 데이터는 `CSV` 파일로 저장되며, 또한 **Streamlit**에서의 편한 조작을 위해 `CSV` 파일을 `JSON` 파일로 변환
- **데이터 필터링:** `Streamlit`의 사이드 바를 통해 **ROE, PBR, PER, PSR, 매출액 증가율** 총 5가지의 지표를 사용자가 필터링 할 수 있는 기능 제공
- **Streamlit Dashboard:** 필터링 된 주식 목록과 모든 주식 목록을 Streamlit Dashboard를 통해 표시 


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

1. **주식 데이터 스크래핑:** `app.py`를 실행하여 Streamlit 대시보드를 확인해보면, **"Update to Latest Data"** 버튼이 존재하고, 만약 최신 데이터가 아닐 경우, 해당 버튼을 눌러 네이버 증권으로부터 스크래핑을 진행하여 최신 데이터로 업데이트가 가능하다. 그리고 스크래핑을 진행하여 저장된 `CSV` 파일은 `csv_files/` 디렉토리 내에 저장된다.

2. **주식 목록 필터링:** 사이드 바에 존재하는 **ROE, 매출액 증가율, PBR, PER, PSR** 지표를 사용자가 필터링 할 수 있고, 필터링 된 주식 목록은 **"FILTERED STOCK LIST""** 섹션에 표시된다.

3. **모든 주식 목록:** **"FILTERED STOCK LIST"** 섹션 아래에 **"ALL STOCK LIST"** 섹션이 존재하고, 해당 섹션에 필터링이 되지 않은, 코스피와 코스닥의 모든 주식 목록이 표시된다.


## Examples

**1.** `streamlit run app.py`로 애플리케이션 실행

**2.** (1)을 통해 필터링 기준을 선택하고, 선택한 주식 목록은 (2)에 표시된다. 만약 현재 최신 데이터가 아니라면 (3) 버튼을 눌러 데이터 업데이트를 진행

<img src="images/3.png" alt="Streamlit Dashboard 1" width="70%" />

**3.** 필터링 된 주식 목록이 아닌 모든 주식 목록을 보고 싶다면 아래의 **ALL STOCK LIST** 에서 확인

<img src="images/4.png" alt="Streamlit Dashboard 2" width="70%" />


## Project Structure

- **app.py:** 스크래핑, 데이터 변환, 필터링 기능, 대시보드를 제공하는 **Main Script**
- **csv_files/:** 주식 데이터 스크래핑을 진행하여 저장된 `CSV` 파일들이 저장되는 디렉토리
- **requirements.txt:** 해당 프로젝트에 필요한 Python 패키지(라이브러리)들의 목록


## License

This project is licensed under the MIT License