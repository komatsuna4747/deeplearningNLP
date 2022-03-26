import json
import re

import requests


def main():
    # Q20
    with open('nlp100/jawiki-country.json') as file:
        for line in file:
            line = json.loads(line)
            if line['title'] == 'イギリス':
                text_uk = line['text']
                break
    
    # print(text_uk)

    # Q21
    pattern = r'^(.*\[\[Category:.*\]\].*)$'
    result = '\n'.join(re.findall(pattern, text_uk, re.MULTILINE))
    print(result)

    # Q22
    pattern = r'^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$'
    result = '\n'.join(re.findall(pattern, text_uk, re.MULTILINE))
    print(result)

    # Q23
    pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
    result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text_uk, re.MULTILINE))
    print(result)

    # Q24
    pattern = r'\[\[ファイル:(.+?)\|'
    result = '\n'.join(re.findall(pattern, text_uk))
    print(result)

    # Q25
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, text_uk, re.MULTILINE + re.DOTALL)
    print(template)
    
    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
    for k, v in result.items():
        print(k + ': ' + v)

    # Q26
    def remove_markup(text):
        pattern = r'\'{2,5}'
        text = re.sub(pattern, '', text)
        
        return text
        
    result_rm = {k: remove_markup(v) for k, v in result.items()}
    for k, v in result_rm.items():
        print(k + ': ' + v)

    # Q27
    def remove_markup(text):
        pattern = r'\'{2,5}'
        text = re.sub(pattern, '', text)
        pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
        text = re.sub(pattern, r'\1', text)
        
        return text
        
    result_rm = {k: remove_markup(v) for k, v in result.items()}
    for k, v in result_rm.items():
        print(k + ': ' + v)

    # Q28
    def remove_markup(text):
        pattern = r'\'{2,5}'
        text = re.sub(pattern, '', text)

        pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
        text = re.sub(pattern, r'\1', text)

        pattern = r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+'
        text = re.sub(pattern, '', text)
        
        pattern = r'<.+?>' 
        text = re.sub(pattern, '', text)
        
        pattern = r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}' 
        text = re.sub(pattern, r'\1', text)
        
        return text
        
    result_rm = {k: remove_markup(v) for k, v in result.items()}
    for k, v in result_rm.items():
        print(k + ': ' + v)

    # Q29
    def get_url(text):
        url_file = text['国旗画像'].replace(' ', '_')
        url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
        data = requests.get(url)
        return re.search(r'"url":"(.+?)"', data.text).group(1)
        
    print(get_url(result))


if __name__ == '__main__':
    main()
