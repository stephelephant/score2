from configparser import ConfigParser
from urllib.request import urlopen, Request
from selectolax.parser import HTMLParser
from data_classes import PlayerData


def load_config(file):
   config = ConfigParser()
   try:
      config.read(file)
   except Exception as e:
      print("Could not read settings file: " + str(e))
   
   return config


def get_players_data(url: str) -> list:
   
   try:
      print(f"{url}")
      r = Request(url, headers={"User-Agent": "Mozilla/5.0"})
      
      with urlopen(r) as html:
         print(html.status)
         read_html = html.read()
      
   except Exception as e:
      print(f"could not get {url}:" + str(e))

   if html.status != 200:

      print(f"Status code not 200 for {url}{html.status}")
      return []
   
   parse = HTMLParser(read_html)
   
   #initial empty list
   player_data_list = []
   # get table body 
   tbody = parse.css_first("tbody")
   player_data = tbody.css("th[data-stat=player]")
   year_min_data = tbody.css("td[data-stat=year_min]")
   year_max_data = tbody.css("td[data-stat=year_max]")
   pos_data = tbody.css("td[data-stat=pos]")
   height_data = tbody.css("td[data-stat=height]")
   weight_data = tbody.css("td[data-stat=weight]")

   for (_player,
        _yearmi,
        _yearmx, 
        _pos,
        _height, 
        _weight
    ) in zip(player_data,
             year_min_data,
             year_max_data,
             pos_data,
             height_data,
             weight_data
             ):
         _player_a = _player.css_first("a")
         player_name = _player_a.text()
         player_url = _player_a.attributes['href']
         yearmi = _yearmi.text()
         yearmx = _yearmx.text()
         pos = _pos.text()
         height = _height.text()
         weight = _weight.text()

         player_data = PlayerData(player_url,
                                  player_name,
                                  yearmi,
                                  yearmx,
                                  pos,
                                  height,
                                  weight)
         player_data_list.append(player_data)
   
   
   print("success")
   return player_data_list
   

def page_url_gen(baseURL, charList):
   return [f"{baseURL}{char}" for char in charList]   


def importPlayerData(txt: str) -> list:

   data_list = []
   with open(txt, 'r') as file:
      datalines = file.readlines()
   
   for entry in datalines:
      urlstart = entry.find("'")
      urlend = entry.find("'", urlstart+1)
      url = entry[urlstart+1:urlend]

      namestart = entry.find("'",urlend+1)
      nameend = entry.find("'", namestart+1)
      name = entry[namestart+1:nameend]

      minStart = entry.find("'",nameend+1)
      minEnd = entry.find("'", minStart+1)
      min = entry[minStart+1:minEnd]

      maxStart = entry.find("'", minEnd+1)
      maxEnd = entry.find("'", maxStart+1)
      max = entry[maxStart+1:maxEnd]

      posStart = entry.find("'", maxEnd+1)
      posEnd = entry.find("'", posStart+1)
      pos = entry[posStart+1:posEnd]

      htStart = entry.find("'", posEnd+1)
      htEnd = entry.find("'", htStart+1)
      ht = entry[htStart+1:htEnd]

      wtStart = entry.find("'", htEnd+1)
      wtEnd = entry.find("'", wtStart+1)
      wt = entry[wtStart+1:wtEnd]

      pd = PlayerData(url, name, min, max, pos, ht, wt)
      data_list.append(pd)
   
   return data_list

   









# def get_active_players():
#   vars = config['GET ACTIVE PLAYERS']
#   baseURL = vars['baseURL']
#   charList = vars['charList']
#   active_players = []
#   ap_links = []

#   for char in charList:
#     try: 
#       with urlopen(f'{baseURL}{char}/') as html:
#         soup = BeautifulSoup(html, features="html.parser")
#     except Exception as e:
#        print("could not connect: " + str(e))

#     th = soup.findAll('th', "left", {'data-stat':'player'})
  
#     players = [th[x].getText() for x in range(0,len(th)) if "strong" in str(th[x])]
    
    
#     for p in players:
#       active_players.append(p)

#     href_list = [th[x].findAll('a')[0]['href'] for x in range(0,len(th)) if "strong" in str(th[x])]

#     for path in href_list:
#        ap_links.append(path)

#   # player_href = {k:v for (k,v) in zip(active_players,ap_links)}

#   table = [(name, url) for (name,url) in zip(active_players,ap_links)]
#   return table
    


  

  # return active_players


# def get_game_log_url(extn_url):
#   vars = config['GET_GAME_LOG_URL']
#   baseURL = vars['baseURL']
#   extn = extn_url
#   with urlopen(baseURL + extn) as html:
#     soup = BeautifulSoup(html, features="html.parser")


#   find = soup.findAll("li", "full hasmore")[0].findAll('a')
  
#   length_of_find = len(find)
#   url_list = [find[x]['href'] for x in range(length_of_find)]
#   # season = [find[x].text for x in range(length_of_find)]

#   # g_URLs = {k:v for (k,v) in zip(season,url_list)}

#   return url_list

# def get_game_log(extn_url,m=0):
#   vars = config['GET_GAME_LOG']
#   baseURL = vars['baseURL']
#   with urlopen(baseURL + extn_url) as html:
#     soup = BeautifulSoup(html, features="html.parser")
  
#   # rows of the game
#   table_row = soup.findAll("tr", id = re.compile("pgl_basic.."))

#   #tabel data from iterating through rows
#   #first section is getting the column data to initiate the dataframe



#   tuple_list = []
#   for x in range(len(table_row)):
#     if x == 0:
#       table_data = table_row[x].findAll("td")
#       length = len(table_data)
#       data_stat = [table_data[i]['data-stat'] for i in range(length)]
#       txt = [table_data[i].text for i in range(length)]
#       tup = tuple(txt)
#       tuple_list.append(tup)
#       data_dic = {k:[v] for (k,v) in zip(data_stat, txt)}
#       df = pd.DataFrame(data_dic)
      
#     else:
#       table_data = table_row[x].findAll("td")
#       length = len(table_data)
#       data_stat = [table_data[i]['data-stat'] for i in range(length)]
#       txt = [table_data[i].text for i in range(length)]
#       tup = tuple(txt)
#       tuple_list.append(tup)
#       df.loc[len(df.index)] = txt



#   df['ref_path'] = extn_url
#   df['season'] = str(extn_url)[-4:]

#   if m == 1:
#      return tuple_list
#   else:
#     return df



  
                         

