import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

#テキスト関連
st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

col1,col2=st.columns(2)

with col1:


    st.subheader('自己紹介')
    st.text('Pythonに関する情報をYouTube上で発信している')
    code = '''
    import streamlit as st

    st.title('サプーアプリ)
    '''

    st.code(code, language='python')


    #画像
    image = Image.open('AI_Image_20240429_093351_0.jpg')
    st.image(image, width=200)

    #動画
    video_file=open('coffee_movie.mp4','rb')
    video_bytes =video_file.read()
    st.video(video_bytes)



    with st.form(key='profile_form'):
        #テキストボックス
        name=st.text_input('名前')
        address=st.text_input('住所')

        #セレクトボックス
        age_category=st.selectbox(
            '年齢層',
            ('子ども(18歳未満)','大人(18歳以上)')
        )
        #ラジオ
        age_category=st.radio(
            '年齢層',
            ('子ども(18歳未満)','大人(18歳以上)')
        )

        #複数選択
        hobby=st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
        )

        #チェックボックス
        mail_subscribe=st.checkbox('メールマガジンを購読する')

        #スライダー
        height=st.slider('身長',min_value=100,max_value=250)

        #日付
        start_date=st.date_input( '開始日', datetime. date(2024,8,14))

        #カラーピッカー
        color=st.color_picker('テーマカラー','#00f900')


        #ボタン
        submit_btn=st.form_submit_button('送信')
        cancel_btn=st.form_submit_button('キャンセル')

        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
            st.text(f'年齢層:{age_category}')
            st.text(f'趣味:{",".join(hobby)}')


with col2:
    #データ分析関連
    df= pd.read_csv('Book2.csv',index_col='月')
    st.dataframe(df)#スクロール
    st.table(df) #ページ全体
    st.line_chart(df) #折れ線グラフ
    st.bar_chart(df['2021'])#棒グラフ

#matplotlib
fig, ax=plt.subplots()