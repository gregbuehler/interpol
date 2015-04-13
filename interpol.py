#!/bin/env python

import requests
import argparse
import json
import os, sys
import pprint
from bs4 import BeautifulSoup

result = []

def getDetails(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text)

  subject = {}
  subject['photo'] = "http://interpol.int%s " % soup.find('img', { 'class': 'photo' }).get('src')

  for section in soup.findAll('table', { 'class': 'table_detail_profil' }):
    for row in section.findAll('tr'):
      if "family name" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['lastname'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "forename" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['firstname'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "sex" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['sex'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "date of birth" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['dob'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "place of birth" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['pob'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "language" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['languages'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "nationality" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['nationality'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "height" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['height'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "hair" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['hair'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "eyes" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['eyes'] = row.find('td', { 'class': 'col2' }).text.strip()

      if "charges" in row.find('td', { 'class': 'col1' }).text.lower():
        subject['charges'] = row.find('td', { 'class': 'col2' }).text.strip()


  return subject

def getSex(sex):
  return {
    "male": "M",
    "m": "M",
    "female": "F",
    "f": "F",
    "u": "U",
    "unknown": "U",
  }.get(sex.lower(), '')

def getHair(hair):
  return {
    "black": "BLA",
    "blue": "BLU",
    "lightblue ": "BLUL",
    "brown": "BRO",
    "darkbrown": "BROD",
    "hazel": "BROH",
    "lightbrown": "BROL",
    "green": "GRE",
    "grey": "GRY",
    "misc": "OTHC",
    "dark": "OTHD",
    "light": "OTHL"
  }.get(hair.lower(), '')

def getNationality(nationality):
  return {
    "afghanistan": "102",
    "albania": "105",
    "algeria": "160",
    "americansamoa": "111",
    "andorra": "100",
    "angola": "108",
    "anguilla": "104",
    "antigua": "103",
    "barbuda": "103",
    "argentina": "110",
    "armenia": "106",
    "aruba": "114",
    "australia": "113",
    "austria": "112",
    "azerbaijan": "116",
    "bahamas": "130",
    "bahrain": "123",
    "bangladesh": "119",
    "barbados": "118",
    "belarus": "134",
    "belgium": "120",
    "belize": "135",
    "benin": "125",
    "bermuda": "126",
    "bhutan": "131",
    "bolivia": "128",
    "bosnia": "117",
    "herzegovina": "117",
    "botswana": "133",
    "brazil": "129",
    "britishvirginislands": "330",
    "brunei ": "127",
    "bulgaria": "122",
    "burkinafaso": "121",
    "burundi": "124",
    "cambodia": "212",
    "cameroon": "145",
    "canada": "136",
    "capeverde": "151",
    "caymanislands": "219",
    "centralafricanrepublic": "139",
    "chad": "306",
    "chile": "144",
    "china": "146",
    "colombia": "147",
    "comoros": "214",
    "congo": "140",
    "drcongo": "138",
    "costarica": "148",
    "croatia": "195",
    "cuba": "150",
    "curacao": "342",
    "cyprus": "153",
    "czechrepublic": "154",
    "cotedivoire": "142",
    "denmark": "157",
    "djibouti": "156",
    "dominica": "158",
    "dominicanrepublic": "159",
    "ecuador": "161",
    "egypt": "163",
    "elsalvador": "302",
    "equatorialguinea": "185",
    "eritrea": "165",
    "estonia": "162",
    "ethiopia": "167",
    "fiji": "169",
    "finland": "168",
    "macedonia": "238",
    "france": "173",
    "gabon": "174",
    "gambia": "182",
    "georgia": "177",
    "germany": "155",
    "ghana": "179",
    "gibraltar": "180",
    "greece": "186",
    "grenada": "176",
    "guatemala": "188",
    "guinea": "183",
    "guinea bissau": "190",
    "guyana": "191",
    "haiti": "196",
    "honduras": "194",
    "hongkong": "192",
    "hungary": "197",
    "icc": "923",
    "iceland": "205",
    "tribunalrwanda": "921",
    "tribunalyugoslavia": "920",
    "india": "201",
    "indonesia": "198",
    "iran": "204",
    "iraq": "203",
    "ireland": "199",
    "israel": "200",
    "italy": "206",
    "jamaica": "207",
    "japan": "209",
    "jordan": "208",
    "kazakhstan": "220",
    "kenya": "210",
    "kiribati": "213",
    "northkorea": "216",
    "southkorea": "217",
    "kuwait": "218",
    "kyrgyzstan": "211",
    "laos": "221",
    "latvia": "230",
    "lebanon": "222",
    "lesotho": "227",
    "liberia": "226",
    "libya": "231",
    "liechtenstein": "224",
    "lithuania": "228",
    "luxembourg": "229",
    "macao": "242",
    "madagascar": "236",
    "malawi": "250",
    "malaysia": "252",
    "maldives": "249",
    "mali": "239",
    "malta": "247",
    "marshallislands": "237",
    "mauritania": "245",
    "mauritius": "248",
    "mexico": "251",
    "micronesia": "171",
    "moldova": "234",
    "monaco": "233",
    "mongolia": "241",
    "montenegro": "235",
    "montserrat": "246",
    "morocco": "232",
    "mozambique": "253",
    "myanmar": "240",
    "namibia": "254",
    "nauru": "263",
    "nepal": "262",
    "netherlands": "260",
    "newzealand": "265",
    "nicaragua": "259",
    "niger": "256",
    "nigeria": "258",
    "norway": "261",
    "oman": "266",
    "pakistan": "272",
    "palau": "279",
    "panama": "267",
    "papuanewguinea": "270",
    "paraguay": "280",
    "peru": "268",
    "philippines": "271",
    "poland": "273",
    "portugal": "278",
    "puertorico": "276",
    "qatar": "281",
    "romania": "283",
    "russia": "284",
    "rwanda": "285",
    "saintkitts": "215",
    "nevis": "215",
    "saintlucia": "223",
    "saintvincent": "328",
    "grenadines": "328",
    "samoa": "335",
    "sanmarino": "297",
    "saotome": "301",
    "principe": "301",
    "saudiarabia": "286",
    "courtsierraleone": "922",
    "senegal": "298",
    "serbia": "341",
    "seychelles": "288",
    "sierraleone": "296",
    "singapore": "291",
    "saintmaarten": "343",
    "slovakia": "295",
    "slovenia": "293",
    "solomonislands": "287",
    "somalia": "299",
    "southafrica": "338",
    "southsudan": "344",
    "spain": "166",
    "srilanka": "225",
    "stl": "924",
    "sudan": "289",
    "suriname": "300",
    "swaziland": "304",
    "sweden": "290",
    "switzerland": "141",
    "syria": "303",
    "taiwan": "319",
    "tajikistan": "310",
    "tanzania": "320",
    "thailand": "309",
    "timor": "312",
    "togo": "308",
    "tonga": "315",
    "trinidad ": "317",
    "tobago": "317",
    "tunisia": "314",
    "turkey": "316",
    "turkmenistan": "313",
    "turks": "305",
    "tuvalu": "318",
    "uganda": "322",
    "ukraine": "321",
    "kosovo": "913",
    "uae": "101",
    "uk": "175",
    "usa": "324",
    "uruguay": "325",
    "uzbekistan": "326",
    "vanuatu": "333",
    "vatican": "327",
    "venezuela": "329",
    "vietnam": "332",
    "yemen": "336",
    "zambia": "339",
    "zimbabwe": "340",
  }.get(nationality.lower(), '')

def search_url(url):
    searchEndpoint = url

    headers = {
        'User-Agent': "Mozilla/4.0",
        'Host': 'www.interpol.int',
        'Origin': 'http://www.interpol.int',
        'Referer': 'http://www.interpol.int/notice/search/wanted'
    }

    r = requests.get(searchEndpoint, headers=headers)
    soup = BeautifulSoup(r.text)

    for person in soup.findAll('a', { 'class': 'details' }):
      result.append(getDetails("http://www.interpol.int%s" % person['href']))

def search(lastname="", forenames="", nationality="", text="", age_min=0, age_max=100, sex="", eyes="", hair="", wantedby=""):

  searchEndpoint = "http://interpol.int/notice/search/wanted"

  query = {
    'search': 1,
    'Name': lastname,
    'Forename': forenames,
    'Nationality': getNationality(nationality),
    'FreeText': text,
    'current_age_mini': age_min,
    'current_age_maxi': age_max,
    'Sex': sex,
    'Eyes': eyes,
    'Hair': hair,
    'RequestingCountry': getNationality(nationality),
    'data': ''
  }

  headers = {
      'User-Agent': "Mozilla/4.0",
      'Host': 'www.interpol.int',
      'Origin': 'http://www.interpol.int',
      'Referer': 'http://www.interpol.int/notice/search/wanted'
  }

  r = requests.post(searchEndpoint, headers=headers, data=query)
  soup = BeautifulSoup(r.text)

  for person in soup.findAll('a', { 'class': 'details' }):
    result.append(getDetails("http://www.interpol.int%s" % person['href']))

  pagenation = soup.find('span', { 'class': 'num_page' })
  pageCount = pagenation.findAll('span')[-1].findAll('a')[0].text
  pageUrl = pagenation.findAll('span')[-1].findAll('a')[0]['href']

  maxOffset = (int(pageCount) - 1) * 9
  for page in range(2, int(pageCount) - 1):
    currentOffset = int(page) * 9
    search_url("http://www.interpol.int%s" % pageUrl.replace('(offset)/%d' % maxOffset, '(offset)/%d' % currentOffset))


# main -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Interpol query tool", add_help=False)
parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')
parser.add_argument('-l', '--lastname', '--name', help='lastname', default="")
parser.add_argument('-f', '--firstname', help='firstname(s)', default="")
parser.add_argument('-n', '--nationality', help='nationality', default="")
parser.add_argument('-t', '--freetext', help='freetext to search', default="")
parser.add_argument('--age-min', help='minimum age', default="0")
parser.add_argument('--age-max', help='maximum age', default="100")
parser.add_argument('-s', '--sex', help='sex, \'male\', \'female\', or \'unknown\'.', default="")
parser.add_argument('-e', '--eyes', help='eye color', default="")
parser.add_argument('-h', '--hair', help='hair color', default="")
parser.add_argument('-w', '--wantedby', help='wanted by', default="")
args = vars(parser.parse_args())

if len(sys.argv) == 1:
   parser.print_help()
   sys.exit(1)

search(lastname=args['lastname'], forenames=args['firstname'], nationality=args['nationality'],text=args['freetext'], age_min=args['age_min'], age_max=args['age_max'], sex=args['sex'], eyes=args['eyes'], hair=args['hair'], wantedby=args['wantedby'])
print json.dumps(result, indent=2)
