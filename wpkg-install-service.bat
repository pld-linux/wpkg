REM this batch file install WPKG as service in windows 2000/XP
REM use as administrator or user with administrators privileges
rem first get from net files: Srvany.exe Instsrv.exe scriptpl.exe
echo on
copy \\servername\wpkg\files\Srvany.exe %SystemRoot%\System32\
copy \\servername\wpkg\files\Instsrv.exe %SystemRoot%\System32\
%SystemRoot%\System32\Instsrv.exe "WPKG" "%SystemRoot%\System32\Srvany.exe"
REM do not must use in XP this????
REM install WHSC - Windows Host Script
\\servername\wpkg\files\scriptpl.exe /Q /R:N
REM 
cscript.exe \\servername\wpkg\files\install-service.js
net start "WPKG"

