
EXT_NAME:=com.github.dankni95.ulauncher-remove-arch-packages
EXT_DIR:=$(shell pwd)

link: 
	ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

dev: 
	ulauncher --no-extensions --dev -v |& grep "ulauncher-remove-arch-packages"

.PHONY:link dev 

