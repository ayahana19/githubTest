# 麻雀アプリ作成用　https://qiita.com/kph7mgb/items/e8cb71ca9a0e75e8a9c3
# 上記のアドのポートを指定しようの項目を参照　「Herok」にファイルを上げる時に使う？
if __name__ == '__main__':
    #app.run(port=8080)　　下記に変更
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
