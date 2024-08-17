import pandas as pd
pd.DataFrame({
    '名前':{'佐藤','斎藤','鈴木'},
    '年齢':{21,30,18},
    '住所':{'東京都','岐阜県','埼玉県'},
    '血液型':{'A','B','o','AB'}

},index=['i-1','i-2','i-3'])

pd.Series({'佐藤','斎藤','鈴木'},
          index=({'佐藤','斎藤','鈴木'}))

df=pd.read_excel('表1.xlsx')