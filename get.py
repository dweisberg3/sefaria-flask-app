
import requests
import re


def remove_html_tags(text):
    # Regular expression to match HTML tags
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def get_tractate_pages(tractate, num_dafs):
    pages = []
    for i in range(2, num_dafs + 1):
        pages.append(f"{tractate}.{i}a")
        pages.append(f"{tractate}.{i}b")
    return pages

def fetch_page_content(page):
    url = f"https://www.sefaria.org/api/v3/texts/{page}?version=hebrew|Wikisource%20Talmud%20Bavli"
    response = requests.get(url)
    return response.json()


def get_text():
    talmud_tractates_daf_count = {
    "Berakhot": 64
   
}

    text = ""
    for tractate, page_num in talmud_tractates_daf_count.items():
           
            with open(f'{tractate.lower()}.txt', 'w') as textFile:
                pages = get_tractate_pages(tractate,page_num)
                # print(f'Mesechta : {tractate} . Num of Daf : {page_num} . Num of Pages : {len(pages)}')
                
                for page in pages:
                
                    content = fetch_page_content(page)
                    if "versions" in content:
                        content_no_html_tags = remove_html_tags((' '.join(content['versions'][0]['text'])))
                        page_name = page.split('.')
                        textFile.write(f'{page_name[0]} {page_name[1]} : \n')
                        textFile.write(f'{content_no_html_tags}\n')
                        text += f'{page_name[0]} {page_name[1]} : \n'
                        text += f'{content_no_html_tags}\n'
    return text
            
