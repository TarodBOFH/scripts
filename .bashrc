# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias stopped='transmission-remote -l | grep "Stopped" | grep -v "100%"'
alias pending='find -links 1 | grep -v ^.*.part$ | sort' 
alias pending_series='find -mindepth 2 -links 1 | grep -v ^.*.part$ | sort'
alias pending_movies='find  -maxdepth 1 -links 1 | grep -v "\ [0-9]\{1,2\}x[0-9]\{1,2\}\ \|^.*.part$" | sort'
alias cp_pending='/root/scripts/copy_pending.sh'
alias not_linked="find . -mindepth 2 -type f -links 2 -exec find -L . -maxdepth 1 -type f -samefile '{}' \;"
alias not_deleted="find . -mindepth 2 -type f -links 3  -exec find -L . -maxdepth 1 -type f -samefile '{}' \;"

TORRENTS="/var/lib/transmission/.config/transmission/torrents/"

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
