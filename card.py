import requests
import json
import Translate
import random


class Card:
    def __init__(self, name, type, text):
        self.name = str(name)
        self.type = str(type)
        self.text = str(text)


def search(card):
    url = "https://api.scryfall.com/cards/named"
    r = requests.get(url, params={"fuzzy": card})
    data = json.loads(r.text)

    if data["object"] != "card":
        print("fail")
    else:
        return data


def makeCard(data):
    name = data["name"]
    type_line = data["type_line"]
    oracle_text = data["oracle_text"]

    return Card(name, type_line, oracle_text)


languages = ("az", "sq", "am", "en", "ar", "hy", "af", "eu", "ba", "be", "bn", "my",
             "bg", "bs", "cy", "hu", "vi", "ht", "gl", "nl", "mrj", "el", "ka", "gu",
             "da", "he", "yi", "id", "ga", "it", "is", "es", "kk", "kn", "ca", "ky",
             "zh", "ko", "xh", "km", "lo", "la", "lv", "lt", "lb", "mg", "ms", "ml",
             "mt", "mk", "mi", "mr", "mhr", "mn", "de", "ne", "no", "pa", "pap", "fa",
             "pl", "pt", "ro", "ru", "ceb", "sr", "si", "sk", "sl", "sw", "su", "tg",
             "th", "tl", "ta", "tt", "te", "tr", "udm", "uz", "uk", "ur","fi", "fr",
             "hi", "hr", "cs", "sv", "gd", "et", "eo", "jv", "ja")


def translate(text, prior, count):
    lang = languages[random.randint(0, len(languages) - 1)]
    text = Translate.translate(text, prior, lang)

    if count == 0:
        return Translate.translate(text, lang, "en")

    return translate(text, lang, count - 1)


def main():
    card = str(input("Enter a card's name: "))

    card = search(card)

    card = makeCard(card)

    count = 20
    print(translate(card.name, "en", count))
    print(translate(card.type, "en", count))
    print(translate(card.text, "en", count))


main()
