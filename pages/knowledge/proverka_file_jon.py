import json
from collections import Counter

def proverka_json_file():
    """
    отдельный запуск файла, просто для информации
    """

    with open(r'PDN_new.json', encoding='utf-8') as f:
        pars = json.load(f)
        data = pars.get("knowledge")
    print(f"► Всего ссылок: {len(data)}")

    # поиск ломанных ссылок
    broken_link, count_broken_link = [], 0
    count_link_page = 0
    new_links_page = []
    for knowledge_link in data:
        new_links_page.append(knowledge_link.get("link_page"))
        if ("." or "alfa" or "//") in knowledge_link.get("link_page"):
            broken_link.append(knowledge_link.get("link_page"))
            count_broken_link+=1
        for key in knowledge_link:
            if "link_bz" in knowledge_link.get(key):
                link = (knowledge_link.get(key)).get("link_bz")
                new_links_page.append(link)
                if ('//' or "." or "alfa") in link:
                    broken_link.append(link)
                    count_broken_link += 1

    if count_broken_link !=0:
        print(f"► Есть ссылки для переделки в кол-ве: {count_broken_link}")
        for i in broken_link:
            print(i)


proverka_json_file()