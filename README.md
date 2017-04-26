# panostoblock
This python script uses the PanOS api to generate an external blocklist that you can point your Palo Alto firewall to

### Requirements ###

This script uses the untangle, time, os and requests modules so be sure that they're installed 

### Usage ###

1.  Generate an api key for use with this script
2.  Add the api key to the script in the Key variable
3.  Add the remainder of the variables specific to your environment
4.  Run the script and verify that the list is generated and matches your firewall threat logs
5.  Create a cron job to make sure that your list is updated regularly
6.  Ensure that you can see the blacklist from a web browser
7.  Add the blacklist to your Palo Alto firewall as an external blacklist
8.  Create a firewall policy to block traffic based on that external blacklist

### Notes ###

Be sure to look through the documentation for your version of PanOS to ensure you're api calls are correct.  
I run this script on Python 3.  Don't know if it works with 2.  
I'm still new to python so I'm sure this isn't optimized or pretty.  Be gentle.  
