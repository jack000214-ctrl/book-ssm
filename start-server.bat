@echo off
echo Downloading Jetty Runner...
if not exist jetty-runner.jar (
    powershell -Command "Invoke-WebRequest -Uri 'https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-runner/9.4.48.v20220622/jetty-runner-9.4.48.v20220622.jar' -OutFile 'jetty-runner.jar'"
)

echo Starting server on port 8000...
java -jar jetty-runner.jar --port 8000 --path / web

pause
