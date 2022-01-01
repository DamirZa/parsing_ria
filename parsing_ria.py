import feedparser

pars_from_ria="https://ria.ru/export/rss2/archive/index.xml"

p=feedparser.parse(pars_from_ria)

print(p.feed.title)
print(p.feed.link)
print(p.feed.description)
print('nuber of items is ',len(p.entries))
for e in range(len(p.entries)):
    print('item №',e)
    print(p.entries[e].title)
    print(p.entries[e].link)
    print(p.entries[e].published)