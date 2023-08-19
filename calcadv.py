import math
import webbrowser
import random
import calcgraph

memory = []

em_list = ['<(￣︶￣)>', '(￢‿￢ )', '⸜( *ˊᵕˋ* )⸝', '(ﾉ´ з `)ノ',
           '(*¯ ³¯*)♡', '(´꒳`)♡', '(＃￣ω￣)', '(҂ `з´ )', 'ᕕ( ᐛ )ᕗ',
           '┐(‘～` )┌', '(¯ . ¯٥)', '(￣～￣;)', '(o´▽`o)ﾉ', 'ヾ( `ー´)シφ__',
           '(＿ ＿*) Z z z', 'ʕ •̀ ω •́ ʔ', '~(˘▽˘~)', '( ˘ ɜ˘) ♬♪♫',
           '٩(ˊ〇ˋ*)و', '(￣^￣)ゞ', 'ଘ(੭ˊ꒳ˋ)੭✧']
sk_replace = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('s', '5')]

emoticon_mode_enabled = False
sk_mode_enabled = False


def op_list(args):
    global emoticon_mode_enabled
    global sk_mode_enabled

    try:
        currentArgument = args[0]
        # args[1] = num and args[2] = num2

        if currentArgument in ('-em', '--emoticons'):
            emoticon_mode_enabled = not emoticon_mode_enabled
            if emoticon_mode_enabled:
                print('\n>>> [*] Emoticon mode enabled! There are 21 total; can you catch them all? (´ ∀ ` *)\n')
            else:
                print('\n>>> [*] Emoticon mode disabled (￣～￣;)\n')
        elif currentArgument in ('-sk', '--script-kiddie'):
            sk_mode_enabled = not sk_mode_enabled
            if sk_mode_enabled:
                print('\n>>> [*] 5cr1pt k1dd13 m0d3 3n4bl3d <3\n')
            else:
                print('\n>>> [*] Script kiddie mode disabled </3 (not very 1337 of you ngl)\n')
        elif currentArgument in ('-a', '--add'):
            print('\n>>> [*] Calculating . . .\n')
            add(args[1], args[2])
        elif currentArgument in ('-s', '--subtract'):
            print('\n>>> [*] Calculating . . .\n')
            sub(args[1], args[2])
        elif currentArgument in ('-m', '--multiply'):
            print('\n>>> [*] Calculating . . .\n')
            mult(args[1], args[2])
        elif currentArgument in ('-d', '--divide'):
            print('\n>>> [*] Calculating . . .\n')
            div(args[1], args[2])
        elif currentArgument in ('-ex', '--exponent'):
            print('\n>>> [*] Calculating . . .\n')
            expo(args[1], args[2])
        elif currentArgument in ('-sq', '--square-root'):
            print('\n>>> [*] Calculating . . .\n')
            sqrt(args[1])
        elif currentArgument in ('-abs', '--abs-value'):
            print('\n>>> [*] Calculating . . .\n')
            absv(args[1])
        elif currentArgument in ('-rad', '--rad-from-deg'):
            print('\n>>> [*] Converting . . .\n')
            rad(args[1])
        elif currentArgument in ('-deg', '--deg-from-rad'):
            print('\n>>> [*] Converting . . .\n')
            deg(args[1])
        elif currentArgument in ('-f', '--factorial'):
            print('\n>>> [*] Calculating . . .\n')
            fact(args[1])
        elif currentArgument in ('-S', '--sine'):
            print('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            sin(angle)
        elif currentArgument in ('-C', '--cosine'):
            print('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            cos(angle)
        elif currentArgument in ('-T', '-tangent'):
            print('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            tan(angle)
        elif currentArgument in ('-aS', '--arc-sin'):
            print('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            arcsin(angle)
        elif currentArgument in ('-aC', '--arc-cos'):
            print('\n>>> [*] Calculating . . .\n')
            angle = args[1]
            arccos(angle)
        elif currentArgument in ('-aT', '--arc-tan'):
            print('\n[*] Calculating . . .\n')
            angle = args[1]
            arctan(angle)
        elif currentArgument in ('-l', '--log'):
            print('\n>>> [*] Calculating . . .\n')
            base = args[2]
            logs(args[1], base)
        elif currentArgument in ('-mo', '--morse-code'):
            print('>>> This feature isn\'t available yet </3')
        elif currentArgument in ('-mr', '--memory-recall'):
            print('\n>>> [*] Recovering . . .\n')
            if memory:
                for idx, result in enumerate(memory, start=0):
                    print(f'Result {idx}: {result}\n')
            else:
                print('>>> No results in memory </3\n')
        elif currentArgument in ('-mc', '--memory-clear'):
            print('\n>>> [*] Clearing . . .\n')
            memory.clear()
            print('>>> [*] Memory cleared <3\n')
        elif currentArgument in ('-g', '--github'):
            url = 'https://github.com/pwnedbyisa/advanced-calc-cli'
            webbrowser.open(url)
        elif currentArgument in ('-gm', '--graphing-mode'):
            equation = args[1]
            left, right = calcgraph.parse_equation(equation)
            if left.lower() == 'y':
                graph = calcgraph.generate_graph(right)
                print(graph)
        # pi and e at the bottom because they interfere w other functions and cause list index out of range errors
        elif args[1] == '[pi]':
            args[1] = float(math.pi)
            out(args[1])
        elif args[1] == '[e]':
            args[1] = float(math.e)
            out(args[1])
        else:
            print('\n>>> Argument Not Recognized: -h or --help for help\n')

    except Exception as e:
        print('\n>>> Error:', str(e) + '\n' + '\n>>> Please use the -h or --help argument to see proper formatting\n')


# this is a decorator, no I don't really understand how it works but it does
def out(func):
    def wrapper(*args, **kwargs):

        args = list(args)
        for i in range(len(args)):
            if args[i] == '[pi]':
                args[i] = float(math.pi)
            elif args[i] == '[e]':
                args[i] = float(math.e)

        result = func(*args, **kwargs)

        if sk_mode_enabled:
            for replace_tuple in sk_replace:
                char_to_replace, replacement = replace_tuple
                result = result.replace(char_to_replace, replacement)

        if emoticon_mode_enabled:
            emoticon = random.choice(em_list)
            result += f'\t {emoticon}'

        print(result)
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
        return f'>>> The sum of {num} and {num2} is {addition}\n'

    except ValueError:
        print('>>> Invalid input. Please provide two valid numbers.\n')


@out
def sub(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        subtract = num - num2
        memory.append(subtract)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} minus {num2} is {subtract}\n'

    except ValueError:
        print('>>> Invalid input. Please provide two valid numbers.\n')


@out
def mult(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        multiply = num * num2
        memory.append(multiply)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} multiplied by {num2} is {multiply}\n'

    except ValueError:
        print('>>> Invalid input. Please provide two valid numbers.\n')


@out
def div(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        divide = num / num2
        memory.append(divide)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} divided by {num2} is {divide}\n'

    except ValueError:
        print('>>> Invalid input. Please provide two valid numbers.\n')


@out
def expo(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        exp = num ** num2
        memory.append(exp)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} to the {num2} is {exp}\n'

    except ValueError:
        print('>>> Invalid input. Please provide two valid numbers.\n')


@out
def sqrt(num):
    try:
        num = float(num)
        sqt = num ** 0.5
        memory.append(sqt)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The square root of {num} is {sqt}\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number.\n')


@out
def absv(num):
    try:
        num = float(num)
        absval = abs(num)
        memory.append(absval)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The absolute value of {num} is {absval}\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number.\n')


@out
def rad(num):
    try:
        num = float(num)
        radian = math.radians(num)
        memory.append(radian)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} degrees is {radian} radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number.\n')


@out
def deg(num):
    try:
        num = float(num)
        degree = math.degrees(num)
        memory.append(degree)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} radians is {degree} degrees\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number.\n')


@out
def fact(num):
    try:
        num = int(num)
        factorial = math.factorial(num)
        memory.append(factorial)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> {num} factorial is {factorial}\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid integer (max 1558).\n')


@out
def cos(angle):
    try:
        angle = float(angle)
        cosine = math.cos(math.radians(angle))
        memory.append(cosine)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The cosine of {angle} degrees is {cosine} radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def sin(angle):
    try:
        angle = float(angle)
        sine = math.sin(math.radians(angle))
        memory.append(sine)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The sine of {angle} degrees is {sine} radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def tan(angle):
    try:
        angle = float(angle)
        tangent = math.tan(math.radians(angle))
        memory.append(tangent)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The tangent of {angle} degrees is {tangent} radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number for the angle.\n')


@out
def arcsin(angle):
    try:
        angle = float(angle)
        arcsinr = math.asin(angle)
        arcsind = math.degrees(math.asin(angle))
        memory.append(f'{arcsinr}, {arcsind}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse sine of {angle} is  {arcsind} in degrees and {arcsinr} in radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number within the domain [-1, 1].\n')


@out
def arccos(angle):
    try:
        angle = float(angle)
        arccosd = math.degrees(math.acos(angle))
        arccosr = math.acos(angle)
        memory.append(f'{arccosr}, {arccosd}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse cosine of {angle} is {arccosd} in degrees and {arccosr} in radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number within the domain [-1, 1].\n')


@out
def arctan(angle):
    try:
        angle = float(angle)
        arctand = math.degrees(math.atan(angle))
        arctanr = math.atan(angle)
        memory.append(f'{arctanr}, {arctand}')

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The inverse tangent of {angle} is {arctand} in degrees and {arctanr} in radians\n'

    except ValueError:
        print('>>> Invalid input. Please provide a valid number within the domain.\n')


@out
def logs(num, base):
    try:
        num = float(num)
        base = float(base)
        log = math.log(num, base)
        memory.append(log)

        if len(memory) > 10:
            memory.pop(0)
        return f'>>> The logarithm of {num} base {base} is {log}\n'

    except ValueError:
        print('>>> Invalid input. Format <number> <base>.\n')


def main():
    prompt = '$ '

    # banner
    print('\n')
    # raw bc the second line wasn't printing for wtv reason
    print(r' .d8888b.        d8888 888      .d8888b.       888     888  d888        d888')
    print('d88P  Y88b      d88888 888     d88P  Y88b      888     888 d8888       d8888')
    print(r'888    888     d88P888 888     888    888      888     888   888         888')
    print(r'888           d88P 888 888     888             Y88b   d88P   888         888')
    print(r'888          d88P  888 888     888              Y88b d88P    888         888')
    print(r'888    888  d88P   888 888     888    888        Y88o88P     888         888')
    print(r'Y88b  d88P d8888888888 888     Y88b  d88P         Y888P      888   d8b   888')
    print(r' "Y8888P" d88P     888 88888888 "Y8888P"           Y8P     8888888 Y8P 8888888 ')
    print('\n\t    Welcome to Calc CLI! Input -h or --help for options <3\n' + '=' * 79 + '\n')

    while True:
        currentArgument = input(prompt)

        if currentArgument in ('exit', 'quit', 'bye', 'peace', 'close'):
            print("\n>>> Exiting CalcCLI. Bye!\n")
            break
        elif currentArgument in ('-h', '--help'):
            print('\nFormat: <options> <number(s)>\n'
                  'Example: -a [pi] 23 \n' + '-' * 79)
            print(
                '\n\nBasic Functions vvv\n' + '-' * 79 + '\n'
                '-a, --add\t <addition>\n-s, --subtract\t <subtraction>\n'
                '-m, --multiply\t <multiplication>\n-d, --divide\t <division>\n-ex, --exponent\t <exponent, [num] [exp]>\n'
                '-sq, --square-root\t <square root>\n-abs, --abs-value\t <absolute value>\n'
                '-l, --log\t <logarithm, [num] [base]>\n-f, --factorial\t <return factorial (!) value>\n\n'
                '\nTrig Functions vvv\n' + '-' * 79 + '\n'
                '-rad, --rad-from-deg\t <output radians from degrees>\n-deg, --deg-from-rad\t <output degrees from radians>\n'
                '-S, --sine\t <sine>\n-C, --cosine\t <cosine>\n-T, --tangent\t <tangent>\n'
                '-aS, --arc-sin\t <inverse of sine>\n-aC, --arc-cos\t <inverse of cosine>\n-aT, --arc-tan\t <inverse of tangent>\n\n'
                '\nInput Numbers vvv\n' + '-' * 79 + '\n'
                '[e]\t <e as input>\n[pi]\t <pi as input>\n\n'
                '\nOutput Settings vvv\n' + '-' * 79 + '\n'
                '-sk, --script-kiddie\t <r35ult l00k5 l1k3 th15>\n'
                # source for more when implemented http://kaomoji.ru/en/
                '-em, --emoticons\t <result gets one of these (´ ω `@)>\n'
                '-gm, --graphing-mode\t <graph an equation - ex// -gm y=3x+2>'
                '\nMemory vvv\n' + '-' * 79 + '\n'
                '-mr, --memory-recall\t <recall previous result(s) (up to 10)>\n'
                '-mc, --memory-clear\t <clear all saved results>\n\n'
                '\nHelp/ Resources vvv\n' + '-' * 79 + '\n'
                '-h, --help\t <help menu>\n-g, --github\t <redirect to github repo>'
            )
        else:
            args = currentArgument.split(' ')
            op_list(args)


if __name__ == '__main__':
    main()
