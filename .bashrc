# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi


export PATH=/home/mcoppola/src/tps/esp-open-sdk/xtensa-lx106-elf/bin:$PATH:/home/mcoppola/Android/Sdk/tools:/home/mcoppola/Android/Sdk/platform-tools:/home/mcoppola/Android/Sdk/tools/bin


# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# Navigation Alias
alias home='cd ~'
alias down='cd ~/Downloads'
alias doc='cd ~/documents'
alias tmp='cd ~/tmp/'

# Command Alias
alias vimbash='vim ~/.bashrc'
alias sourcebash='source ~/.bashrc'
alias qq='exit'
alias chrome='chromium-browser'
alias python='python3'
alias py='python3'
alias maket='make test'
alias maked='make dev'
alias makec='make clean'
alias clean='make clean'
alias l='ls -a'
alias lsusb='ls /dev/ttyUSB*'

#Git Comand Alias
alias status='git status'
alias branch='git branch'

function open {
    gnome-open $1
}

function spell {
    aspell -c $1 -d en_CA
}
