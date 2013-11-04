Note:

This plugin has some differences that the original: See here: https://github.com/stvkoch/sublime-text-go-to-file/compare/gs:master...master


Sublime Text Go To File
=======================

Overview
--------
Plugin searches for a file under the cursor and opens it in new tab.
(The idea comes from Vim `gf` functionality as I missed it in Sublime Text and also the script found on https://gist.github.com/jbjornson/1186126 written by @jbjornson helped a lot!)

Additional functionality - printing currently opened file path in status bar and copy it to clipboard.

Usage
-----
Add shortcut to your keybindings:

    {
      "keys": ["alt+d"], "command": "go_to_file",
      "keys": ["alt+i"], "command": "file_info"
    }

You can highlight the text using `cmd+d` and press `alt+d`.

Press `alt-i` to get info about currently opened file.


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


This version:
``` shell
git clone https://github.com/stvkoch/sublime-text-go-to-file.git GoToFile
```


Original version without open file from class name:
``` shell
git clone https://github.com/gs/sublime-text-go-to-file.git GoToFile
```

Note
----
Please open an issue at https://github.com/gs/sublime-text-go-to-file if you discover a problem or would like to see a feature/change implemented.


Steven Note
----
This version, while not merge with fork branch, has more power to find files basead on class name.


Try: 

 - select namespace and click alt+d
 - click on word of class name and click alt+d
 - click on path of template file and click alt+d
