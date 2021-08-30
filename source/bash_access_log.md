You are working on a site and need to perform Apache access log analysis.
The IT team needs statistics on **requests per day** and **requests per IP**.

* **Bash version 5.0 is installed, and your script will run on Debian Linux**

### Your task

Create a Bash script to parse and analyze the Apache access log file.
The path to the log file is passed as the first parameter to the script (the initial solution stores the log file path in the `LOG_FILE` variable).
This means that if your script is stored in `solution.sh`, it can be called as `bash solution.sh /var/log/access.log`, and should analyze this specific log file.

You need to output two statistics, limited to the top 10 results and sorted numerically by quantity from highest to lowest value without leading blanks and that lines with greater key
 values appear earlier in the output instead of later.
Your script should output both results one after the other, and each row must have `QUANTITY FIELD` format, with either space or tabulator as separator.

The Apache log has the following example content:

```
172.19.0.104 - - [25/Jul/2019:22:32:02 +0000] "GET /index HTTP/1.1" 200 14034 "-" "Mozilla/5.0 (compatible; SemrushBot/6~bl; +http://www.semrush.com/bot.html)" "172.19.0.4"
172.19.0.104 - - [26/Jul/2019:22:31:32 +0000] "GET /site HTTP/1.1" 200 36565 "https://command-not-found.com/curl" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)" "172.19.0.3"
172.19.0.105 - - [26/Jul/2019:22:30:10 +0000] "GET /credits HTTP/1.1" 200 31067 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)" "172.19.0.2"
172.19.0.106 - - [27/Jul/2019:22:30:10 +0000] "GET /index HTTP/1.1" 200 31067 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)" "172.19.0.2"
172.19.0.104 - - [28/Jul/2019:22:35:10 +0000] "GET /index HTTP/1.1" 200 31067 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)" "172.19.0.2"
```

The first statistic is **requests per day**.

The **day** value is located in brackets in every log entry and must be extracted to have only a date value without a time: for example `16/Feb/2020`. The correct output for this statistic using the above example log is:

```
2 26/Jul/2019
1 25/Jul/2019
1 27/Jul/2019
1 28/Jul/2019
```

The second statistic is **requests per IP**.

The **IP** value is located at the very beginning of each log entry and must be extracted. The correct output for this statistic using the above example log is:

```
3 172.19.0.104
1 172.19.0.105
1 172.19.0.106
```

* **Ensure your Bash script contains robust code, as it is checked with a static code analyzer.**
