# krita-verticalsvg-convert-plugin

Kritaで入力した文字列を縦書きSVGに変換するDockerを出現させるスクリプト

# Description

文字列を入力し「Output SVG」をクリックすると、その入力テキストを縦書きで表示するSVGを出力するプラグインです。
このSVGテキストは、Tool EditorのSVG Sourceタブ内、SVGの文字列をそのコピーした文字列を置換して、Saveを押すことで縦書きのテキストを貼り付けることができます。


# Dependencies

* krita >= 4.0.1
	* Ubuntu18.04で確認
* krita >= 4.1.1
	* Windows7で確認

# Install


installscriptフォルダ内のinstall_windows.batを実行してください。


1. プラグインをインストールします。
	1. Windowsの場合
		1. ReleaseからSourceCode.zipをダウンロードし、展開します。
		2. 展開したフォルダ内のinstallscriptフォルダに格納してあるinstall_windows.batを実行してください。
	2. Linuxの場合
		1. 以下のコマンドを端末から入力します。
		2. リポジトリを削除及び移動しない場合は2つ目のコマンドの第一引数にlnと指定してください。\(コピーの代わりにシンボリックリンクの作成を行います。\)
```
git clone https://github.com/Hayakuchi0/krita-verticalsvg-convert-plugin.git
./krita-verticalsvg-convert-plugin/installscript/install_linux.sh
```

2. kritaを起動して設定\(N\) → Kritaの設定を変更\(C\) → Pythonプラグインマネージャ → Writing Mode RL にチェックをつけます。
3. kritaを再起動します。
Create Vertical Writingが表示されていたら成功です。
非表示にした場合、設定\(N\) → ドッキングパネル\(D\) → Create Vertical Writingを選ぶことで再度出現させることができます。


# Usage

[Manual](https://hayakuchi0.github.io/krita-verticalsvg-convert-plugin/writing_mode_rl/Manual.html
)を参照してください。

# LICENSE

[MIT](https://github.com/Hayakuchi0/krita-verticalsvg-convert-plugin/blob/master/LICENSE)

# Author

[Hayakuchi0](https://github.com/Hayakuchi0)
