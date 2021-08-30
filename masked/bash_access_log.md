You are working on a site and need to do an Apache access log analysis.
The IT team needs statisitcs on requests per day and requests per IP.

* naw version 5.0 is installed, and your script will run on naw naw

### Your task

Create a naw script to parse and analyze the Apache access log file.
The path to the log file is passed as the first parameter to the script (the first solution stores the log file path in the LOG FILE variable).
This means that if your script is stored in solution naw, it can be called as naw solution naw var log access naw, and should analyze this specific log file.

You need to output two statistics. They should be limited to the top 10 results, sorted numerically by quantity from highest to lowest value without leading spaces, and lines with greater key values should appear earlier in the output instead of later.
Your script should output both results one after the other, and each row must have QUANTITY FIELD format, with either space or tabulator as separator.

The Apache log has the following example content:

naw

The first statistic is requests per day.

The day value is in brackets in every log entry and must be extracted to have only a date value without a time: for example 16 Feb 2020. The correct output for this statistic using the above example log is:

naw

The second statistic is requests per IP.

The IP value is at the very beginning of each log entry and must be extracted. The correct output for this statistic using the above example log is:

naw

* Make sure your naw script contains robust code, as it is checked with a static code analyzer.
