import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd

def add_sentiment(df):
    df.loc[(df['star']>=4), 'label'] = 1
    df['label'] = df['label'].fillna(0)
    print(df.head())
    return df

if __name__ == "__main__":
   
    # wc.reviewdata_toCsv(urls)
    df = pd.read_csv(os.path.join(basedir, '앱리뷰csv파일.csv'))
    add_sentiment(df)
    df.to_csv('앱리뷰csv파일.csv', index=False, encoding='utf-8-sig')