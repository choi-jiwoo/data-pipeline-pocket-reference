from urllib.parse import urlsplit, parse_qs
import csv


url = ('https://www.mydomain.com/page-name?'
       'utm_content=textlink&utm_medium=social&utm_source=twitter&'
       'utm_campaign=fallsale')

split_url = urlsplit(url)
params = parse_qs(split_url.query)
parsed_url = []
all_urls = []

parsed_url.append(split_url.netloc)
parsed_url.append(split_url.path)

parsed_url.append(params['utm_content'][0])
parsed_url.append(params['utm_medium'][0])
parsed_url.append(params['utm_source'][0])
parsed_url.append(params['utm_campaign'][0])
all_urls.append(parsed_url)

export_file = 'data/export_url_parse_file.csv'

with open(export_file, 'w') as f:
    csvw = csv.writer(f, delimiter='|')
    csvw.writerows(all_urls)
