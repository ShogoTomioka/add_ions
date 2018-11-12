# add_ions
python-script-to-add-couterion

・研究用のスクリプト
MD計算では系全体の電荷を中世にしておく必要があるため、カウンターイオンを付加する必要がある。
しかし、Gromacs等のコマンドでは期待した場所にはつかないので、荷電アミノ酸の末端付近に付加するプログラムを作った。

距離の計算はLys以外は、末端の二つの酸素もしくは水素の中間点から、窒素または酸素への距離の二倍離れた場所に。
Lysの場合は、末端の水素三つの中点からの二倍離れた距離に付加するようになっている。

-i :　入力PDBファイル、タンパク質以外は電荷の計算に入らないので、リンガンドなどが電荷を持っている場合は電荷を指定する　　
-n :　電荷を指定する場合に使用
-o :　出力するファイル名、デフォルトでは"ions.txt"

TODO：

- [] 距離の倍率を指定できるようにする
- [] リガンド周りにもつけられるようにする
