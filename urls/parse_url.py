import requests


url_word = ['https://eleciz.ru/catalog/list/orgsteklo/','фторопласт']

def count_words_at_url(url_word):
    resp = requests.get(url_word[0])
    if resp.status_code==200:
        text = resp.text.lower().split()
        count = 0
        for word in text:
            if word.find(url_word[1])!=-1:
                count +=1
        return [url_word[0],count]
    return False


def update_url(url_update):


dd =count_words_at_url(url_word)
if dd:
    print(dd)
# print(count_words_at_url(url_word))