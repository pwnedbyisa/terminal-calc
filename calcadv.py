import math
import sys
import webbrowser

# to do
# input numbers
# set up memory
# output custom


def op_list():
    if len(sys.argv) == 1:
        return None

    try:
        for i in range(1, len(sys.argv), 2):
            currentArgument = sys.argv[i]
            if currentArgument in ('-h', '--help'):
                print('\nFormat: python3 calcadv.py <options> <number(s)>\n'
                      'Example: python3 calcadv.py -a 84 23 \n' + '-' * 79)
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
                    '-sk, --script-kiddie\t <re5ult 100k5 1ik3 th15>\n'
                    '-mo, --morse-code\t <.-. . ... ..- .-.. - / .-.. --- --- -.- ... / .-.. .. -.- . / - .... .. ...>\n'
                    # source for more when implemented http://kaomoji.ru/en/
                    '-em, --emoticons\t <result gets one of these (´ ω `@)>\n'
                    '\nMemory vvv\n' + '-' * 79 + '\n'
                    '-mr, --memory-recall\t <recall previous result(s) (up to 10)>\n'
                    '-mc, --memory-clear\t <clear all saved results>\n\n'
                    '\nHelp/ Resources vvv\n' + '-' * 79 + '\n'
                    '-h, --help\t <help menu>\n-g, --github\t <redirect to github repo>'
                )
            elif currentArgument in ('-a', '--add'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                num2 = sys.argv[i + 2]
                add(num, num2)
                break  # break after two args because otherwise it prints the else statement w the answer
            elif currentArgument in ('-s', '--subtract'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                num2 = sys.argv[i + 2]
                sub(num, num2)
                break
            elif currentArgument in ('-m', '--multiply'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                num2 = sys.argv[i + 2]
                mult(num, num2)
                break
            elif currentArgument in ('-d', '--divide'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                num2 = sys.argv[i + 2]
                div(num, num2)
                break
            elif currentArgument in ('-ex', '--exponent'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                num2 = sys.argv[i + 2]
                expo(num, num2)
                break
            elif currentArgument in ('-sq', '--square-root'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                sqrt(num)
            elif currentArgument in ('-abs', '--abs-value'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                absv(num)
            elif currentArgument in ('-rad', '--rad-from-deg'):
                print('\n[*] Converting . . .\n')
                num = sys.argv[i + 1]
                rad(num)
            elif currentArgument in ('-deg', '--deg-from-rad'):
                print('\n[*] Converting . . .\n')
                num = sys.argv[i + 1]
                deg(num)
            elif currentArgument in ('-f', '--factorial'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                fact(num)
            elif currentArgument in ('-S', '--sine'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                sin(angle)
            elif currentArgument in ('-C', '--cosine'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                cos(angle)
            elif currentArgument in ('-T', '-tangent'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                tan(angle)
            elif currentArgument in ('-aS', '--arc-sin'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                arcsin(angle)
            elif currentArgument in ('-aC', '--arc-cos'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                arccos(angle)
            elif currentArgument in ('-aT', '--arc-tan'):
                print('\n[*] Calculating . . .\n')
                angle = sys.argv[i + 1]
                arctan(angle)
            elif currentArgument in ('-l', '--log'):
                print('\n[*] Calculating . . .\n')
                num = sys.argv[i + 1]
                base = sys.argv[i + 2]
                logs(num, base)
                break
            elif currentArgument in ('-mr', '--memory-recall'):
                print('\n[*] Recovering . . .\n')
                print('This feature isn\'t available yet </3')
            elif currentArgument in ('-mc', '--memory-clear'):
                print('\n[*] Clearing . . .\n')
                print('This feature isn\'t available yet </3')
            elif currentArgument in ('-g', '--github'):
                url = 'https://github.com/pwnedbyisa'
                webbrowser.open(url)
            else:
                print('Argument Not Recognized: -h or --help for help')
    except Exception as e:
        print('Error:', str(e))


def add(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        addition = num + num2
        print(f'The sum of {num} and {num2} is {addition}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers.\n')


def sub(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        subtract = num - num2
        print(f'{num} minus {num2} is {subtract}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers.\n')


def mult(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        multiply = num * num2
        print(f'{num} multiplied by {num2} is {multiply}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers.\n')


def div(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        divide = num / num2
        print(f'{num} divided by {num2} is {divide}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers.\n')


def expo(num, num2):
    try:
        num = float(num)
        num2 = float(num2)
        exp = num ** num2
        print(f'{num} to the {num2} is {exp}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers.\n')


def sqrt(num):
    try:
        num = float(num)
        sqt = num ** 0.5
        print(f'The square root of {num} is {sqt}\n')

    except ValueError:
        print('Invalid input. Please provide a valid number.\n')


def absv(num):
    try:
        num = float(num)
        absval = abs(num)
        print(f'The absolute value of {num} is {absval}\n')

    except ValueError:
        print('Invalid input. Please provide a valid number.\n')


def rad(num):
    try:
        num = float(num)
        radian = math.radians(num)
        print(f'{num} degrees is {radian} radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number.\n')


def deg(num):
    try:
        num = float(num)
        degree = math.degrees(num)
        print(f'{num} radians is {degree} degrees\n')

    except ValueError:
        print('Invalid input. Please provide a valid number.\n')


def fact(num):
    try:
        num = int(num)
        factorial = math.factorial(num)
        print(f'{num} factorial is {factorial}\n')

    except ValueError:
        print('Invalid input. Please provide a valid integer (max 1558).\n')


def cos(angle):
    try:
        angle = float(angle)
        cosine = math.cos(math.radians(angle))
        print(f'The cosine of {angle} degrees is {cosine} radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number for the angle.\n')


def sin(angle):
    try:
        angle = float(angle)
        sine = math.sin(math.radians(angle))
        print(f'The sine of {angle} degrees is {sine} radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number for the angle.\n')


def tan(angle):
    try:
        angle = float(angle)
        tangent = math.tan(math.radians(angle))
        print(f'The tangent of {angle} degrees is {tangent} radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number for the angle.\n')


def arcsin(angle):
    try:
        angle = float(angle)
        arcsinr = math.asin(angle)
        arcsind = math.degrees(math.asin(angle))
        print(f'The inverse sine of {angle} is  {arcsind} in degrees and {arcsinr} in radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number within the domain [-1, 1].\n')


def arccos(angle):
    try:
        angle = float(angle)
        arccosd = math.degrees(math.acos(angle))
        arccosr = math.acos(angle)
        print(f'The inverse cosine of {angle} is {arccosd} in degrees and {arccosr} in radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number within the domain [-1, 1].\n')


def arctan(angle):
    try:
        angle = float(angle)
        arctand = math.degrees(math.atan(angle))
        arctanr = math.atan(angle)
        print(f'The inverse tangent of {angle} is {arctand} in degrees and {arctanr} in radians\n')

    except ValueError:
        print('Invalid input. Please provide a valid number within the domain.\n')


def logs(num, base):
    try:
        num = float(num)
        base = float(base)
        log = math.log(num, base)
        print(f'The logarithm of {num} base {base} is {log}\n')

    except ValueError:
        print('Invalid input. Please provide two valid numbers for the logarithm.\n')


def main():
    # banner
    if len(sys.argv) == 1:
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
    else:
        op_list()


if __name__ == '__main__':
    main()
