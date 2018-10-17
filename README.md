# krita-verticalsvg-convert-plugin

Kritaで入力した文字列を縦書きSVGに変換するスクリプト。

# Description

文字列を入力し、「Output SVG」または「Copy to Clipboard」をクリックすると、その入力テキストを縦書きで表示するSVGを出力するプラグイン。
また、「Copy to Clipboard」をクリックした場合、クリップボードへのコピーを行う。
このSVGテキストは、Tool EditorのSVG Sourceタブ内、SVGの文字列をそのコピーした文字列を置換して、Saveを押すことで縦書きのテキストを貼り付ける。


# Dependencies

krita >= 4.0.1
Linux版でのみ確認。(Mac OSXではPythonプラグインの使用が不可能との情報あり。)

# Install for linux

1. 以下のコマンドを端末から入力します。（コピペが望ましいです。）
```
git clone https://github.com/Hayakuchi0/krita-verticalsvg-convert-plugin.git
ln -s `pwd`/krita-verticalsvg-convert-plugin/writing_mode_rl ~/.local/share/krita/pykrita
ln -s `pwd`/krita-verticalsvg-convert-plugin/writing_mode_rl.desktop ~/.local/share/krita/pykrita
```
2. Kritaを起動し、Settings → Configure Krita... → Python Plugin Managerを選びます。
3. Writing Mode RLにチェックをつけ、再起動します。
4. Create Vertical Writingが表示されていたら成功です。非表示にした場合、Settings → Dockers → Create Vertical Writingを選ぶことで再度出現させることができます。

# Usage

## 基本的な使い方

Create Vertical WritingというDocker内の最下部に、２つの入力欄がある。
その左側の入力欄に縦書きとして貼り付けたいテキストを横書きで入力し、BothをクリックしてSVGテキストをクリップボードにコピーする。
このSVGテキストは、Tool EditorのSVG Sourceタブ内、SVGの文字列をそのコピーした文字列を置換して、Saveを押すことで縦書きのテキストを貼り付ける。

## 各項目について

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

未定

# Author

[Hayakuchi0](https://github.com/Hayakuchi0)
