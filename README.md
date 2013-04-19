Sublime Text Go To File
=======================

Overview
--------
Plugin searches for a file under the cursor and opens it in new tab.
(The idea comes from Vim `gf` functionality as I missed it in Sublime Text and also the script found on https://gist.github.com/jbjornson/1186126 written by @jbjornson helped a lot!)

Usage
-----
Add shortcut to your keybindings:

`{ "keys": ["alt+d], "command": "go_to_file" }`

1) Highlight the text using `cmd+d`

2) Press `alt+d`


Maintainers:
------------
* Grzegorz Smajdor (https://github.com/gs)
* Maciej Gajek (https://github.com/maltize)

Installation
------------

Go to your Sublime Text 3 `Packages` directory

 - OS X: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
 - Windows: `%APPDATA%/Sublime Text 3/Packages/`
 - Linux: `~/.config/sublime-text-3/Packages/`

and clone the repository using the command below:

``` shell
git clone https://github.com/gs/sublime-text-go-to-file.git GoToFile
```

Note
----
Please open an issue at https://github.com/gs/sublime-text-go-to-file if you discover a problem or would like to see a feature/change implemented.
