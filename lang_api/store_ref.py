from requests_futures.sessions import FuturesSession
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import csv
def store_ref():
    '''Write the full table of country codes from standard maintener
    inside a db
    '''
    # db.dropCollection()

    session = FuturesSession()
    urls = ["http://id.loc.gov/search/?q=cs:http://id.loc.gov/vocabulary/iso639-2&start=%i"%i for i in range(1, 521, 20)]
    conn = MongoClient()
    db = conn.ref


    def store_results(future):
        response = future.result()
        headers = ["id", "label", "vocabulary","concept_type","subdivision","identifier"]
        # defaultdict.fromkeys(headers)
        data = bs(response.text, "lxml").find("tbody")
        #print(data)
        for i, n in enumerate(data.findAll("tr")):
            if i%2 == 1:
                pass
            else:
                # print(len(n.findAll("td")))
            # print([cell.text.strip() for cell in n.findAll("td")])
                doc = dict(zip(headers, [cell.text.strip() for cell in n.findAll("td")]))
                doc["labels"] = [n.strip() for n in doc["label"].split("|")]
                doc["default_label"] = {"en":doc["label"][0], "fr": doc["label"][1], "de":doc["label"][2]}
                doc["uri"] = "http://id.loc.gov/vocabulary/iso639-2/%s" %doc["identifier"]
                doc["date"] = [dt.today()]
                doc["author_uri"] = ["http://id.loc.gov/"]

                db.lang_ref.insert(doc)


    for url in urls:
        future = session.get(url)
        future.add_done_callback(store_results)



# def store_ref():
#     ref_exo = build_ref()
#     conn = MongoClient()
#     db = conn.ref
#     db.lang_ref.insert_many(ref_exo)

def build_bnf():
    '''construire le référentiel de la BNF
    {"fre":[Label1, Label2, Label3, ...]}
    '''
    ref = {}
    with open("./data/code_lang_BNF.csv", "r", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            labels = row['Libellé'].replace(".", "",).split(" => ")
            label = labels[0]



            try:
                ref[row["Code"]]["labels"].append(label)
            except KeyError:
                ref[row["Code"]]= {"labels":[label]}
            try:
                ref[row["Code"]]["default_label"] = {"fr":labels[1]}
            except (IndexError,KeyError):
                ref[row["Code"]]["default_label"] = {"fr":label}


            ref[row["Code"]]["date"] = [dt.now()]

    return ref

def store_bnf():
    '''stocker le referentiel dans une BDD
    pour une première fois
    '''
    ref = build_bnf()
    conn = MongoClient()
    db = conn.ref
    for k, v in ref.items():

        db.lang_ref.update({"identifier": k},{
                    "identifier":k,"labels":v["labels"],
                    "default_label":v["default_label"],
                    "author_uri": "data.bnf.fr/vocabulary/codelang",
                    "date": v["date"]},
                    upsert=True)

if __name__ == '__main__':
    store_ref()
    store_bnf()
