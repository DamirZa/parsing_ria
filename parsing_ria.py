import feedparser
pars_from_ria="https://ria.ru/export/rss2/archive/index.xml"
p=feedparser.parse(pars_from_ria)
# Выводим основную информацию об RSS канале:
print(p.feed.title)
print(p.feed.link)
print(p.feed.description)
print('nuber of items is ',len(p.entries))
# Выводим информацию из двумерного массива. Поочередно (и через запятую) выводиться информация с каждого item (новости):
print('number of item, ','datepub of item, ','title of item, ','link of item')
for e in range(len(p.entries)):
    print('item №',e, end=', ')
    print(p.entries[e].published, end=', ')
    print(p.entries[e].title, end=', ')
    print(p.entries[e].link)
nent=len(p.entries) # информация о количестве item (новостей)
array_of_news=[['number of item','datepub of item','title of item','link of item']]
for e in range(len(p.entries)):
    array_of_news.append([e, p.entries[e].published, p.entries[e].title, p.entries[e].link])
print(array_of_news)
# Выводим информацию о item (новостях) в csv файл:
import csv
with open('feeds_from_ria.csv', 'w', encoding='utf-8', newline='\n',) as filecsv:
    file_writer = csv.writer(filecsv,dialect='excel')
    file_writer.writerow(['number of item','datepub of item','title of item','link of item']) # названия столбцов
    for i in range(nent): # цикл перечисления информации об item (новостях) в RSS фиде:
        file_writer = csv.writer(filecsv,dialect='excel')
        number_of_item=i+1
        date_of_publishing=p.entries[i].published
        title_of_publishing=p.entries[i].title
        link_of_publishing=p.entries[i].link
        file_writer.writerow([number_of_item, date_of_publishing, title_of_publishing, link_of_publishing])