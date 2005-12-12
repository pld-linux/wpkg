set WPKGROOT=\\server\wpkg
set PACKAGES=%WPKGROOT%\packages
cscript %WPKGROOT%\wpkg\wpkg.js /synchronize /nonotify /quiet

REM This one is a recommended way of starting WPKG
REM \\server\wpkg\wpkg.js /synchronize /quiet
REM 
REM Use this one if you don't want the notify window
REM \\server\wpkg\wpkg.js /synchronize /quiet /nonotify
REM 
REM Use this one when logged in as Administrator to debug the problems
REM \\server\wpkg\wpkg.js /synchronize /debug
