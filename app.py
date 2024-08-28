from bs4 import BeautifulSoup
import requests
import sqlite3


DATA_FILE = 'data.db'

def page_scraper(url):
    res = requests.get(url)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.tbody

    rank_list = [elem.get_text() for elem in data.find_all(class_='rank-td')]
    name_list = [elem.get_text().strip() for elem in data.find_all(class_='company-name')]
    code_list = [elem.get_text() for elem in data.find_all(class_='company-code')]
    country_list = [elem.get_text() for elem in data.find_all(class_='responsive-hidden')]
    mc_list = [
        elem.get_text() for elem in data.find_all(class_='td-right')
        if elem.find('span') and '$' in elem.find('span').get_text()
    ]
    companies_data = []
    for i in range(100):
        companies_data.append((rank_list[i], name_list[i], code_list[i], country_list[i], mc_list[i]))
    
    return companies_data


def init_db():
    conn = sqlite3.connect(DATA_FILE)
    cur = conn.cursor()
    
    cur.execute('''
        DROP TABLE IF EXISTS companies
    ''')
    
    cur.execute('''
        CREATE TABLE companies (
            rank INT,
            name TEXT,
            code TEXT,
            country TEXT,
            market_cap TEXT
        )
    ''')
    
    conn.close()


def populate_db():
    urls = [
        'https://companiesmarketcap.com/',
        'https://companiesmarketcap.com/page/2/',
        'https://companiesmarketcap.com/page/3/',
        'https://companiesmarketcap.com/page/4/',
        'https://companiesmarketcap.com/page/5/'
    ]
    companies_data = []
    
    for url in urls:
        companies_data += page_scraper(url)
        
    conn = sqlite3.connect(DATA_FILE)
    cur = conn.cursor()
    cur.executemany('''
        INSERT INTO companies (rank, name, code, country, market_cap)
        VALUES (?, ?, ?, ?, ?)
    ''', companies_data)
    conn.commit()
    conn.close()


def view_db():
    conn = sqlite3.connect(DATA_FILE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM companies')
    data = cur.fetchall()
    print(data)

init_db()
populate_db()
view_db()
