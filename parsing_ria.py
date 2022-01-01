import feedparser

pars_from_ria="https://ria.ru/export/rss2/archive/index.xml"

p=feedparser.parse(pars_from_ria)

print(p.feed.title)
print(p.feed.link)
print(p.feed.description)
print('nuber of items is ',len(p.entries))
print('number of item, ','datepub of item, ','title of item, ','link of item')
for e in range(len(p.entries)):
    print('item №',e, end=', ')
    print(p.entries[e].published, end=', ')
    print(p.entries[e].title, end=', ')
    print(p.entries[e].link)