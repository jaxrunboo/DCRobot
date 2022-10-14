'''
Author: bobo 1052028084@qq.com
Date: 2022-10-14 10:42:31
LastEditors: bobo 1052028084@qq.com
LastEditTime: 2022-10-14 17:10:12
FilePath: /test/underdog-work.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from datetime import datetime
import json
from random import random
import requests
import schedule


def send_msg(msg):
    url = 'https://discord.com/api/v9/channels/<频道id>/messages'
    input = {
        'content': msg,
        'tts': False
    }
    header = {
        'authorization': '',
        'content-type': 'application/json',
        'user-agent': ''
    }
    res = requests.post(url=url, data=json.dumps(input), headers=header)
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date_str + ':'+res.content)


if __name__ == "__main__":
    schedule.every().day.at('10:30').do(send_msg, '$work')
    schedule.every(3).to(4).hours.do(send_msg, '$collect')
    while (True):
        print('开始执行...')
        schedule.run_pending()
