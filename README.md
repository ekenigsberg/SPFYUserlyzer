# SPFYUserlyzer
Script that downloads Salesforce Storage Usage by user and object

Salesforce provides a way to view data storage by user by record, at this URL: https://na1.salesforce.com/setup/user/userstorageusage.jsp?id=0123456789ABCDE

. . . but AFAIK they don't provide a way to access that info via the API. This is a small script that leverages the simple-salesforce and chromedriver libraries 
to screenscrape the data storage by record, by user, for every active full user in your org and export the results to an Excel spreadsheet.
