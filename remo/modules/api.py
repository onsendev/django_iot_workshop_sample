import os
import json
import pprint
import requests

class NatureRemoApi:
    
    REMO_ACTIONS = {
        'light_on_off': 'xxxxx',
    }
    
    def fetch_sensor_values(self):
        """現在のセンサーの値をNature Cloud APIから取得する。
        
        Returns:
            Nature Cloud APIのレスポンスの['newest_events']のタプル。室温, 湿度, 照度の順番
        """
        try:
            response = requests.get(
                'https://api.nature.global/1/devices',
                headers=self.__build_header()
            )
            response = response.json()
            newest_events = response[1]['newest_events']
            
            return (
                newest_events['te']['val'],
                newest_events['hu']['val'],
                newest_events['il']['val'], )
                
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"エラーが発生しました。 {type(e)}: {e}")
            raise
        

    def invoke_remo_action(self, action_name):
        """Nature Cloud APIを叩き、Nature Remoから赤外線信号を発出する。
        
        Returns: 成功した場合はTrue
        """
        try:
            action_id = self.REMO_ACTIONS[action_name]
            if action_id is None:
                raise ValueError("無効な action_id が指定されました")
            
            response = requests.post(
                f"https://api.nature.global/1/signals/{action_id}/send",
                headers=self.__build_header()
            )
            return True
    
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"エラーが発生しました。 {type(e)}: {e}")
            raise
            

    def __get_access_token(self):
        return os.environ.get('NATURE_REMO_API_KEY')

    def __build_header(self):
        return {'Authorization': 'Bearer ' + self.__get_access_token()}
       
