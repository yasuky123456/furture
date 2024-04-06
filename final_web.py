import pandas as pd
import streamlit as st
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt



video_file = open('point.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


data = pd.read_csv('命数表.csv', encoding='utf-8', index_col=0)
#st.write(data)
data2 = pd.read_csv('年代別属性.csv', encoding='utf-8', index_col=0)



year = st.text_input('西暦', placeholder='生まれた年入力', max_chars=10, help='数字を入れてね')
#moth = st.text_input('月', placeholder='生まれた月', max_chars=10)
moth_data =[" ","1","2","3","4","5","6","7","8","9","10","11","12"]
moth = st.selectbox('月', moth_data, index=0)

#day = st.text_input('日', placeholder='生まれた日', max_chars=10)
day_data =[" ","1","2","3","4","5","6","7","8","9","10","11","12",
           "13","14","15","16","17","18","19","20","21","22","23",
           "24","25","26","27","28","29","30","31"]
day = st.selectbox('日', day_data, index=0)

options1 = [" ","男性", "女性"]
sel1 = st.selectbox('性別', options1, index=0)






st.markdown("")
st.markdown("")
st.markdown("")

if st.button('ブレンド占い'):
    year_int =int(year)
    moth_int = int(moth)
    day_int = int(day)
#命数b計算　a:運命数
#もしbが60より大きければ-60
    a = data.loc[year_int,moth]
    b = a + day_int

    if b > 60 :
        b = b -60

    year_int =int(year)
    moth_int = int(moth)
    day_int = int(day)
#命数b計算　a:運命数
#もしbが60より大きければ-60
    a = data.loc[year_int,moth]
    b = a + day_int

    if b > 60 :
        b = b -60


#キャラ属性B　rad ink hok tot kam is
    if 1 <= b <= 10 :
        B = "rad"
    elif 11<= b <= 20 :
        B = "ink"
    elif 21 <= b <= 30:
        B = "hok"
    elif 31 <= b <= 40:
        B = "tot"
    elif 41 <= b <= 50:
        B = "kam"
    elif 51 <= b <= 60 :
        B = "is"
    else:
        B = "NAN"

#print("属性"+":"+B)

#金(+)：Kp，銀(-):Gm→A
    A = "Kp" if year_int % 2 == 0 else "Gm"
#print(A)

#属性結果
    AB = A  + B
    st.write(AB)

# 現在の西暦を取得
    current_year = datetime.now().year

#print("現在の西暦:", current_year)
#属性番号

    dict ={
        1: "Kprad", 2: "Gmink", 3: "Kpink", 4: "Gmhok", 5: "Kphok",6: "Gmtot", 7: "Kptot", 8: "Gmkam", 9: "Kpkam", 10: "Gmis",11: "Kpis", 12: "Gmrad"}
#print(dict)
#今年current_yearの番号
    year_2020 = 2020
    for key, value in dict.items():
        if value == AB:
            today_year = current_year - year_2020
            z = key + today_year
            if z > 12:
                z = z - 12
            else:
                print(z)


#属性記号

    dict2 ={
        "E": "Kprad", "F": "Gmink", "G": "Kpink", "H": "Gmhok", "I": "Kphok","J": "Gmtot", "K": "Kptot", "L": "Gmkam", "A": "Kpkam", "B": "Gmis","C": "Kpis", "D": "Gmrad"}
#print(dict2)

#入力者の属性記号
    target_value = AB
    keys_for_value_1 = [key for key in dict2 if dict2[key] == target_value]

#リストから文字列変換
    join_moji = ''.join(keys_for_value_1)
#st.write(join_moji)



#生年の抽出
    aa = str(year)
    birthday_year_100 = year_int +100
    
    bb = str(birthday_year_100)
    data3 = data2.loc[: ,aa:bb]

    #属性
    data4 = data3[data3 == join_moji]

    #data4
    data5 = data4.copy()

    # 欠損値以外の文字列が出た場合、1行目は3、2行目は2、3行目は0に置き換える
    #五星点数
    for i, row in enumerate(data4.values):
        for j, value in enumerate(row):
            if pd.notna(value):
                if i == 0:
                    data4.iat[i, j] = 3
                elif i == 1:
                    data4.iat[i, j] = 2
                elif i == 2:
                    data4.iat[i, j] = 3
                elif i == 3:
                    data4.iat[i, j] = 3
                elif i == 4:
                    data4.iat[i, j] = 5
                elif i == 5:
                    data4.iat[i, j] = 3
                elif i == 6:
                    data4.iat[i, j] = 4
                elif i == 7:
                    data4.iat[i, j] = 5
                elif i == 8:
                   data4.iat[i, j] = 4
                elif i == 9:
                    data4.iat[i, j] = 0
                elif i == 10:
                    data4.iat[i, j] = 1
                elif i == 11:
                    data4.iat[i, j] = 1
#st.write(data4)
#data4 NaNを除外した各年のデータの数値の合計を計算し、辞書に格納
    year_sums_4 = {year: data4[year].sum(skipna=True) for year in data4.columns}
    #st.write(year_sums_4)

# 欠損値以外の文字列が出た場合、1行目は3、2行目は2、3行目は0に置き換える
#六星点数
    for i, row in enumerate(data5.values):
        for j, value in enumerate(row):
            if pd.notna(value):
                if i == 0:
                  data5.iat[i, j] = 3
                elif i == 1:
                     data5.iat[i, j] = 3
                elif i == 2:
                    data5.iat[i, j] = 3
                elif i == 3:
                   data5.iat[i, j] = 3
                elif i == 4:
                    data5.iat[i, j] = 5
                elif i == 5:
                    data5.iat[i, j] = 2
                elif i == 6:
                    data5.iat[i, j] = 4
                elif i == 7:
                    data5.iat[i, j] = 4
                elif i == 8:
                    data5.iat[i, j] = 5
                elif i == 9:
                    data5.iat[i, j] = 1
                elif i == 10:
                    data5.iat[i, j] = 0
                elif i == 11:
                    data5.iat[i, j] = 1

#data NaNを除外した各年のデータの数値の合計を計算し、辞書に格納
    year_sums_5 = {year: data5[year].sum(skipna=True) for year in data5.columns}

#年齢list1
    ages = list(range(101))

#生年list2 zoku_4,5同じ
    age_years = list(year_sums_4.keys())
#len(age_years)
#int型に変換
    age_years= list(map(int, age_years))


#九星気学9年周期用
# 年から100年後までのリストを作成
year_100list = list(range(year_int, year_int + 101))

# 各年ごとの合計を格納するリスト
year_totals = []

# 各年について処理
for year in year_100list:
    # 各年の合計を初期化
    year_total = 0
    # 各年の各桁を足す
    while year > 0:
        year_total += year % 10
        year //= 10
    # 月の各桁を足す
    month_total = 0
    for digit in str(moth_int):
        month_total += int(digit)
    year_total += month_total
    # 日の各桁を足す
    day_total = 0
    for digit in str(day_int):
        day_total += int(digit)
    year_total += day_total
    
    # 合計が11, 22, 33の場合は0にする
    if year_total in [11, 22, 33]:
        year_total = 0
    # 合計が2桁の場合は10の位と1の位を足す
    elif year_total >= 10:
        year_total = (year_total // 10) + (year_total % 10)
    
    year_totals.append(year_total)
#st.write(year_totals)
#11を消す
for i in range(len(year_totals)):
    if year_totals[i] == 11:
        year_totals[i] = 0
    elif year_totals[i] == 22:
        year_totals[i] = 0
    elif year_totals[i] == 33:
        year_totals[i] = 0
#st.write(year_totals)
#2桁を一けたに
for i in range(len(year_totals)):
    if year_totals[i] >= 10:  # 2桁の場合
        tens_digit = year_totals[i] // 10
        ones_digit = year_totals[i] % 10
        year_totals[i] = tens_digit + ones_digit

#九星気学点数変更
for i in range(len(year_totals)):
    if year_totals[i] == 4:
        year_totals[i] = 3
    elif year_totals[i] == 5 or year_totals[i] == 9:
        year_totals[i] = 4
    elif year_totals[i] == 6:
        year_totals[i] = 5
    elif year_totals[i] == 7:
        year_totals[i] = 3
    elif year_totals[i] == 8:
        year_totals[i] = 5
#st.write(year_totals)



st.markdown('---')

#年齢
my_year = current_year - year_int

st.subheader('入力情報')
st.write(f'生年月日:{year}/{moth}/{day}',f'年齢:{my_year}', f'性別:{sel1}',f'属性:{AB}')
    #st.write(f'年齢:{my_year}')
    #st.write(f'性別:{sel1}')
    #st.write(f'属性:{AB}')



if  sel1 == '男性':
   #厄点数list3
    #男厄年点数0～100歳
        Mlist = [2 if i in {24, 60, 26, 62} else 1 if i in {41, 43, 25, 61} else 0 if i == 42 else 3 for i in range(101)]
    #生年list4
        zoku_point_4 = list(year_sums_4.values())

    #生年list5
        zoku_point_5 = list(year_sums_5.values())

    
        #動的グラフ作成
        import plotly.graph_objects as go
        fig = go.Figure(data=go.Scatter(x = ages, y = Mlist, mode='lines',name='data_厄年', line_color='blue')) 
        #fig = go.Figure(data=go.Scatter(x = ages, y = zoku_point_4, mode='lines', line_color='red')) 
        #fig = go.Figure(data=go.Scatter(x = ages, y = zoku_point_5, mode='lines', line_color='green')) 
        #データ追加　
        fig.add_trace(go.Scatter(x=ages, y=zoku_point_4, mode='lines', name='data_極秘', line_color='red'))
        fig.add_trace(go.Scatter(x=ages, y=zoku_point_5, mode='lines', name='data_極秘2', line_color='green'))
        fig.add_trace(go.Scatter(x=ages, y=year_totals, mode='lines', name='data_数秘術', line_color='yellow'))

        fig.update_layout(title='', xaxis_title='年齢', yaxis_title='y_value')
        st.plotly_chart(fig)


    # 折れ線グラフを作成
        fig = plt.figure()
        plt.plot(ages, Mlist, label='data_厄年', color='blue', linewidth=0.5)
#plt.plot(ages, Flist, label='List3')
        plt.plot(ages, zoku_point_4, label='data_極秘', color='red', linewidth=0.5)
        plt.plot(ages, zoku_point_5, label='data_極秘2', color='forestgreen', linewidth=0.5)
        plt.plot(ages, year_totals, label='data_数秘術', color='yellow', linewidth=0.5)

# 横軸の目盛りを手動で設定
        plt.xticks(np.arange(0, 101, 5))  # 0から100の範囲を10刻みで設定

# グラフのタイトルと軸ラベルを設定
        plt.title('iPhone or Android')
        plt.xlabel('years')
        plt.ylabel('Y values')

# グラフを表示
        st.pyplot(fig)


if  sel1 == '女性':
    #女厄年点数0～100歳
        Flist = [2 if i in {18, 36, 20, 38} else 1 if i in {32,34,19,37} else 0 if i == 33 else 3 for i in range(101)]
        #生年list4
        zoku_point_4 = list(year_sums_4.values())

        #生年list5
        zoku_point_5 = list(year_sums_5.values())


        #動的グラフ作成
        import plotly.graph_objects as go
        fig = go.Figure(data=go.Scatter(x = ages, y = Flist, mode='lines',name='data_厄年', line_color='blue')) 
        #fig = go.Figure(data=go.Scatter(x = ages, y = zoku_point_4, mode='lines', line_color='red')) 
        #fig = go.Figure(data=go.Scatter(x = ages, y = zoku_point_5, mode='lines', line_color='green')) 
        #データ追加
        fig.add_trace(go.Scatter(x=ages, y=zoku_point_4, mode='lines', name='data_極秘', line_color='red'))
        fig.add_trace(go.Scatter(x=ages, y=zoku_point_5, mode='lines', name='data_極秘2', line_color='green'))
        fig.add_trace(go.Scatter(x=ages, y=year_totals, mode='lines', name='data_数秘術', line_color='yellow'))

        fig.update_layout(title='', xaxis_title='年齢', yaxis_title='y_value')
        st.plotly_chart(fig)
    
        # 折れ線グラフを作成

        fig = plt.figure()
        #plt.plot(ages, Mlist, label='data_厄年', color='blue', linewidth=0.5)
        plt.plot(ages, Flist, label='List3')
        plt.plot(ages, zoku_point_4, label='data_極秘', color='red', linewidth=0.5)
        plt.plot(ages, zoku_point_5, label='data_極秘2', color='forestgreen', linewidth=0.5)
        plt.plot(ages, year_totals, label='data_数秘術', color='yellow', linewidth=0.5)

        # 横軸の目盛りを手動で設定
        plt.xticks(np.arange(0, 101, 5))  # 0から100の範囲を10刻みで設定

        # グラフのタイトルと軸ラベルを設定
        plt.title('iPhone or Android')
        plt.xlabel('years')
        plt.ylabel('Y values')

# グラフを表示
        st.pyplot(fig)
 



st.markdown("# グラフから見えてくるもの")
st.write(f'横軸が年齢，縦軸が運気point.data1では，鹿児島県における厄年を表示．data2.3は極秘．data4では，九星気学と数秘術を計算し表示')
st.write(f'9年周期と12年周期の表示させ，人生の波をとらえる．寒い冬の時期に海に入らないように，タイミングを知っておこう！')
st.write(f'出会い/結婚','病気5/入院', '引っ越し/転職', 'ギャンブル','→すべておすすめタイミング')

st.markdown("# わからないこと")
st.write(f'運気の正確な月と日．性格，適職，相性')
st.write(f'姓名判断，手相→これも組み合わせて自分で判断して')
st.write(f'血液型→誰かデータ探して')






