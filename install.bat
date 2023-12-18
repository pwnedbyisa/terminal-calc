@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
  echo.
  echo Usage %0 [option]
  echo Set Default Color:
  echo -r Red -o Orange -y Yellow -g Green -b Blue -p Purple -w White
  echo.
) else (
  set "colorCode="
  :parseArgs
  if "%~1"=="-r" set "colorCode=\033[0;31m"
  if "%~1"=="-o" set "colorCode=\033[0;33m"
  if "%~1"=="-y" set "colorCode=\033[0;33m"
  if "%~1"=="-g" set "colorCode=\033[0;32m"
  if "%~1"=="-b" set "colorCode=\033[0;36m"
  if "%~1"=="-p" set "colorCode=\033[0;35m"
  if "%~1"=="-w" set "colorCode=\033[0;37m"

  if not "!colorCode!"=="" (
    echo !colorCode! > default.txt
  ) else (
    echo Invalid option: %1
    exit /b 1
  )

  shift
  if not "%~1"=="" goto parseArgs
  echo [*] Installation Complete
)
