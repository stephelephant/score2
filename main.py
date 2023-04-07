from functions import load_config, get_player_urls

config = load_config('.settings.ini')


def main():
    
    getplayers_cfg = config['GETPLAYERS']
    url = getplayers_cfg['baseURL']

    names = get_player_urls(url)
    print(names)
    




if __name__ == "__main__":
    main()

