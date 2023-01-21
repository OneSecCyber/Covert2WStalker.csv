# Covert2WStalker.csv

 **What it does?**

It converts the saved .xml formatted burpsuite proxy history to a .csv format, that can be imported in Logger ++

I switched to burpsuite community for same reason recently. I was trying different ways to save the burpsuite history but i was not able to do so. There was a feature in Logger ++ which we can use to import and export the proxy history in the format of CSV. But unfortunately, that was not working properly. I was looking on the internet to find some tools to do this. But I was not able to find anything even though there was a lot of discussion about this.

So, I decided to make a stupid script as soon as I got the perfect idea. And here is the result of my one hour.

> NOTE: it's not bullet proof; I have not done much testing. But it works for me.

Hope it can help you.


## Usage

**1) Save burpsuite proxy history to .xml file**
 - Go to proxy tab and select all history
 - right click and `save items` and save the file as <anything>.xml file

 ![save history](https://github.com/OneSecCyber/Covert2WStalker.csv/blob/main/save-history.png)


**2) Use this python script to convert this .xml file into .csv file, in the format of WStalker**

  python3 Covert2WStalker.py <Your proxy history log file in the format of .xml>
 
  **Example Usage** : `python3 Covert2WStalker.py history.xml`
 
 **3) Now you can import the output csv file into Logger ++**
   - Go to Logger++'s `Options` tab.
   - Click on `Import From WStalker CSV` and import the output CSV.
   



