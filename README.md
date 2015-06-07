# SplatonRegularMatchGetter
レギュラーマッチの情報を取得するPythonモジュールです

Splatonになってるのは意図的な検索避けみたいなものです。  
[言い訳]  
Pythonの練習も兼ねてます。あまり期待はしないであげてください。  

[使い方]  
>python stageinfo  
で、log/に現在のステージ情報のjsonを保存します。  

import stageinfo 
url = <Splatoonのステージ情報のjsonがかえってくるurl>  
j = GetStageInfo(url)  
print j.json()  
で、ステージ情報のjsonが出力されると思います。  
あとはソース直接見てもらえれば分かるかと思いますのであとはよろしくお願いします。
