import pandas as pd
import requests
import os

def translate_column(df, column_index):
    texts = df.iloc[:, column_index].tolist()
    translated_texts = []
    for text in texts:
        try:
            response = requests.post(
                'https://api.deepl.com/v2/translate',
                # 이 코드는 환경변수에서 API 키를 받아옵니다. 환경변수에 DEEPL_API_KEY를 생성하세요.
                headers={'Authorization': f'Bearer {os.environ.get("DEEPL_API_KEY")}'},
                data={
                    'text': text,
                    'source_lang': source_lang,
                    'target_lang': target_lang,
                }
            )
            response.raise_for_status()
            translated_texts.append(response.json()['translations'][0]['text'])
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 403:
                raise ValueError(f"403 Forbidden error: {e}")
            else:
                raise

    return translated_texts

def translate_csv_file(file_path: str, source_lang: str, target_lang: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, encoding='utf-8')
    df = df.map(str)  

    
    df.replace('\n', ' ', regex=True, inplace=True)

    
    try:
        df.iloc[:, 0] = translate_column(df, 0)
    except ValueError as e:
        print(e)
        exit(1)

    return

# 파일 경로를 지정합니다.
file_path = 'file_name.csv'

# 번역할 언어를 지정합니다.
source_lang = 'ja'
target_lang = 'ko'

# 번역을 수행합니다.
df = translate_csv_file(file_path, source_lang, target_lang)

# 번역된 CSV 파일을 저장합니다.
df.to_csv('translated_file_name.csv', encoding='utf-8')
