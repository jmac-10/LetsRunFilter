from bs4 import BeautifulSoup
import csv
import urllib.request

# get page source and create a BeautifulSoup object based on it
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
base_url = 'https://www.letsrun.com/forum?page='
headers = {'User-Agent': user_agent}

cum_threads = {}
page_num = 1
while len(cum_threads) < 10000:
    print(f"reading page {page_num}...")
    # pull page
    request = urllib.request.Request(base_url + str(page_num), None, headers)
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page)

    # get thread titles and authors
    threads = soup.find_all(class_="subject font-sans-n tracking-tightish")
    threads = [thread.find('a').contents[0] for thread in threads]
    authors = [str(name.string) for name in soup.find_all(class_="author-name")][1:]

    # pair threads with authors and add to dataset
    thread_dict = dict(zip(threads, authors))
    cum_threads.update(thread_dict)

    page_num += 1

print("threads read, writing to csv...")

# write to csv
with open('threads.csv', 'w') as f:
    w = csv.writer(f)
    for thread in cum_threads:
        w.writerow([thread, cum_threads[thread], 0])

