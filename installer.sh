#!/bin/sh

# https://github.com/drebrb/masstouch

red='\033[0;31m'
green='\033[0;32m'
no_color='\033[0m'
user=$(whoami)

Installation_Complete() {
    printf "%s
************************************
*******${green}INSTALLATION COMPLETE!${no_color}*******
************************************
\n"
}

Error() {
    printf "%s
************************************
***************${red}ERROR!${no_color}***************
************************************
\n"
}

install() {
    if [ -e /usr/local/bin ]
    then
        if cp masstouch_cli.py /usr/local/bin
        then
            Installation_Complete
            exit 0
        else
            Error
            exit 1
        fi
    else
        printf '%s\n' "'usr/local/bin' does not exist."
        printf '%s' "Do you want to create it? [Y/n] "
        read -r input
        case $input in
            y|Y|[yY][eE][sS]) mkdir_install
                ;;
            *) printf '%s\n' "Abort"
                exit 1
        esac
    fi
}

mkdir_install() {
    if mkdir -p /usr/local/bin
    then
        if cp masstouch_cli.py /usr/local/bin
        then
            Installation_Complete
            exit 0
        else
            Error
            exit 1
        fi
    else
        Error
        exit 1
    fi
}

sudo_check() {
    if [ "$user" != "root" ]
    then
        printf '%s\n' "Run as root"
        exit 1
    else
        return 0
    fi
}

sudo_check && install
