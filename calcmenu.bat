:: this fully does not work bc chat gpt made it bc I can't code in batch <3
@echo off
title [ -- Options -- ]
set "opt1=>> Colors/Theme"
set "opt2=>> Language"
set "submenu_opt1=
^>^> Red
^>^> Orange
^>^> Yellow
^>^> Green
^>^> Blue
^>^> Purple
^>^> White"

set "submenu_opt2=
^>^> English
^>^> Spanish
^>^> French"

set main=true
set sub1active=false
set sub2active=false
set highlighted=1
set sub_highlighted=0

:print_opts
cls

if %1==1 (
    echo %opt1%
    echo.
    echo %opt2%
)
else (
    echo %opt1%
    echo.
    echo %opt2%
    echo.
)
goto :EOF

:sub_menu
setlocal EnableDelayedExpansion
cls

for /l %%i in (1,1,%#%) do (
    if %%i==%sub_highlighted% (
        echo %%~1
    ) else (
        echo.
    )
    shift
)
endlocal
goto :EOF

:list
set "text="
call :print_opts %1
set "row=4"

:: Clear any remaining submenu
for /l %%i in (7,1,%lines%) do (
    call :clear_line %%i
)

:: Set cursor position
call :set_cursor_position %row%
echo %text%
goto :EOF

:clear_line
cls
setlocal EnableDelayedExpansion

for /l %%i in (0,1,%cols%) do (
    set "line=!line! "
)
echo.!line!
endlocal
goto :EOF

:set_cursor_position
echo ESC[!%1!;0H
goto :EOF

:: Create an empty exp.txt if it doesn't exist
if not exist exp.txt (
    echo. > exp.txt
)

:get_color
set "option=%~1"
setlocal EnableDelayedExpansion

if "!option!"=="^>^> Red" (
    set "color=^[[0;31m"
)
else if "!option!"=="^>^> Orange" (
    set "color=^[[0;33m"
)
else if "!option!"=="^>^> Yellow" (
    set "color=^[[0;33m"
)
else if "!option!"=="^>^> Green" (
    set "color=^[[0;32m"
)
else if "!option!"=="^>^> Blue" (
    set "color=^[[0;34m"
)
else if "!option!"=="^>^> Purple" (
    set "color=^[[0;35m"
)
else if "!option!"=="^>^> White" (
    set "color=^[[0;37m"
)

:: Change the text color to the desired color
color !color!
:: Display the success message in the specified color
echo !color! "^>> New color set successfully"
:: Reset the text color to the default (usually white)
color 07

echo.!color! > exp.txt
endlocal
goto :EOF

:: Initialize console
cls
echo ESC[H
echo ESC[2J
echo.%title%
echo.

:: Trap for cleaning up before exit
:cleanup
set "main=%main:*%%=1"
set "sub1active=%sub1active:*%%=1"
set "sub2active=%sub2active:*%%=1"
set "highlighted=%highlighted:*%%=1"
set "sub_highlighted=%sub_highlighted:*%%=1"
exit /b

:trap
call :cleanup
goto :EOF

:: Initialize the script
call :cleanup
call :print_opts 1
call :set_cursor_position 4
set "exp_color="

:: Main loop
:main_loop
set "input="
choice /n /c:wabq /t:0,1 >nul
set /p "input="

if "%input%"=="w" (
    if %main%==true (
        set "highlighted=1"
        call :list %highlighted%
    )
)

if "%input%"=="a" (
    if %main%==true (
        call :cleanup
        set "sub1active=true"
        set "sub_highlighted=0"
        call :sub_menu %submenu_opt1%
    )
)

if "%input%"=="b" (
    if %main%==true (
        call :cleanup
        set "sub2active=true"
        set "sub_highlighted=0"
        call :sub_menu %submenu_opt2%
    )
)

if "%input%"=="q" (
    goto :trap
)

if "%input%"=="" (
    if %main%==true (
        if %highlighted%==1 (
            call :cleanup
            set "sub1active=true"
            set "sub_highlighted=0"
            call :sub_menu %submenu_opt1%
        ) else if %highlighted%==2 (
            call :cleanup
            set "sub2active=true"
            set "sub_highlighted=0"
            call :sub_menu %submenu_opt2%
        )
    )
)
goto :main_loop
