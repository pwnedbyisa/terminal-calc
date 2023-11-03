#!/bin/bash

title="[ -- Options -- ]"
opt1=">> Colors/Theme"
opt2=">> Language"
submenu_opt1=(">> Red" ">> Orange" ">> Yellow" ">> Green" ">> Blue" ">> Purple" ">> White")
submenu_opt2=(">> English" ">> Spanish" ">> French")

main=true
sub1active=false
sub2active=false
highlighted=1
sub_highlighted=0

print_opts() {
    local option="$1"

    if [ "$option" == 1 ]; then
        printf "\e[7m%s\e[0m%s\n\n%s\n" "${opt1:0:2}" "${opt1:2}" "$opt2" # indexed so only the first two chars are highlighted
    else
        printf "%s\n\n\e[7m%s\e[0m%s\n" "$opt1" "${opt2:0:2}" "${opt2:2}"
    fi
}

sub_menu() {
    local submenu=("$@")

    tput cup 3 0
    printf "\33[2K\r" # clear the line
    for ((i = 0; i < ${#submenu[@]}; i++)); do
        if [ "$i" -eq "$sub_highlighted" ]; then
            printf "\e[7m%s\e[0m%s\n\n" "${submenu[$i]:0:2}" "${submenu[$i]:2}"
        else
            printf "\33[2K\r"
            printf "%s\n\n" "${submenu[$i]}"
        fi
    done
}

list() {
    local text=$(print_opts "$highlighted")
    local row=4

    # clearing any remaining submenu
    for ((i = 7; i < $(tput lines); i++)); do
        tput cup "$i" 0
        printf "%$(tput cols)s" " "
    done

    printf "\e[%d;0H" "$row"
    echo -e "$text" # maintain formatting
}

get_color() {
    local option="$1"
    local color

    case "$option" in
        ">> Red") color='\033[0;31m' ;;
        ">> Orange") color='\033[0;33m' ;;
        ">> Yellow") color='\033[0;33m' ;;
        ">> Green") color='\033[0;32m' ;;
        ">> Blue") color='\033[0;34m' ;;
        ">> Purple") color='\033[0;35m' ;;
        ">> White") color='\033[0;37m' ;;
    esac

    exp_color="$color"
    export exp_color
}

printf "\033[H\033[2J"
echo -e "$title\n\n\n"

list "$highlighted"

end_screen() {
    tput cnorm
    echo
    stty echo
    exit 0
}

trap end_screen EXIT

while true; do
    tput civis
    read -rsn1 key
    if [ "$sub1active" == true ]; then
        case "$key" in
            A)  # up
                sub_highlighted=$(( (sub_highlighted - 1 + ${#submenu_opt1[@]}) % ${#submenu_opt1[@]} ))
                sub_menu "${submenu_opt1[@]}"
                ;;
            B)  # down
                sub_highlighted=$(( (sub_highlighted + 1) % ${#submenu_opt1[@]} ))
                sub_menu "${submenu_opt1[@]}"
                ;;
            b)
                sub1active=false
                sub2active=false
                main=true
                highlighted=1
                list "$highlighted"
                ;;
            q)
                break
                ;;
            "") # enter key
                selected_color="${submenu_opt1[sub_highlighted]}"
                get_color "$selected_color"
                ;;
        esac
    elif [ "$sub2active" == true ]; then
        case "$key" in
            A)  # up
                sub_highlighted=$(( (sub_highlighted - 1 + ${#submenu_opt2[@]}) % ${#submenu_opt2[@]} ))
                sub_menu "${submenu_opt2[@]}"
                ;;
            B)  # down
                sub_highlighted=$(( (sub_highlighted + 1) % ${#submenu_opt2[@]} ))
                sub_menu "${submenu_opt2[@]}"
                ;;
            b)
                sub1active=false
                sub2active=false
                main=true
                highlighted=1
                list "$highlighted"
                ;;
            q)
                break
                ;;
        esac
    fi
    case "$key" in
        A)  # up arrow - highlight opt1
            if [ "$main" == true ]; then
                highlighted=1
                list "$highlighted"
            fi
            ;;
        B)  # down arrow - highlight opt2
            if [ "$main" == true ]; then
                highlighted=2
                list "$highlighted"
            fi
            ;;
        q)
            break
            ;;
        "") # enter key
            if [ "$highlighted" -eq 1 ]; then
                main=false
                sub1active=true
                sub_menu "${submenu_opt1[@]}"
            elif [ "$highlighted" -eq 2 ]; then
                main=false
                sub2active=true
                sub_menu "${submenu_opt2[@]}"
            fi
            ;;
    esac
done
