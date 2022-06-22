#!/usr/bin/env python3
import pathlib
from os import listdir, PathLike
from os.path import isfile, join, isdir

__TARGET_DIR = 'content'

_TARGET_DIR= pathlib.Path(__file__).parent.joinpath(__TARGET_DIR)

#FIXME move to file
_INDEX = '''---
layout: post
---
<html lang="en">
{% assign npath = page.path | get_subpage_path %}
<head>
<meta name="viewport" content="width=device-width"><style>:root{--b:#fbf1c7;--f:#282828;--d:#af3a03;font-family:monospace;font-size:16px}*{color:var(--f);background:var(--b)}body{margin:0;padding:1.5rem;line-height:1.8}h1{font-size:1.5rem}a{word-wrap:break-word;min-width:0;white-space:pre-wrap;text-underline-position:under}.d{color:var(--d)}.g{display:grid;width:100%;grid-template-columns:7fr 3fr 2fr}.g *{margin:.5rem}.g *:nth-child(3n+3){text-align:right}@media(prefers-color-scheme:dark){:root{--b:#282828;--f:#fbf1c7;--d:#fe8019}}@media(max-width:880px){.g{grid-template-columns:7fr 3fr}.g *{margin:1rem}.g *:nth-child(3n+2){display:none}}</style>
<title>Index of /algoritmi-e-strutture-di-dati</title>
</head>
<body>
<h1>Index of <a>matunibo</a>/<a>{{npath}}</a></h1><hr><div class="g">
{% assign files = npath | list_folders %}
{% for file in files %}
{% unless file contains 'index.html' %}
<a href="{{ site.baseurl}}/{{npath}}{{ file }}">{{file}}</a><p></p><p></p>
{% endunless %}
{% endfor %}
</body></html>
'''








def _gen_index(path:PathLike):
  print('genating %s' % str(path))
  with open(path.joinpath('index.html'), 'w') as f:
    f.write(_INDEX)



def recursive_gen_index(path:[PathLike, str]) -> None:
  _gen_index(path)
  for fl in listdir(path):
    print('checking %s' % str(fl))
    if isdir(path.joinpath(fl)):
      print('entered')
      recursive_gen_index(path.joinpath(fl))
  return None

if __name__ == "__main__":
  recursive_gen_index(_TARGET_DIR)
