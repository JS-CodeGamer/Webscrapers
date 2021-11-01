from bs4 import BeautifulSoup
import requests
from urllib.parse import quote


class job:
  
  def __init__(self, html_str):
    self.job_html = html_str
  
  def get_HTML(self):
    return self.job_html
  
  def get_details(self):
    _company_name = self.job_html.find('h3', class_ = "joblist-comp-name").text.replace("(More Jobs)", "").strip()
    _skills = self.job_html.find('span', class_ = 'srp-skills').text.strip()
    return (_company_name, _skills)

keywords = input("Input Skills, Designation etc...: ").strip()
keywords = quote(keywords)
website_html = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keywords}&txtLocation=').text
soup = BeautifulSoup(website_html, "html.parser")

jobs = [job(li) for li in soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")]


for curr_job in jobs:
 comapny, skills = curr_job.get_details()
 print("\033[1;44m Compay Name:\033[1;0m", comapny)
 print("\033[1;44m Skills Required:\033[1;0m", skills)
 print()