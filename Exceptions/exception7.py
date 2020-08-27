"""
This is the another example of exception
"""

gold ={"US":46, "Fiji":1, "Great Britain":27 ,"cuba":5, "Thailand":2, "china":26,"France":10}
countries = ["Fiji", "chile","Mexico","France","Norway","US"]
country_gold = []

for country in countries:
    try:
        country_gold.append(gold[country])
    except KeyError:
        country_gold.append("Did not have gold")

for value in zip(countries, country_gold):
    print(value)