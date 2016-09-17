# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# Navigation Alias
alias home='cd ~'
alias down='cd ~/downloads'
alias life='cd ~/documents/life'
alias doc='cd ~/documents'
alias src='cd ~/src'
alias toast='cd ~/src/Toast'
alias tps='cd ~/src/tps'
alias test='cd ~/src/Toast/tests'
alias tests='cd ~/src/Toast/tests'
alias sand='cd ~/src/sandbox'
alias uni='cd ~/documents/university'
alias fydp='cd ~/documents/university/fydp'

# Command Alias
alias vimbash='vim ~/.bashrc'
alias sourcebash='source ~/.bashrc'
alias vimthought='vim ~/documents/life/thoughts.txt'
alias qq='exit'
alias chrome='chromium-browser'
alias python='python3'
alias py='python3'
alias maket='make test'
alias maked='make dev'
alias makec='make clean'
alias clean='make clean'

#Git Comand Alias
alias status='git status'
alias branch='git branch'
