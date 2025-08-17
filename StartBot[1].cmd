@echo off
chcp 65001 >nul
title GoldPowerSignalsBot
where python >nul 2>&1
if errorlevel 1 (
  echo ❌ Python не найден. Установите Python 3.10+ и перезапустите StartBot.cmd
  pause
  exit /b
)
set TOKEN=
if exist ".env" (
  for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    if /I "%%A"=="TOKEN" set TOKEN=%%B
  )
)
if "%TOKEN%"=="" (
  echo Введите токен Telegram-бота (из BotFather):
  set /p TOKEN=
  > .env echo TOKEN=%TOKEN%
)
echo Установка зависимостей...
python -m pip install -r requirements.txt
:loop
echo ====================================
echo 🚀 Запуск GoldPowerSignalsBot ...
echo ====================================
setlocal
set TOKEN=%TOKEN%
python bot.py
endlocal
echo ⚠️ Бот остановился. Перезапуск через 5 секунд...
timeout /t 5 >nul
goto loop
