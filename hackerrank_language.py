import re

[print('VALID') if re.match(r'\d+ (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA| ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART| GROOVY|OBJECTIVEC)', input()) else print('INVALID') for _ in range(int(input()))]