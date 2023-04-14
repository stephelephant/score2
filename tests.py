import unittest
import functions

class TestFunctionsConfigFile(unittest.TestCase):
    
    def test_read_config(self):
        inifile = '.settings.ini'
        with open(inifile, 'r') as f:
            content = f.readlines()
        first = content[0]
        dummy = content[13]
        self.assertEqual(first, '[CONFIG]\n')
        self.assertEqual(dummy, 'dummy = dummytest')

    def test_load_config(self):
        inifile = '.settings.ini'
        cf = functions.load_config(inifile)
        self.assertTrue(cf['GETPLAYERS'])
        self.assertTrue(cf['GET_GAME_LOG_URL'])
        self.assertTrue(cf['GET_GAME_LOG'])


class TestGetPlayersData(unittest.TestCase):
    
    def test_return_one_char(self):
        static_url = "https://www.basketball-reference.com/players/a/"
        data = functions.get_players_data(static_url)
        self.assertTrue(data != None)

    def test_return_many_char(self):
        charList = 'abdehpw'
        static_url = "https://www.basketball-reference.com/players/"
        url_list = [f"{static_url}{char}" for char in charList]

        pd_list = []
        for url in url_list:
            data = functions.get_players_data(url)
            pd_list.append(data)

        for pd in pd_list:
            self.assertTrue(pd != None)
        


    


    



if __name__ == '__main__':
    unittest.main()