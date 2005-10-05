var WshShell = WScript.CreateObject("WScript.Shell");
var srvKey = "HKLM\\SYSTEM\\CurrentControlSet\\Services\\WPKG\\Parameters\\";
var appKey = srvKey + "Application";
var srvPath = "\\\\servername\\wpkg\\wpkg-start.bat"
WshShell.RegWrite(appKey, srvPath, "REG_SZ");

