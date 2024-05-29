import requests
import json


def get_tractate_pages(tractate, num_dafs):
    pages = []
    for i in range(2, num_dafs + 1):
        pages.append(f"{tractate}.{i}a")
        pages.append(f"{tractate}.{i}b")
    return pages

def get_gemara_sections():
    

    talmud_tractates_daf_count = {
    "Berakhot": 64,
    "Shabbat": 157,
    "Eruvin": 105,
    "Pesachim": 121,
    "Yoma": 88,
    "Sukkah": 56,
    "Beitzah": 40,
    "Rosh Hashanah": 35,
    "Taanit": 31,
    "Megillah": 32,
    "Moed Katan": 29,
    "Chagigah": 27,
    "Yevamot": 122,
    "Ketubot": 112,
    "Nedarim": 91,
    "Nazir": 66,
    "Sotah": 49,
    "Gittin": 90,
    "Kiddushin": 82,
    "Bava Kamma": 119,
    "Bava Metzia": 119,
    "Bava Batra": 176,
    "Sanhedrin": 113,
    "Makkot": 24,
    "Shevuot": 49,
    "Avodah Zarah": 76,
    "Horayot": 14,
    "Zevachim": 119,
    "Menachot": 110,
    "Chullin": 142,
    "Bekhorot": 61,
    "Arakhin": 34,
    "Temurah": 34,
    "Keritot": 27,
    "Meilah": 21,
    "Tamid": 10,
    "Middot": 10,
    "Kinnim": 3,
    "Niddah": 73
    }
    sections = []
    for tractate, pages in talmud_tractates_daf_count.items():
        sections += get_tractate_pages(tractate,pages)
    return sections

def get_commentary(part):
    endpoint = f"https://www.sefaria.org/api/texts/{part}"

    # Add parameters to include commentary
    params = {
        "commentary": 1,
        "context": 0,
        "pad": 0,
        "wrapLinks": 0
    }

    # Make the request
    response = requests.get(endpoint, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        # Access the commentaries
        commentaries = data.get('commentary')
        commentary_names = []
      
        for perush in commentaries:
            if(isinstance(perush,dict)):
            
                # print(perush['ref'])
                name = perush['ref']
                commentary_names.append(name)
        return commentary_names
            
    else:
        return("Error:", response.status_code, response.text)
