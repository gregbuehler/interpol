interpol
========

This is utility script to query the Interpol wanted list. This currently only displays the top 9 results.


Example
-------
```
[16:29:55] :gbuehler/interpol  % python interpol.py --name jiang
{"hair": "Black", "eyes": "Brown", "firstname": "BO", "dob": "07/06/1978 (36 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2012-339073/wanted-GetPicture-57915839.jpg ", "sex": "Male", "languages": "Chinese, English", "charges": "Trafficking in Counterfeit Goods1) Conspiracy to Traffic in Counterfeit Goods\n2) Trafficking in Counterfeit Goods (29 counts)", "lastname": "JIANG", "nationality": "China", "height": "1.7 meter", "pob": "SHANDONG, China"}
{"hair": "Black", "eyes": "Black", "firstname": "HAIYU", "dob": "08/11/1973 (40 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2014-33214/wanted-GetPicture-59123168.jpg ", "sex": "Male", "languages": "Chinese", "charges": "Fraud", "lastname": "JIANG", "nationality": "China", "height": "1.74 meter", "pob": "JIANGSU PROVINCE, China"}
```