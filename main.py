import streamlit as st
import altair as alt
import pandas as pd
import streamlit as st
import requests
import numpy as np 
from time import time
from datetime import time as dt_time, datetime

# from streamlit_chat import message


st.set_page_config(layout="wide")
#3日目チャレンジ

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.markdown(''':rainbow[Day 3]''')
st.markdown(''':gray[st.button]''')


st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


col1, col2 = st.columns(2)

if st.button('Say Hello'):
    st.write('Well hello governor')
else:
    st.write('Good bye')





st.write('-----------------------------')

#5日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.markdown(''':rainbow[Day 5]''')

st.markdown(''':gray[st.write]''')

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")



st.header('Display text:')
#テキスト・マークダウン形式のテキスト表示
st.write('Oh hello, *governor!* :smile:')


st.header('Display numbers')
st.write('1234')


st.header('Display DataFrame')
#df→pandasのDataFrame
airi = pd.DataFrame({
    'fisrt column': [1, 2, 3, 4, 5],
    'second column' : [10, 20, 30, 40, 50 ]
    #このデータフレームは2つの列（'fisrt column' と 'second column'）を持ち、
    # それぞれの列には整数値のデータが格納されています。
})

st.write(airi)
#Pandasを使用してデータを表形式で整理し、
# それをStreamlitアプリケーション内で表示するためのもの


st.header('Accept multiple arguments')
st.write('Below is a DataFrame', airi, 'Above is a dataframe')

airi2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

airichart = alt.Chart(airi2).mark_circle().encode(
    x='a', y='b', size= 'c', color ='b', tooltip=['a', 'b', 'c'])
st.write(airichart)




st.write('-----------------------------')

#8日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 8]''')

st.markdown(''':gray[st.slider]''')


st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.subheader('Slider')

age = st.slider('How old are you?',0, 100, 25 )
#最小, 最大, デフォルト値
st.write("I'm", age, "years old", ":sunglasses:")



#範囲スライダー
st.subheader('Range Slider')
airis = st.slider(
    'Select a range of values',
    0, 100, (25, 75))
st.write('Values', airis)


#時間範囲スライダー
st.subheader('Range Time slider')

itu = st.slider(
    "Schedule your appointment:",
    value=(dt_time(11,30), dt_time(12,45)))
st.write("You are scheduled for:", itu)


#日時スライダー
st.subheader('Datetime slider')

itus_start = st.slider(
    "When do you start?",
    value=datetime(2023,1,1,0,0),
    format="YY/MM/DD - hh:mm")
st.write("Sart Time :",itus_start )



st.write('-----------------------------')

#9日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 9]''')
st.markdown(''':gray[st.line_chart]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

#構築内容
#1.NumPyでランダムに生成された数値からPandasのDataFrameを作成する
#2.st.line_chart()コマンドで折れ線グラフを作成して表示する


st.header('Line Chart')

#3つの列を含むランダムに生成された数値のDataFrameを作成
chart_no_date = pd.DataFrame(
    np.random.randn(20,3),
    columns=['blue', 'light blue', 'red'])
    #最後に、chart_data変数に格納されたDataFrameを入力データとして、
    # st.line_chart()を使って折れ線グラフを作成します
st.line_chart(chart_no_date)
#20行3列のランダムなデータを生成


st.write('-----------------------------')


#10日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 10]''')
st.markdown(''':gray[st.selectbox]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


#ユーザーが色を選択します
#アプリから選択された色が出力されます

st.header('st.selectbox')

choisu = st.selectbox(
    'What is your favourite desert?', 
    ('Choucream', 'Cake', 'Fluits'))

st.write('Your favourite desert is', choisu)

st.write('-----------------------------')

#11日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 11]''')
st.markdown(''':gray[st.multiselect]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.header('st.multiselect')

choices = st.multiselect(
    'What is your favourite fruits?',
    ['Apple', 'Kiwi', 'Orange', 'Grape', 'Pineapple'],
    #default
    ['Kiwi', 'Pineapple']
)
st.write('You like', choices)



st.write('-----------------------------')
#12日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 12]''')
st.markdown(''':gray[st.checkbox]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.header('st.checkbox')

st.write('What would you like to order?')

incecream = st.checkbox('Icecream')
Choucream = st.checkbox('Choucream')
Coffee = st.checkbox('Coffee')
Cola = st.checkbox('Cola')

if incecream:
    st.write("Great! Here's some more! 	:icecream:")

if Choucream:
    st.write('Okay, here is your chou à la crème :honey_pot:')

if Coffee:
    st.write('There you go but it`s tea :tea:')

if Cola:
    st.write('COCA COLA :tropical_drink:')



st.write('-----------------------------')
# #14日目
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
# st.markdown(''':rainbow[Day 14]''')
# st.markdown(''':gray[コンポーネント]''')
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# message("Hej tis") 
# message("Halløj diller!", is_user=True)

# st.write('-----------------------------')

#15日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 15]''')
st.markdown(''':gray[st.latex]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


#st.latexは、LaTeX形式の数式を表示します。
st.header('st.latex')


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1}=
    \sum_{k=0}^{n-1} ar^k=
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write('-----------------------------')
#16日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 16]''')
st.markdown(''':gray[Custmizing the theme]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title('Customizing the themeof Streamlit apps')
st.write('Contents of the `.streamlit/config.toml` file of this app')

#config.tomlファイルに記載
st.code("""
[theme]
primaryColor="#F0DBDB"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
number = st.sidebar.slider('Select a number:', 0,10,5)
st.write('Selected number from slider widget is :', number)


# #17日目
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
# st.markdown(''':rainbow[Day 17]''')
# st.markdown(''':gray[st.secrets]''')
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# st.title('st.secrets')
# st.write(st.secrets['message'])



st.write('-----------------------------')
#18日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 18]''')
st.markdown(''':gray[st.file_uploader]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title('st.file_uploader')
st.subheader('Input CSV')
uploaded_sareta = st.file_uploader("Choose a file")

if uploaded_sareta is not None:
    df = pd.read_csv(uploaded_sareta)
    st.subheader('Dataframe')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info(':rainbow: Upload a CSV file')

st.write('-----------------------------')
#19日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 19]''')
st.markdown(''':gray[アプリをレイアウト]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")



# st.set_page_config(layout="wide")
st.title('How to layout your Steramlit app')

with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', 
['','😆','😊','😍','😴','😕','😱'])
user_food = st.sidebar.selectbox('What is your favourite food?',
['', 'Pizza', 'Burger', 'Yakiniku', 'Burrito'])
st.write(f"{user_name},")
st.write(f"Today, you look like: {user_emoji}")
st.write(f"And I know you like: {user_food}")

#st.columnsコマンドを使用して、
#col1、col2、col3に対応する3つの列を作成します。
st.header('Output')

# withステートメントで始まる個々のコードブロックを作成し、 
col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'Hey {user_name}! :smile:')
    else:
        st.write(':orange_heart: Please enter your **name**!')

with col2:
    if user_emoji !='': 
        st.write(f'{user_emoji} is your **emoji**!')
    else:
        st.write(':orange_heart: Please choose an **emoji**!')

with col3:
    if user_food != '':
        st.write(f'**{user_food}** :stuffed_flatbread: is your favourite **food**!')
    else:
        st.write(':orange_heart: Please choose your favourite **food**!')

#f文字列を使用して、定型テキストとユーザーが指定した値を
# 組み合わせている点にも注目してください。

st.write('-----------------------------')
#21日目
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
# st.markdown(''':rainbow[Day 21]''')
# st.markdown(''':gray[st.progress]''')
# st.markdown("\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# st.title('st.progress')


# with st.expander('About this thingie'):
#     st.write('You can now display the progress of your calculation in a Streamlit app with the `st.progress` command.')

# #進行状況バーを定義し、開始値を0としてインスタンス化します。
# # 次に、forループで0から100に達するまで反復します
# my_bar = st.progress(0)
# progress_placeholder = st.empty()

# #各反復でtime.sleep(0.05)を使用して
# #アプリがmy_bar進行状況バーに値1を追加する前に0.05待機する

# for percent_complete in range(100):
#     time.sleep(0.3)
#     my_bar.progress(percent_complete +1)
# st.balloons()


#バーのグラフィック表示が反復ごとに増加するようにします。


st.write('-----------------------------')
#22日目

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 22]''')
st.markdown(''':gray[st.form]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.title('st.form')
st.header('1.Example of using `with` notation')
st.subheader('Donuts butik :doughnut:')

#st.formコマンドをwith表記で適用します。
#フォーム内でサブヘッダーOrder your coffeeを記述


def custom_checkbox(label):
    if st.checkbox(label, key=f'{label}_checkbox'):
        return 'Ja'
    else:
        return 'Nej'

with st.form('my_form'):
    st.subheader('**Tilpas og bestil din doughnut**')
    which_donut_val = st.selectbox('Typer af donuts', 
    ['Old fashion', 'Fluff', 'Pon de ring', 'Mini balls'])
    sauce_val = st.selectbox('Graze', 
    ['chokolade', 'hvid chokolade', 'Jordbær', 'Honning'])
    topping_val = st.selectbox('Drys?', 
    ['Tivoli drys', 'Oreo', 'Crunsh', 'Nødder'])
    serving_type_val = st.selectbox('Varm eller kold',
    ['Varm donuts op', 'Kold'])
    owncup_val = custom_checkbox('Jeg tager min donutpose med')
    submitted = st.form_submit_button('Submit')
#これをクリックすると、すべてのユーザー入力が1つのバッチ情報としてアプリに送信され、処理されます

if submitted:
    st.markdown(f'''
    You have orderd :doughnut::orange_heart:  :
    - Doughnut: `{which_donut_val}`
    - Graze: `{sauce_val}`
    - Toppings: `{topping_val}`
    - Serveringstype:`{serving_type_val}`
    - Bring own bag: `{owncup_val}`
    - Tak for din ordre!:orange_heart:
    ''')
else:st.write('Place your order and have some goodies!:doughnut:')


st.header('2. Example of object notation')

form = st.form('my_form2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected Value', selected_val)


st.write('-----------------------------')
#23日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 23]''')
st.markdown(''':gray[st.experimental_get_query_params]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title('st.ecperimental_get_query_params')

with st.expander('About this app'):
    st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.この関数を使うことで、ユーザーのブラウザのURLからクエリパラメーター（クエリ文字列内の情報）を取得できます。")

#手順
#1
    st.header('1.Instructions')
    st.markdown('''
    In the above URL bar of your internet browser, append the following:
    `?name=Jack&surname=Beanstalk`
    after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
    such that it becomes 
    http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
#2
st.header('2.Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
#3
st.header('3.Retrieving and displaying information from the URL')


query_prams = st.experimental_get_query_params()
if 'firstname' in query_prams and 'surname'in query_prams:
    firstname = st.experimental_get_query_params()['firstname'][0]
    surname = st.experimental_get_query_params()['surname'][0]
    st.write(f'Hello**{firstname}**, how are you?')


#st.experimental_get_query_params()からクエリパラメーターを取得しています。
# 'firstname'および'surname'という名前のクエリパラメーターを取得し、
# それぞれの値をfirstnameとsurname変数に代入しています。




st.write('-----------------------------')
#24日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 24]''')
st.markdown(''':gray[st.cache]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.title('st.cache')

a0 = time()
#time()関数を使って現在の時間をa0変数に保存しています。
# この時刻は後で実行時間の計測に使用されます。
st.subheader('Using st.cache')

#大規模なDataFrameを生成するための2つのカスタム関数を定義します。
#@st.cacheデコレーターを使用して、
# 関数 load_data_a をキャッシュ対象にしています。
@st.cache(suppress_st_warning=True)
def load_data_a():
    #カスタム関数 load_data_a を定義しています。
    # この関数は大規模なデータフレームを生成します。
    df = pd.DataFrame(
        #関数内で、200万行×5列のランダムなデータを持つデータフレームを生成しています。
        # これは大規模なデータセットです。
        np.random.rand(2000000,5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df
st.write(load_data_a())
a1 = time()
#再度 time() 関数を使用して現在の時間を a1 変数に保存しています。
# これは処理時間の計算に使用されます。
st.info(a1-a0)
#a0 と a1 の差分を計算して、Streamlitの st.info() を使用して
# 処理時間を表示しています。
# これにより、データ生成と表示にかかった時間が表示されます。


st.write('-----------------------------')
#25日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 25]''')
st.markdown(''':gray[st.session_state]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.title('st.session_state')

#重量をlbsからkgに、およびその逆に変換するためのカスタム関数を定義
def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046


#st.number_inputを使用して重量値の数値入力を受け入れます。
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

#上記2つのカスタム関数は、st.number_inputコマンドで作成した数値ボックスに
# 数値が入力されるとすぐに呼び出されます

#on_changeオプションで2つのカスタム関数lbs_to_kgとkg_to_lbsを指定している
st.header('Output')
st.write("st.session_state object:", st.session_state)



st.write('-----------------------------')
#26日目
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''':rainbow[Day 26]''')
st.markdown(''':gray[Bored APIアプリを構築してAPIを使用する方法]''')
st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.title(':neutral_face: Bored API app')

st.sidebar.header('Bored app')
#st.selectboxコマンドによって、
# アクティビティタイプに関するユーザー入力を受け入れます。
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
#上記で選択されたアクティビティは、f-stringによってURLに追加され、
#結果のJSONデータを取得するために使用されます。



c1, c2 = st.columns(2)
with c1:
    with st.expander('About this app'):
        st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

#最後に、Number of Participants、Type of Activity、Priceなど、
# 提案するアクティビティの付随情報も表示します。

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label = 'Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
    st.metric(label = 'Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
    st.metric(label='Price', value=suggested_activity['price'],delta='')

st.write('-----------------------------')



api_key = ' 026d1492891a46dcadedaee9c7886552'

st.title('RECIPE suggestion app')

st.sidebar.header('Recipe app')

meal_type = st.sidebar.selectbox('Select a meal type', ["breakfast", "lunch", "dinner"])
#Web APIにリクエストを送信するためのURLを作成します。
spoonacular_url = f'https://api.spoonacular.com/recipes/random?apiKey={api_key}&number=1&tags={meal_type}'


# APIからデータを取得
response = requests.get(spoonacular_url)
data = response.json()

with st.expander('About this app'):
    st.write('Looking for recipe ideas? The **Spoonacular Recipe Suggestion App** provides you with a random recipe based on your selected meal type.')

with st.expander('Recipe data'):
    st.write(data)

st.header('Suggested Recipe')
recipe = data['recipes'][0]
st.info(f"Here's a suggested {meal_type} recipe: {recipe['title']}")

col1, col2, col3 = st.columns(3)
st.metric(label='Ready In Minutes', value=recipe['readyInMinutes'], delta='')
st.metric(label='Serving Size', value=recipe['servings'], delta='')
st.metric(label='Source URL', value=recipe['sourceUrl'], delta='')