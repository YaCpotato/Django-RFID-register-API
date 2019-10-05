# DjangoでRFIDカードでの色々登録用のAPIを作る

## 作成するAPI
UFID(1~3桁,1~3桁,1~3桁,1~3桁)を受け取り、対象UserのStateをUpdateする
対象Userには4つFieldを作成し、セクター1,2,3,4それぞれ記録する