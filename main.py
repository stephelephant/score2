from functions import load_config, get_players_data, open_pool_manager, page_url_gen
import requests
from urllib.request import Request
config = load_config('.settings.ini')


def main():
    
    getplayers_cfg = config['GETPLAYERS']
    b_url = getplayers_cfg['baseURL']
    charList = getplayers_cfg['charList']
    

    # get URL list
    url_list = page_url_gen(b_url, charList)

    pd_list =[]
    
    for url in url_list:
        
        try:
            print(f"trying url: " + str(url))
            pd = get_players_data(session, url)
            pd_list.append(pd)
        except Exception as e:
            print("could not get data for" + str(url))
            pass
    
    

    
        


    
    flat_list_s = [pData for subList in pd_list for pData in subList]


    return flat_list_s
    




if __name__ == "__main__":
    main()

