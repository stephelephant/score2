from functions import load_config, get_players_data

config = load_config('.settings.ini')


def main():
    
    getplayers_cfg = config['GETPLAYERS']
    b_url = getplayers_cfg['baseURL']
    charList = getplayers_cfg['charList']
    
    list_s =[]
    for char in charList:
        
        url = f"{b_url}{char}"

        try:
            ttt = get_players_data(url)
        except AttributeError as ae:
            print("error occured with :" + str(ae) + str(ae))
            print(str(url))
            
            pass
        list_s.append(ttt)

    flat_list_s = [pData for subList in list_s for pData in subList]


    return flat_list_s
    




if __name__ == "__main__":
    main()

