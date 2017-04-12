pican-menu
==========
Python script that uses the two external buttons with pull-up (PIN is configurable) to step through a menu.  Two buttons are used, one for each function, N(ext) and R(un), R is used to execute a menu-entry, while N is used to step to the next menu-entry. Each time a new entry is selected, it's name is read out using espeak.  By default, button N is configured as BCM pin 24, while R is defined as BCM pin 23. The menu is loaded from menu.json at load-time.

Default config is for [pican](skpang.co.uk/catalog/pican-canbus-board-for-raspberry-pi-p-1196.html), but any pair of buttons with pull-up should do. 

main.py
-------
Main executable, tested with python 2.

menu.json
---------
Menu definition, JSON-array. Each object in the array defines a menu-entry, with to attributes: name and command. 
Example:
```
[
	{
		"name":"Rick Astley",
		"command":"./rickAstley"
	},
  {
    "name":"John Williams",
    "command":"./johnWilliams"
  }
]
```
