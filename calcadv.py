import math
import subprocess
import webbrowser  # dependency
import random
import os
import calcgraph

COLORS = {
    'default': '\033[0;36m',  # cyan
    'reset': '\033[0m',  # reset text color to default
}

color = COLORS['default']


def print_color(text):
    print(color + text + COLORS['reset'])


memory = []

em_list = ['<(￣︶￣)>', '(￢‿￢ )', '⸜( *ˊᵕˋ* )⸝', '(ﾉ´ з `)ノ',
           '(*¯ ³¯*)♡', '(´꒳`)♡', '(＃￣ω￣)', '(҂ `з´ )', 'ᕕ( ᐛ )ᕗ',
           '┐(`～` )┌', '(¯ . ¯٥)', '(￣～￣;)', '(o´▽`o)ﾉ', 'ヾ( `ー´)シφ__',
           '(＿ ＿*) Z z z', 'ʕ •̀ ω •́ ʔ', '~(˘▽˘~)', '( ˘ ɜ˘) ♬♪♫',
           '٩(ˊ〇ˋ*)و', '(￣^￣)ゞ', 'ଘ(੭ˊ꒳ˋ)੭✧']
sk_replace = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('s', '5')]

emoticon_mode_enabled = False
sk_mode_enabled = False


def op_list(args):
    global emoticon_mode_enabled
    global sk_mode_enabled
    global color

    try:
        currentArgument = args[0]
        # args[1] = num and args[2] = num2

        if currentArgument in ('-em', '--emoticons'):
            emoticon_mode_enabled = not emoticon_mode_enabled
            if emoticon_mode_enabled:
                print_color('\n>>> [*] Emoticon mode enabled! There are 21 total; can you catch them all? (´ ∀ ` *)\n')
            else:
                print_color('\n>>> [*] Emoticon mode disabled (￣～￣;)\n')
        elif currentArgument in ('-sk', '--script-kiddie'):
            sk_mode_enabled = not sk_mode_enabled
            if sk_mode_enabled:
                print_color('\n>>> [*] 5cr1pt k1dd13 m0d3 3n4bl3d <3\n')
            else:
                print_color('\n>>> [*] Script kiddie mode disabled </3 (not very 1337 of you ngl)\n')
        elif currentArgument in ('-a', '--add'):
            print_color('\n>>> [*] Calculating . . .\n')
            add(args[1], args[2])
        elif currentArgument in ('-s', '--subtract'):
            print_color('\n>>> [*] Calculating . . .\n')
            sub(args[1], args[2])
        elif currentArgument in ('-m', '--multiply'):
            print_color('\n>>> [*] Calculating . . .\n')
            mult(args[1], args[2])
        elif currentArgument in ('-d', '--divide'):
            print_color('\n>>> [*] Calculating . . .\n')
            div(args[1], args[2])
        elif currentArgument in ('-ex', '--exponent'):
            print_color('\n>>> [*] Calculating . . .\n')
            expo(args[1], args[2])
        elif currentArgument in ('-sq', '--square-root'):
            print_color('\n>>> [*] Calculating . . .\n')
            sqrt(args[1])
        elif currentArgument in ('-abs', '--abs-value'):
            print_color('\n>>> [*] Calculating . . .\n')
            absv(args[1])
        elif currentArgument in ('-rad', '--rad-from-deg'):
            print_color('\n>>> [*] Converting . . .\n')
            rad(args[1])
        elif currentArgument in ('-deg', '--deg-from-rad'):
            print_color('\n>>> [*] Converting . . .\n')
            deg(args[1])
        elif currentArgument in ('-f', '--factorial'):
            print_color('\n>>> [*] Calculating . . .\n')
            fact(args[1])
        elif currentArgument in ('-S', '--sine'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            sin(angle)
        elif currentArgument in ('-C', '--cosine'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            cos(angle)
        elif currentArgument in ('-T', '-tangent'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            tan(angle)
        elif currentArgument in ('-aS', '--arc-sin'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            arcsin(angle)
        elif currentArgument in ('-aC', '--arc-cos'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            arccos(angle)
        elif currentArgument in ('-aT', '--arc-tan'):
            print_color('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            arctan(angle)
        elif currentArgument in ('-l', '--log'):
            print_color('\n>>> [*] Calculating . . .\n')
            base = args[2]
            try:
                logs(args[1], base)
            except ZeroDivisionError:
                print_color(">>> [!] Zero division error - base of a log cannot be 1\n")
        elif currentArgument in ('-mo', '--morse-code'):
            print_color('>>> This feature isn\'t available yet </3')
        elif currentArgument in ('-mr', '--memory-recall'):
            print_color('\n>>> [*] Recovering . . .\n')
            if memory:
                for idx, result in enumerate(memory, start=0):
                    print_color(f'Result {idx}: {result}\n')
            else:
                print_color('>>> No results in memory </3\n')
        elif currentArgument in ('-mc', '--memory-clear'):
            print_color('\n>>> [*] Clearing . . .\n')
            memory.clear()
            print_color('>>> [*] Memory cleared <3\n')
        elif currentArgument in ('-c', '--clear'):
            clear_screen()
        elif currentArgument in ('-git', '--github'):
            url = 'https://github.com/pwnedbyisa/advanced-calc-cli'
            webbrowser.open(url)
        elif currentArgument in ('-gm', '--graphing-mode'):
            equation = args[1]
            left, right = calcgraph.parse_equation(equation)
            if left.lower() == 'y':
                graph = calcgraph.generate_graph(right)
                print_color(graph)
        elif currentArgument in ('-o', '--options'):
            # half cheating bc the amount of tomfoolery it takes to export child env vars to the parent process is ridiculous
            if 'nt' in os.name:  # windows
                # subprocess.run('calcmenu.bat')
                print_color("\n>> Implementation in progress \n")
            elif 'posix' in os.name:  # mac or linux - unix based
                subprocess.run('./calcmenu.sh')
                with open('exp.txt', 'r') as file:
                    color = file.read().strip()
            else:
                print_color("[!] OS not recognized")
        # pi and e at the bottom because they interfere w other functions and cause list index out of range errors
        elif args[1] == '[pi]':
            args[1] = float(math.pi)
            out(args[1])
        elif args[1] == '[e]':
            args[1] = float(math.e)
            out(args[1])
        else:
            print_color('\n>>> Argument Not Recognized: -h or --help for help\n')

    except IndexError:
        print_color('\n>>> Command Not Recognized/ Missing Parameters: use -h or --help for proper formatting\n')


def clear_screen():
    print_color("\033c")


# decorator for emoticon and sk modes (i partially understand how it works)
def out(func):
    def wrapper(*args, **kwargs):

        args = list(args)
        for i in range(len(args)):
            if args[i] == '[pi]':
                args[i] = float(math.pi)
            elif args[i] == '[e]':
                args[i] = float(math.e)

        result = func(*args, **kwargs)

        if result is None:
            result = ''  # fixing the nonetype errors w inverse trig domain handling

        if sk_mode_enabled:
            for replace_tuple in sk_replace:
                char_to_replace, replacement = replace_tuple
                result = result.replace(char_to_replace, replacement)

        if emoticon_mode_enabled:
            emoticon = random.choice(em_list)
            result += f'\t {emoticon}'

        print_color(result)
        return result

    return wrapper


@out
def add(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        addition = num + num2
        memory.append(addition)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The sum of {num} and {num2} equals {addition}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide two valid numbers.\n')


@out
def sub(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        subtract = num - num2
        memory.append(subtract)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} minus {num2} equals {subtract}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide two valid numbers.\n')


@out
def mult(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        multiply = num * num2
        memory.append(multiply)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} multiplied by {num2} equals {multiply}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide two valid numbers.\n')


@out
def div(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        divide = num / num2
        memory.append(divide)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} divided by {num2} equals {divide}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide two valid numbers.\n')


@out
def expo(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        exp = num ** num2
        memory.append(exp)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} to the {num2} equals {exp}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide two valid numbers.\n')


@out
def sqrt(num):
    try:
        num = float(num)
        sqt = num ** 0.5
        memory.append(sqt)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The square root of {num} equals {sqt}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number.\n')


@out
def absv(num):
    try:
        num = float(num)
        absval = abs(num)
        memory.append(absval)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The absolute value of {num} equals {absval}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number.\n')


@out
def rad(num):
    try:
        num = float(num)
        radian = math.radians(num)
        memory.append(radian)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} degrees equals {radian} radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number.\n')


@out
def deg(num):
    try:
        num = float(num)
        degree = math.degrees(num)
        memory.append(degree)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} radians equals {degree} degrees\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number.\n')


@out
def fact(num):
    try:
        num = int(num)
        factorial = math.factorial(num)
        memory.append(factorial)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} factorial equals {factorial}\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid integer (max 1558).\n')


@out
def cos(angle):
    try:
        angle = float(angle)
        cosine = math.cos(math.radians(angle))
        memory.append(cosine)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The cosine of {angle} degrees equals {cosine} radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def sin(angle):
    try:
        angle = float(angle)
        sine = math.sin(math.radians(angle))
        memory.append(sine)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The sine of {angle} degrees equals {sine} radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def tan(angle):
    try:
        angle = float(angle)
        tangent = math.tan(math.radians(angle))
        memory.append(tangent)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The tangent of {angle} degrees equals {tangent} radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def arcsin(angle):
    try:
        angle = float(angle)
        arcsinr = math.asin(angle)
        arcsind = math.degrees(math.asin(angle))
        memory.append(f'{arcsinr}, {arcsind}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse sine of {angle} equals  {arcsind} in degrees and {arcsinr} in radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number within the domain [-1, 1].\n')


@out
def arccos(angle):
    try:
        angle = float(angle)
        arccosd = math.degrees(math.acos(angle))
        arccosr = math.acos(angle)
        memory.append(f'{arccosr}, {arccosd}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse cosine of {angle} equals {arccosd} in degrees and {arccosr} in radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number within the domain [-1, 1].\n')


@out
def arctan(angle):
    try:
        angle = float(angle)
        arctand = math.degrees(math.atan(angle))
        arctanr = math.atan(angle)
        memory.append(f'{arctanr}, {arctand}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse tangent of {angle} equals {arctand} in degrees and {arctanr} in radians\n'

    except ValueError:
        print_color('>>> Invalid input. Please provide a valid number within the domain.\n')


@out
def logs(num, base):
    try:
        num = float(num)
        base = float(base)
        log = math.log(num, base)
        memory.append(log)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The logarithm of {num} base {base} equals {log}\n'

    except ValueError:
        print_color('>>> Invalid input. Format <number> <base>.\n')


def main():
    prompt = '$ '

    # banner v1.3
    print_color('\n')
    print_color(' ██████╗ █████╗ ██╗      ██████╗    ██╗   ██╗ ██╗   ██████╗ ')
    print_color('██╔════╝██╔══██╗██║     ██╔════╝    ██║   ██║███║   ╚════██╗')
    print_color('██║     ███████║██║     ██║         ██║   ██║╚██║    █████╔╝')
    print_color('██║     ██╔══██║██║     ██║         ╚██╗ ██╔╝ ██║    ╚═══██╗')
    print_color('╚██████╗██║  ██║███████╗╚██████╗     ╚████╔╝  ██║██╗██████╔╝')
    print_color(' ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝      ╚═══╝   ╚═╝╚═╝╚═════╝ ')
    print_color('\n   Welcome to Calc CLI! Input -h or --help for options <3\n' + '=' * 60 + '\n')

    
    while True:
        currentArgument = input(prompt)

        if currentArgument in ('exit', 'quit', 'bye', 'peace', 'close', 'q'):
            print_color("\n>>> Exiting CalcCLI. Bye!\n")
            break
        elif currentArgument in ('-h', '--help'):
            print_color('\nFormat: <options> <number(s)>\n'
                        'Example: -a [pi] 23 \n' + '-' * 79)
            print_color(
                '\n\nBasic Functions vvv\n' + '-' * 79 + '\n'
                '-a, --add\t\t <addition>\n-s, --subtract\t\t <subtraction>\n'
                '-m, --multiply\t\t <multiplication>\n-d, --divide\t\t <division>\n-ex, --exponent\t\t <exponent, [num] [exp]>\n'
                '-sq, --square-root\t <square root>\n-abs, --abs-value\t <absolute value>\n'
                '-l, --log\t\t <logarithm, [num] [base]>\n-f, --factorial\t\t <return factorial (!) value>\n\n'
                '\nTrig Functions vvv\n' + '-' * 79 + '\n'
                '-rad, --rad-from-deg\t <output radians from degrees>\n-deg, --deg-from-rad\t <output degrees from radians>\n'
                '-S, --sine\t\t <sine>\n-C, --cosine\t\t <cosine>\n-T, --tangent\t\t <tangent>\n'
                '-aS, --arc-sin\t\t <inverse of sine>\n-aC, --arc-cos\t\t <inverse of cosine>\n-aT, --arc-tan\t\t <inverse of tangent>\n\n'
                '\nInput Numbers vvv\n' + '-' * 79 + '\n'
                '[e]\t <e as input>\n[pi]\t <pi as input>\n\n'
                '\nOutput Settings vvv\n' + '-' * 79 + '\n'
                '-sk, --script-kiddie\t <r35ult l00k5 l1k3 th15>\n'
                '-o, --options\t\t <options menu>\n'
                # source for more when implemented http://kaomoji.ru/en/
                '-em, --emoticons\t <result gets one of these (´ ω `@)>\n'
                '-gm, --graphing-mode\t <graph an equation - ex// -gm y=3x+2>\n'
                '\nMemory vvv\n' + '-' * 79 + '\n'
                '-mr, --memory-recall\t <recall previous result(s) (up to 10)>\n'
                '-mc, --memory-clear\t <clear all saved results>\n\n'
                '\nHelp/ Resources vvv\n' + '-' * 79 + '\n'
                '-h, --help\t <help menu>\n'
                '-c, --clear\t <clear screen>\n-git, --github\t <redirect to github repo>\n\n'                                                                                                                                                                                                                                '-h, --help\t <help menu>\n-o, --options\t <settings menu>\n-c, --clear\t <clear screen>\n-git, --github\t <redirect to github repo>\n'
            )
        else:
            args = currentArgument.split(' ')
            op_list(args)


if __name__ == '__main__':
    main()
