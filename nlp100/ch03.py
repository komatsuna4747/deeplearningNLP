import json
import re


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


if __name__ == '__main__':
    main()
