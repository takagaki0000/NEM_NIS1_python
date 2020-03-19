# NEM_NIS1_python


python3で作ったNEMNIS1用の小さなツール


注意点　記事からコピーして作成したのでpython3でのスペースとかタブが混在していてエラーになるかもしれません
ラズパイなどlinux環境で作成するとわかりやすいと思われます

ハードウェアに依存しているプログラムは載せていません
（e-paper,AIY-voice,LED,obnizなど）

最初のころはランダムでNISサーバーを選ばずに固定で書いています
場合によっては反応が悪くてエラーがでます
必要であればサーバーを変更してください
サーバーをランダムに選ぶルーチンも書いておきます

想定している環境
python3.x
ネット環境
nanoなどのエディタで編集（もちろん補完のあるものでも）
ラズパイでも動作可能です

アドヴェントカレンダーに記事をアップしてるのでそちらも参考に

2019 NEM アドヴェントカレンダー

モザイクガチャ　（nemlog版）の仕組みについて
https://qiita.com/takamoto0000/items/31210c8edf87851b0e95


NEMのモザイクのメッセージをpython3で制御してみる
https://qiita.com/takamoto0000/items/5b5d4554a0b7d5910289



各プログラムの説明
基本的に変数はプログラムに書き込みして実行

make-outgoing.py　　あるアドレスのoutgoing.jsonを作成するツール

address-list-from-outgoing.py  outgoing.jsonからアドレスリスト作成 

make-qr-from-address.py 　　アドレスリストからｑｒコード作成

make-data-fron-incoming.py  incoming.jsonからsigner:データとaddress:データを表示    

message-from-address.py   アドレスに送られたincomingデータからメッセージを抜き出す（暗号化なしのみ）

get-data-from-incoming.py  アドレスを指定してincominfgのデータから指定したデータを表示

compair-data.part_py   incomingから抜き出したデータの値を比較　データによって違うので一部の例です

make-bingo-card.py  ビンゴカードを作ってみる

get-mosaic-info.py  あるアドレスのMOSAIC情報をゲットする

get-mosaic-info2.py  上記のqiita公開版　NISサーバーをランダムで選んでいます

getaddress05-ok.py   ユーザー名を引数に与えて実行するとアドレスとペアのデータが表示されます（要　nemlog03-ok.json）

getname_from_address01.py  上と逆にアドレスから名前を引いてデータペアを表示してくれます（要　nemlog03-ok.json）

nemlog03-ok.ison  上のプログラムで使うための名前とアドレスのペアデータ.jsonです
