# SymboLikeVim

Vimのように数式の変形を行うterminalソフト

# 背景

式変形を行うとき、関数f(x)の微分を行うなら

diff( f(x) )

と両側に括弧を打たなければいけない。
これは不便である。関数f(x)にカーソルを当て、
dキーを押すだけで微分ができるようなシステムにしたい。


## 実装したもの

- insert, normal, math (m) mode
- hjkl移動
- qで終了