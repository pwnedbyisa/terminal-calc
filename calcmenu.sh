#!/bin/bash

title="[ -- Options -- ]"
opt1=">> Colors/Theme"
opt2=">> Language"
submenu_opt1=(">> Red" ">> Orange" ">> Yellow" ">> Green" ">> Blue" ">> Purple" ">> White")
submenu_opt2=(">> English" ">> Spanish" ">> French")

main=true
sub1=false
sub2=false

print_opts() {
    local option1="$1"

    if [ "$option1" == 1 ]; then
        printf "\e[7m%s\e[0m%s\n\n%s\n" "${opt1:0:2}" "${opt1:2}" "$opt2" # indexed so only the first two chars are highlighted
    else
        printf "%s\n\n\e[7m%s\e[0m%s\n" "$opt1" "${opt2:0:2}" "${opt2:2}"
    fi
}

sub_1() {
    tput cup 3 0
    printf "\33[2K\r" # clear the line
    for ((i = 0; i < ${#submenu_opt1[@]}; i++)); do
        if [ "$i" -eq "$sub1_highlighted" ]; then
            printf "\e[7m%s\e[0m%s\n\n" "${submenu_opt1[$i]:0:2}" "${submenu_opt1[$i]:2}"
        else
            printf "\33[2K\r"
            printf "%s\n\n" "${submenu_opt1[$i]}"
        fi
    done
}

sub_2() {
    tput cup 3 0
    printf "\33[2K\r" # clear the line
    for ((i = 0; i < ${#submenu_opt2[@]}; i++)); do
        if [ "$i" -eq "$sub2_highlighted" ]; then
            printf "\e[7m%s\e[0m%s\n\n" "${submenu_opt2[$i]:0:2}" "${submenu_opt2[$i]:2}"
        else
            printf "\33[2K\r"
            printf "%s\n\n" "${submenu_opt2[$i]}"
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

sublist1() {
    local text=$(sub_1 "$sub1_highlighted")
    local row=4

    printf "\e[%d;0H" "$row"
    echo -e "$text"
}

sublist2() {
    local text=$(sub_2 "$sub2_highlighted")
    local row=4

    printf "\e[%d;0H" "$row"
    echo -e "$text"
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

end_screen() {
    tput cnorm
    echo
    stty echo
    exit 0
}

trap end_screen EXIT

highlighted=1
sub1_highlighted=0
sub2_highlighted=0
list "$highlighted"

while true; do
    tput civis
    read -rsn1 key
    if [ "$sub1" == true ]; then
        case "$key" in
            A)  # up
                sub1_highlighted=$(( (sub1_highlighted - 1 + ${#submenu_opt1[@]}) % ${#submenu_opt1[@]} ))
                sublist1 "$sub1_highlighted"
                ;;
            B)  # down
                sub1_highlighted=$(( (sub1_highlighted + 1) % ${#submenu_opt1[@]} ))
                sublist1 "$sub1_highlighted"
                ;;
            b)
                sub1=false
                sub2=false
                main=true
                highlighted=1
                list "$highlighted"
                ;;
            q)
                break
                ;;
            "") # enter key
                selected_color="${submenu_opt1[sub1_highlighted]}"
                get_color "$selected_color"
                ;;
        esac
    elif [ "$sub2" == true ]; then
        case "$key" in
            A)  # up
                sub2_highlighted=$(( (sub2_highlighted - 1 + ${#submenu_opt2[@]}) % ${#submenu_opt2[@]} ))
                sublist2 "$sub2_highlighted"
                ;;
            B)  # down
                sub2_highlighted=$(( (sub2_highlighted + 1) % ${#submenu_opt2[@]} ))
                sublist2 "$sub2_highlighted"
                ;;
            b)
                sub1=false
                sub2=false
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
                    sub1=true
                    sub_1
                elif [ "$highlighted" -eq 2 ]; then
                    main=false
                    sub2=true
                    sub_2
                fi
                ;;
    esac
done
