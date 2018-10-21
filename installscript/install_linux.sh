#!/bin/sh

here=`dirname ${0}`
here=`cd ${here}/..;pwd`
if [ $# -eq 0 ];then
	cp -r ${here}/writing_mode_rl ~/.local/share/krita/pykrita
else
	ln -s ${here}/writing_mode_rl ~/.local/share/krita/pykrita
fi
if [ $# -eq 0 ];then
	cp -r ${here}/writing_mode_rl.desktop ~/.local/share/krita/pykrita
else
	ln -s ${here}/writing_mode_rl.desktop ~/.local/share/krita/pykrita
fi
