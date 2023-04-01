import requests
from bs4 import BeautifulSoup
 
# exam paramter examples: AMC_8, AJHSME, AMC_10A, AMC_12B, AHSME, AIME_I
def get_problem(year, exam, problem):
    link = f'https://artofproblemsolving.com/wiki/index.php/{year}_{exam}_Problems/Problem_{problem}'
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.body.find('div', id= 'page-wrapper')
    soup= soup.find('div', id= 'main-content')
    soup = soup.find('div', id = 'main-column')
    soup = soup.find('div', class_= 'page-wrapper')
    soup = soup.find('div', class_= 'mw-body')
    soup = soup.find('div', id= 'mw-content-text')
    soup = soup.find('div', class_= 'mw-parser-output')
    soup = soup.find_all('p')[0]
    return soup.prettify()
