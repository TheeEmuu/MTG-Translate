import requests
import json


def translate(text, lang1, lang2):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    r = requests.get(url, params={
        "key": "trnsl.1.1.20181211T053706Z.44c320c33c3c2cab.ed3481602e189cfe3774bcae9da1d059d948b85a",
        "text": text,
        "lang": lang1 + "-" + lang2})

    data = json.loads(r.text)
    return data["text"][0]


translate("hello", "en", "es")
