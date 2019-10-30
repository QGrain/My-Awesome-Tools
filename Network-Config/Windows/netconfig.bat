@echo off
if "%1" == "help" goto usage
if "%1" == "static" goto static
if "%1" == "dhcp" goto dhcp

:usage
echo Usage: netconfig.bat [static][dhcp][help]
goto end

:static
echo Using static mode for 709
netsh interface ip set address "以太网" static 192.168.9.189 255.255.255.0 192.168.9.254
netsh interface ip set dnsservers "以太网" static 202.114.0.131 primary
echo Static-config finish with ip:192.168.9.189
goto end

:dhcp
echo Using dhcp mode
netsh interface ip set address name="以太网" source=dhcp
netsh interface ip set dnsservers name="以太网" source=dhcp
echo Dhcp-config finish
goto end

:end
echo netconfig finish
pause 
