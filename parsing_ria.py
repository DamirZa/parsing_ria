import feedparser

pars_from_ria="https://ria.ru/export/rss2/archive/index.xml"

p=feedparser.parse(pars_from_ria)

# Выводим основную информацию об RSS канале
print(p.feed.title)
print(p.feed.link)
print(p.feed.description)
print('nuber of items is ',len(p.entries))

# Выводим информацию без использования двумерного массива. Поочередно (и через запятую) выводиться информация с каждого item (новости)
print('number of item, ','datepub of item, ','title of item, ','link of item')
for e in range(len(p.entries)):
    print('item №',e, end=', ')
    print(p.entries[e].published, end=', ')
    print(p.entries[e].title, end=', ')
    print(p.entries[e].link)

# Выводим информацию о item (новостях) в виде двумерного массива (предполагаю подойдет для использования в csv файлах)

feeds=[] # начало двумерного массива

nent=len(p.entries) # информация о количестве item (новостей)

for i in range(nent): # создаем двумерный массив
    feeds.append([i, p.entries[e].published, p.entries[e].title, p.entries[e].link])
print(feeds)