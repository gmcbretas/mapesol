FOR /f "tokens=*" %%i IN ('"C:\ProgramData\chocolatey\lib\docker-machine\bin\docker-machine.exe" env default') DO %%i
set DOCKER_CERT_PATH=%DOCKER_CERT_PATH%\
