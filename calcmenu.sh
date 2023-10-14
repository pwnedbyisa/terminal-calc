# THIS IS A WORK IN PROGRESS
# AKA IT DOES NOT WORK YET
# AKA IGNORE THIS UNTIL THE MESSAGE IS GONE
# thanks!

#!/bin/bash

# rn theres one char showing through when i switch back to main idk why
# also the box function doesn't deal w overwritten lines well
# and none of the options have logic attached yet

title="Options"
opt1="Colors/Theme"
opt2="Language"
submenu_opt1=("Red" "Orange" "Yellow" "Green" "Blue" "Purple" "White")
submenu_opt2=("English" "Spanish" "French")

sub1=false
sub2=false

# prints options menu with highlighting
print_opts() {
    local option1="$1"

    if [ "$option1" == 1 ]; then
        printf "\e[7m%s\e[0m \t%s\n" "$opt1" "$opt2"
    else
        printf "%s \t\e[7m%s\e[0m\n" "$opt1" "$opt2"
    fi
}

submenu_opt1() {
    # Clear the previous submenu options
    tput cup 5 0
    printf " %s" " "  # Clear the row

    # Print the submenu options
    for ((i = 0; i < ${#submenu_opt1[@]}; i++)); do # iterates through the array, the lil #@ situation is the length
        if [ "$i" -eq "$sub1_highlighted" ]; then
            printf "\e[7m%s\e[0m " "${submenu_opt1[$i]}"
        else
            printf "%s " "${submenu_opt1[$i]}"
        fi

        if (( (i + 1) % 4 == 0 )); then
            printf "\n  " # newline after every fourth opt
        fi
    done
}

submenu_opt2() {
    # clear the previous submenu options
    tput cup 5 0
    printf " %s" " "  # clear the row

    # print the submenu options
    for ((i = 0; i < ${#submenu_opt2[@]}; i++)); do
        if [ "$i" -eq "$sub2_highlighted" ]; then
            printf "\e[7m%s\e[0m " "${submenu_opt2[$i]}"
        else
            printf "%s " "${submenu_opt2[$i]}"
        fi
    done
}

box() {
    local highlighted="$1"
    local text=$(print_opts "$highlighted")
    local len=${#text}
    local row=3
    # local num_lines=$(( ($(echo -e "$text" | wc -l) / 2) + 1 ))

    # move cursor to correct row and overwrite content
    printf "\e[%d;0H" "$row"

    # top
    echo "╔$(printf '=%.0s' $(seq 1 "$len"))╗"
    echo "║ $title $(printf ' %.0s' $(seq 1 "$((len - 10))")) ║" # yeah the formatting is bootleg, i'm tired, myb

    # sides
    echo "║$(printf ' %.0s' $(seq 1 "$len"))║" # empty line
    # for ((i = 1; i <= num_lines; i++)); do
    echo "║ $text $(printf ' %.0s' $(seq 1 "$((len / 5))"))║"

    # bottom
    echo "╚$(printf '=%.0s' $(seq 1 "$len"))╝"
    echo -e "\n<enter - select, q - quit, b - back>"
}

end_screen() {
    tput cnorm
    tput cup 9 0
    stty echo
    exit 0
}

trap end_screen EXIT

printf "\033[H\033[2J"

# initialize opt1 highlighted
highlighted=1
sub1_highlighted=0
sub2_highlighted=0

# print options with initial highlighting
box "$highlighted"

while true; do
    tput civis
    read -rsn1 key # reads single char input without echoing to terminal and stores in key variable
    if [ "$sub1" == true ]; then
        # handle submenu arrow key presses
        case "$key" in
            D)  # left
                sub1_highlighted=$(( (sub1_highlighted - 1 + ${#submenu_opt1[@]}) % ${#submenu_opt1[@]} ))
                submenu_opt1
                ;;
            C)  # right
                sub1_highlighted=$(( (sub1_highlighted + 1) % ${#submenu_opt1[@]} ))
                submenu_opt1
                ;;
        esac
    elif [ "$sub2" == true ]; then
        case "$key" in
            D)  # left
                sub2_highlighted=$(( (sub2_highlighted - 1 + ${#submenu_opt2[@]}) % ${#submenu_opt2[@]} ))
                submenu_opt2
                ;;
            C)  # right
                sub2_highlighted=$(( (sub2_highlighted + 1) % ${#submenu_opt2[@]} ))
                submenu_opt2
                ;;
        esac
    else
        # handle main options arrow key presses
        case "$key" in
            D)  # left arrow - highlight opt1
                highlighted=1
                box "$highlighted"
                ;;
            C)  # right arrow - highlight opt2
                highlighted=2
                box "$highlighted"
                ;;
        esac
    fi

    case "$key" in
        q)  # q key - quit
            break
            ;;
        b)
            sub1=false
            sub2=false
            highlighted=1
            box "$highlighted"
            ;;
        "") # enter key
            if [ "$highlighted" -eq 1 ]; then
                # enter key pressed on opt1
                sub1=true
                submenu_opt1
            elif [ "$highlighted" -eq 2 ]; then
                # enter key pressed on opt2
                sub2=true
                submenu_opt2
            fi
            ;;
    esac
done
