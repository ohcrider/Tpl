## About
Tpl is a javascript template plugin for Sublime Text 3.
It uses [tpl](https://github.com/caolvchong/tpl) to covert template to javascript.

## Features
* more powerful

## Settings
Tpl depends [Node.js](https://github.com/joyent/node).
There is a awsome way to install Node.js,you can visit [nvm](https://github.com/creationix/nvm) for more detail.

The following **Tpl** settings are available in Tpl/Tpl.sublime-settings (defaults shown below).There is my nodejs and tpl absolute path.Just a reference.You can type `where node && where tpl` find  you current environment.

* `node_path`: /Users/fewspider/.nvm/versions/node/v0.12.2/bin/node
* `tpl_path`: /Users/fewspider/.nvm/versions/node/v0.12.2/bin/tpl

## Install
#### [Package Control](https://github.com/wbond/sublime_package_control) (Recommended)
Tpl is now included in the default repository channel for [Package Control](https://github.com/wbond/sublime_package_control). It should show up in your install list
with no changes.

If it does not show up, or you are on an older version of Package Control,
add https://github.com/fewspider/Tpl as a Package Control repository. Tpl will show up in the
package install list.

## Key Binding

The default key binding is "ctrl+t",in os x is "command+t"

## Key Binding Conflicts

Unfortunately there are other plugins that use "ctrl + alt + t", this is a hard problem to solve. If Tpl works
OK via the command palette but does nothing when you use the "ctrl + alt + s" shortcut, you have two options:

1. Add ```{ "keys": ["ctrl+alt+s"], "command": "tpl" }``` to your user keybindings file. This will override anything specified by a plugin.
2. Find the offending plugin, and change the shortcut in its sublime-keymap file (will revert on updates)

### License
Copyright (C) 2015 fewspider

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
