# krita-verticalsvg-convert-plugin

Kritaで入力した文字列を縦書きSVGに変換するDockerを出現させるスクリプト

# Description

文字列を入力し「Output SVG」をクリックすると、その入力テキストを縦書きで表示するSVGを出力するプラグインです。
また、「Copy to Clipboard」をクリックした場合、出力したSVGをクリップボードへのコピーすることができます。
「Both」を押すと両方が可能です。
このSVGテキストは、Tool EditorのSVG Sourceタブ内、SVGの文字列をそのコピーした文字列を置換して、Saveを押すことで縦書きのテキストを貼り付けることができます。


# Dependencies

krita >= 4.0.1
Linux版でのみ確認。(Mac OSXではPythonプラグインの使用が不可能との情報あり。)

# Install

## Windowsの場合

作成中です。

## Linuxの場合

1. 以下のコマンドを端末から入力します。なお、リポジトリを削除及び移動しない場合は2つ目のコマンドの第一引数にlnと指定してください。(コピーの代わりにシンボリックリンクの作成を行います。)
```
git clone https://github.com/Hayakuchi0/krita-verticalsvg-convert-plugin.git
./krita-verticalsvg-convert-plugin/installscript/install_linux.sh
```

2. Kritaを起動し、Settings → Configure Krita... → Python Plugin Managerを選びます。
3. Writing Mode RLにチェックをつけ、再起動します。
4. Create Vertical Writingが表示されていたら成功です。非表示にした場合、Settings → Dockers → Create Vertical Writingを選ぶことで再度出現させることができます。


# Usage

## 基本的な使い方

1. Create Vertical WritingというDocker内の最下部にある左側入力欄に縦書きとして貼り付けたいテキストを横書きで入力します。
2. BothをクリックしてSVGテキストをクリップボードにコピーします。
3. Tool EditorのSVG Sourceタブを開き、既存のSVGテキストを削除します。
4. 2でコピーしたSVGの文字列を貼り付けます。
5. Saveを押すことで縦書きのテキストを貼り付けることができます。

## 各項目について

### font-color

使用するフォントの色を選びます。

### font-family

使用するフォント名を選びます。

### font size(pt)

ポイント単位でのフォントサイズを指定します。
直接入力しても、プルダウンで選んでもよいです。

### Output SVG

このボタンを押すと、左側の入力欄の内容を、縦書き表示にしたSVGに変換し右側の入力欄に書き込みます。

### Copy to Clipboard

このボタンを押すと、右側の入力欄の内容をすべてクリップボードにコピーします。
(右クリックでのコピーと同じ処理です。)

### Both

上記の「Output SVG」と「Copy to Clipboard」の両方、つまりSVGに変換し右側の入力欄へ書き込み、それをコピーすることができます。

# LICENSE

[MIT](https://github.com/Hayakuchi0/krita-verticalsvg-convert-plugin/blob/master/LICENSE)

# Author

[Hayakuchi0](https://github.com/Hayakuchi0)
