copy \\servername\wpkg\srvany.exe %SystemRoot%\System32
copy \\servername\wpkg\instsrv.exe %SystemRoot%\System32
instsrv "Windows Packager" "%SystemRoot%\System32\srvany.exe"
\\servername\wpkg\scriptpl.exe /Q /R:N
cscript.exe \\servername\wpkg\install-service.js
net start "Windows Packager"

