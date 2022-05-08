
# [uLauncher](https://github.com/Ulauncher/Ulauncher) Arch remove package



<p align="center">
</p>



### Little tool written in python to remove Arch packages using uLauncher

 

# Install
Open uLauncher preferences window -> extensions -> add extension and paste the following url:
`https://github.com/Dankni95/ulauncher-remove-arch-packages`

## Start up 
Start uLauncher and type `rm`. <br>
To search `rm -> name of the package or using arrows, enter to delete`.

## Scrolling(kinda)
 `rm -> write number to show packages further down` <br>


### Currently
* No error handling
* No success prompt
* Sudo prompts for every package, exits uLauncher



## Development
Git clone this repo.

In repo folder do `make link` to create symlink to ulauncher extensions folder.

Close uLauncher and run `make dev` and follow instructions in terminal.

You will get code that looks something like this:
```
 VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/com.github.dankni95.ulauncher-remove-arch-packages PYTHONPATH=/usr/lib/python3.9/site-packages /bin/python /home/daniel/.local/share/ulauncher/extensions/com.github.dankni95.ulauncher-remove-arch-packages/main.py
```
Paste it in new terminal window and run keyword `rm` in uLauncher. 
Happy coding!



# Credits
#### This extension uses uLauncher as main driver https://github.com/Ulauncher/Ulauncher
