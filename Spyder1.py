# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd


st.title('蔵の街須坂　季節別日帰り旅行のすゝめ')


st.write('「1日暇だなー何しよう。。。」ってときに使えるアプリを開発しました。四季折々の須坂市の季節別に訪れてほしい場所がたくさんあるので、季節を選択してあなたに合った日帰りツアーを提案します😄')



genre = st.radio(
    "訪れたい季節はいつですか",
    ('春', '夏','秋','冬'))


   
if genre == '春':
    
     
    st.write('春の日のおすすめルート') 
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/suzaka-haru.jpg')
    
    st.image(image, caption='')
    st.write('<span style="color:black;background:yellow">10:00～　臥龍公園散策</span>',
                  unsafe_allow_html=True)
    
   
    from PIL import Image
    image = Image.open('C:/Users/ab/Pictures/garyuukouensakura1.jpg')
    
    st.image(image, caption='')
    
   
    
    st.write('臥竜公園の桜並木は『さくら名所100選』に選ばれています。池の周りにはソメイヨシノを中心に160本（池の1週は約800ｍ）、公園全体で約600本の桜が楽しめます。')
   
   
    
    
    st.write('<span style="color:black;background:yellow">12:00～　黒おでんで昼食</span>',
                  unsafe_allow_html=True)
    st.write('小腹がすいたらおすすめ！名物の黒おでん!なんと朝4時から仕込んでいるらしい？！')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/kurooden.webp')
    
    st.image(image, caption='臥龍公園名物の黒おでん🍢')
    
    image = Image.open('C:/Users/ab/Downloads/suzaka-motoya.jpg')
    
    st.image(image, caption='「もとや」にて発売中！')
    
    
    ###<iframe width="1140" height="641" src="https://www.youtube.com/embed/qSdSR2FTeyQ" title="須坂市　臥竜公園おでん食べ歩き" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    df = pd.DataFrame(
        [[36.64357575005858, 138.31199439829481]],
        columns=['lat', 'lon'])

    st.map(df)
    
    
    
    
    ####https://blog.suzaka.jp/omise/2018/04/06/p34776
    
    
    st.write('<span style="color:black;background:yellow">13:00～　須坂動物園</span>',
                  unsafe_allow_html=True)
    
    st.write('さくらの名所100選・日本の名松100選で名高い「臥竜公園」内ある動物園。約50種・230点の飼育動物を展示。現在の人気者は、カピバラの華（はな）、ベンガルトラ兄妹の臥桜（がお）と未桜（みお）、ワオキツネザルなどです。')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/douutueniriguti.jpg')
    
    st.image(image, caption='')
    
   
    
    st.write('')
   
   
    
    
    
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/doubutuendensya.jpg')
    
    st.image(image, caption='昔ながらの電車が飾ってあります')
    
    image = Image.open('C:/Users/ab/Downloads/map.png')
    
    st.image(image, caption='動物園のマップ。小さいながらたくさんの動物がいるのが特徴！')
    
    st.info('所在地	〒382-0028　須坂市臥竜2-4-8', icon="ℹ️")
    df = pd.DataFrame(
        [[36.644363567063195, 138.3108054873123]],
        columns=['lat', 'lon'])

    st.map(df) 
    
    
    
    
    
    
    
    
    
    



if genre == '夏':
    st.write('夏の日のおすすめルート') 
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/messageImage_1670204849555.jpg')
    
    st.image(image, caption='')
    st.write('<span style="color:black;background:yellow">10:00～　蔵の街並み　散策</span>',
                  unsafe_allow_html=True)
    
   
   
    
   
    
    st.write('江戸時代は、須坂藩主堀氏の館町（陣屋町）として、また大笹街道の追分の地として、数々の商取引が行われました。その後、明治から昭和初期にかけて近代製糸業によって繁栄し、今も豪壮な土蔵造りの旧製糸家建物や繁盛した大壁造りの商屋などの町並みが残されており、蔵を生かした商店、博物館、美術館など当時を偲ぶことができます。')
   
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/kura.jpg')
    
    st.image(image, caption='')
    
    
    image = Image.open('C:/Users/ab/Downloads/kura2.jpg')
     
    st.image(image, caption='')
    

    
    
    st.write('<span style="color:black;background:yellow">12:00～　かねき</span>',
                  unsafe_allow_html=True)
    st.write('須坂の名物　かねきのオムライス。毎日並んでいる超有名店舗。相葉マナブに紹介されました。野沢菜ライスの味噌オムライスが大人気です。')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/kaneki2.jpg')
    
    st.image(image, caption='地上波で紹介されました！')
    
    image = Image.open('C:/Users/ab/Downloads/kaneki3.jpg')
    
    st.image(image, caption='みそオムライスが絶品！安くて量が多くてコスパ◎')
    
    
    ###<iframe width="1140" height="641" src="https://www.youtube.com/embed/qSdSR2FTeyQ" title="須坂市　臥竜公園おでん食べ歩き" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    st.info('所在地　〒382-0087 長野県須坂市須坂東横町３４４−１', icon="ℹ️")
    df = pd.DataFrame(
        [[36.65631373498742, 138.30882849987003]],
        columns=['lat', 'lon'])

    st.map(df)
    
    
    
    
    ####https://blog.suzaka.jp/omise/2018/04/06/p34776
    
    
    st.write('<span style="color:black;background:yellow">13:00～　サマーランドでスライダーを楽しもう！</span>',
                  unsafe_allow_html=True)
    
    st.write('スライダーは県内一の長さ!　流水プールと大型スライダーがあり家族みんなで楽しめます。筆者も高校生の時よく行ってました(笑)')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/samaran.jpg')
    
    st.image(image, caption='')
    
   
    
    st.write('')
   
   
    
    
    
    
    st.info('所在地	〒382-0000 長野県須坂市大字日滝４１３−４', icon="ℹ️")
    df = pd.DataFrame(
        [[36.65774802541648, 138.3295211607985]],
        columns=['lat', 'lon'])

    st.map(df) 





if genre == '秋':
    st.write('秋の日のおすすめルート') 
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/suzakaaki.jpg')
    
    st.image(image, caption='')
    st.write('<span style="color:black;background:yellow">10:00～　蔵の街並み　散策</span>',
                  unsafe_allow_html=True)
    
   
   
    
   
    
    st.write('江戸時代は、須坂藩主堀氏の館町（陣屋町）として、また大笹街道の追分の地として、数々の商取引が行われました。その後、明治から昭和初期にかけて近代製糸業によって繁栄し、今も豪壮な土蔵造りの旧製糸家建物や繁盛した大壁造りの商屋などの町並みが残されており、蔵を生かした商店、博物館、美術館など当時を偲ぶことができます。')
   
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/kura.jpg')
    
    st.image(image, caption='')
    
    
    image = Image.open('C:/Users/ab/Downloads/kura2.jpg')
     
    st.image(image, caption='')
    
    st.write('<span style="color:black;background:yellow">12:00～　ラノッキオ</span>',
                  unsafe_allow_html=True)
    st.write('古民家を利用したおしゃれな空間で食べるピザとパスタはおいしい！隠れ家的で')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/ranokkio.jpg')

    st.image(image, caption='写真の右側のところから入ります。わかりづらすぎる')

    image = Image.open('C:/Users/ab/Downloads/ranokkioiriguti.jpg')

    st.image(image, caption='裏路地感がワクワクするポイント高め')

    image = Image.open('C:/Users/ab/Downloads/pizza.jpg')

    st.image(image, caption='このピザめっちゃ好き')

    st.write('わかりづらい立地ですがめちゃめちゃいいですおすすめ！') 


    
    st.info('所在地　382-0000　長野県須坂市須坂209-2', icon="ℹ️")
    df = pd.DataFrame(
        [[36.65675858127002, 138.31243627080724]],
        columns=['lat', 'lon'])

    st.map(df)
    
    
    st.write('<span style="color:black;background:yellow">13:00～　りんご狩り</span>',
                  unsafe_allow_html=True)
    st.write('もぎたての味は、また格別！りんごは8月の「つがる」から、11月の「ふじ」まで、品種もさまざま。ぶどうは8月下旬から10月です。「1日1個のりんごは医者を遠ざける」という諺があり、病院のお見舞いの定番として選ばれたり、りんごは身体に良い果物として知られています。須坂の観光農園でおいしい天下一品の果物をお買い求めください。　須坂市から小布施町にかけての国道403号線および、北信濃くだもの街道沿線にある観光農園でりんご・ぶどう狩りが楽しめます。')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/ringo.jpg')
    
    st.image(image, caption='長野の秋と言えばりんごでしょ！')
    
    
    
    st.info('所在地　〒382-0012 長野県須坂市大谷町４４７−４', icon="ℹ️")
    df = pd.DataFrame(
        [[36.65703553531375, 138.33102731531105]],
        columns=['lat', 'lon'])

    st.map(df)
    
    
    
    
   
    

   
    
    
    
    
  
    
    
    
    
    
    
    
if genre == '冬':
    st.write('冬の日のおすすめルート') 
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/suzakahuyu.jpg')
    
    st.image(image, caption='')
    st.write('<span style="color:black;background:yellow">10:00～　REWILD NINJA SNOW HIGHLANDスキー場</span>',
                  unsafe_allow_html=True)
    
   
   
    

    
   
    
    st.write('峰の原高原にあるスキー場⛄️wow&fun❗️キッズパークやチューブや謎解き、巨大AR×忍者と記念撮影📸標高1550mのパウダー❄️自然地形を活かした多彩な10コース⛷忍者コースや多数のスノーアイテムによる地形パーク🏂日没後、オーロライルミネーションが雪山に大出現🌈山頂から見る景色は絶景🌄')
    
    
    image = Image.open('C:/Users/ab/Downloads/sunobo.png')
     
    st.image(image, caption='長野と言ったらウィンタースポーツ！　今年の冬はスノボめっちゃいきたい')
    
    from PIL import Image
    image = Image.open('C:/Users/ab/Pictures/buranko.png')
    
    st.image(image, caption='ブランコでインスタ映え！')
    
    st.info('〒386-2211 長野県須坂市仁礼峰の原３１５３−５０', icon="ℹ️")
    df = pd.DataFrame(
        [[36.556883206686294, 138.35100948461994]],
        columns=['lat', 'lon'])

    st.map(df)
   
    

    
    
    st.write('<span style="color:black;background:yellow">17:00～　湯っ蔵んどで一息</span>',
                  unsafe_allow_html=True)
    st.write('県内最大級の温泉！でかすぎる露天風呂と二種類のサウナが魅力！食事スペースやお土産スペースも充実しています！')
    from PIL import Image
    image = Image.open('C:/Users/ab/Downloads/gaikan[.jpg')
    
    st.image(image, caption='でかいです！')
    
    image = Image.open('C:/Users/ab/Downloads/syokudou.jpg')
    
    st.image(image, caption='ご飯が量が多くておいしい！地元の食べ物も多いです。')
    
    image = Image.open('C:/Users/ab/Downloads/onsen.jpg')
    
    st.image(image, caption='でかい！')
    
    st.write('車で行かないと少し遠いですが、最高なのでぜひ行ってみてね') 
    
    
   
    st.info('所在地　〒382-0000 長野県須坂市仁礼7 番地', icon="ℹ️")
    df = pd.DataFrame(
        [[36.616002764174574, 138.33699755763809]],
        columns=['lat', 'lon'])

    st.map(df)
    
    
    
    
    ####https://blog.suzaka.jp/omise/2018/04/06/p34776
    
    
    
    
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
