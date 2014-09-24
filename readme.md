interpol
========

This is utility script to query the Interpol wanted list. This currently only displays the top 9 results.


Examples
-------

Search by last name:
```
[16:29:55] :gbuehler/interpol  % python interpol.py --name jiang
{"hair": "Black", "eyes": "Brown", "firstname": "BO", "dob": "07/06/1978 (36 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2012-339073/wanted-GetPicture-57915839.jpg ", "sex": "Male", "languages": "Chinese, English", "charges": "Trafficking in Counterfeit Goods1) Conspiracy to Traffic in Counterfeit Goods\n2) Trafficking in Counterfeit Goods (29 counts)", "lastname": "JIANG", "nationality": "China", "height": "1.7 meter", "pob": "SHANDONG, China"}
{"hair": "Black", "eyes": "Black", "firstname": "HAIYU", "dob": "08/11/1973 (40 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2014-33214/wanted-GetPicture-59123168.jpg ", "sex": "Male", "languages": "Chinese", "charges": "Fraud", "lastname": "JIANG", "nationality": "China", "height": "1.74 meter", "pob": "JIANGSU PROVINCE, China"}
```

Search by text:
```
[16:37:27] :gbuehler/interpol git:(master) % python interpol.py --freetext "terrorism"
{"hair": "Black", "eyes": "Brown", "firstname": "ILYAS", "dob": "10/02/1964 (50 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2010-11150/wanted-GetPicture-54041783.jpg ", "sex": "Male", "languages": "Urdu", "charges": "1) CONSPIRACY TO MURDER AND MAIM IN A FOREIGN COUNTRY (1 COUNT)\n2) CONSPIRACY TO PROVIDE MATERIAL SUPPORT TO TERRORISM IN A FOREIGN COUNTRY (1 COUNT)", "lastname": "KASHMIRI", "nationality": "Pakistan", "pob": "Pakistan"}
{"firstname": "IKHTIYOR", "dob": "25/12/1972 (41 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2010-24993/wanted-GetPicture-54100499.jpg ", "sex": "Male", "languages": "", "charges": "THE DESIGNED MURDER, THE THREAT BY MURDER OR BY THE USAGE OF VIOLENCE, THE DRAWING IN A MINOR INTO THE ANTISOCIAL BEHAVIOUR, THE VIOLATION OF THE CITIZENS EQUALITY OF RIGHTS, THE INFRINGEMENT OF THE CITIZENS DWELLING INVIOLABILITY, THE VIOLATION OF FREEDOM OF CONSCIENCE, THE TERRORISM, THE AGITATION OF THE NATIONAL, RACE OR RELIGIONS HOSTILITY, THE DIVERSION, THE ROBBERY, THE ORGANIZATION OF THE CRIMINAL COMMUNITY, THE LEGALIZATION OF INCOMES, RECEIVED BY CRIMINAL ACTIVITY, THE SMUGGLING, THE ILLEGAL SEIZURE OF FIRE-ARMS, AMMUNITION, EXPLOSIVE SUBSTANCES OR DEVICES, THE ILLEGAL POSSESSION OF ARMS, AMMUNITION, EXPLOSIVE SUBSTANCES OR DEVICES.", "lastname": "NURILLAEV", "nationality": "Uzbekistan", "pob": "KASHKADARYA, Uzbekistan"}
{"hair": "Black", "eyes": "Black", "firstname": "NAJEEB ULLAH", "dob": "22/06/1989 (25 years old)", "photo": "http://interpol.int//var/interpol/cache/ws/2012-300582/wanted-GetPicture-56550881.jpg ", "sex": "Male", "languages": "Panjabi, Urdu, English", "charges": "Murder, abetment, hurt, attempt to murder, Rioting\n   and Terrorism", "lastname": "ULLAH", "nationality": "Pakistan", "height": "1.73 meter", "pob": "CHAK JHUMRA FAISALABAD PUNJAB, Pakistan"}
```