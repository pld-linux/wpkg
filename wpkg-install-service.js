var WshShell = WScript.CreateObject("WScript.Shell");
var srvKey = "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Windows Packager\\Parameters\\";
var appKey = srvKey + "Application";
var srvPath = "C:\\NETINST\\wpkg-start.bat"
WshShell.RegWrite(appKey, srvPath, "REG_SZ");

