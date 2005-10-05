rem rózne metody instalacji na koncówkach 
rem 1 metoda dla wpkg - windows packager 
rem zainstalowaæ nalezy z konta administratora za 1 razem 
rem uwaga parametr "/sc Przy_uruchomieniu " zale¿y od wersji jezykowej systemu windows 
schtasks /create /tn wpkg /tr "\\server\wpkg\wpkg-start.bat" /sc Przy_uruchomieniu /ru domena\adminuser /rp password 
rem 2 metoda dla wpkg - podmontowanie jako dysk sieciowy udzia³u wpkg 
plik C:\NETINST\wpkg-start.bat 
net use W: \\servername\wpkg /user:domain\user password 
cscript W:\wpkg.js /synchronize /quiet 
net use W: /delete 
rem 3 metoda dla wpkg - windows packager 
rem instalacja jako us³uga za pomoca pliku bat
wpkg-install-service.bat
