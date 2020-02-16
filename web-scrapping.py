
# making imports
from bs4 import BeautifulSoup
import requests
import csv


csv_file = open("H:\indeed-1.csv", 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "ratiing"])
# to build links for pagination
source = ["https://www.indeed.co.in/jobs?q=restaurant&l=Hyderabad%2C+Telangana"]
for i in range(1, 6):
    link = f'https://www.indeed.co.in/jobs?q=restaurant&l=Hyderabad%2C+Telangana&start={i}0'
    source.append(link)



d = 1
count = 0
# for-loop to scrape across different-pages
for link in source:
    page = requests.get(link).text
    soup = BeautifulSoup( page ,'lxml')

    for post in soup.find_all('div',attrs={"data-tn-component": "organicJob"}):

        title = post.find('div', class_="title").a.text
        if (post.find('div', class_="sjcl").find('div', class_='').find('span', class_="ratingsDisplay")):
            ratiing = post.find('div', class_="sjcl").find('div', class_='').find('span', class_="ratingsDisplay").a.span.text
        else:
            ratiing = "NA"
        count = count+1

        # print(f'title : {title.strip()}')
        # print(f'ratiing : {ratiing.strip()}')
        # print("-----------------") 
        csv_writer.writerow([title.strip(),ratiing.strip()])
    print(f"========page{d}-completed=========")
    d=d+1

print(f"total count:{count}")
csv_file.close()


