import urllib.request
#decoding jason
import json
import time
#parsing jason data
from collections import OrderedDict
#twillo
from twilio.rest import Client
account_sid = #"account_sid"
auth_token = #"auth_token"
client = Client(account_sid, auth_token)


def get_jason_data():


    #getting jason from url
    #link from ethermine. Go to your miner and then JASON API
    url = 'https://ethermine.org/api/miner_new/58801ebec6685d0d5461a30999fa5df91549a59e'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    #parse
    data = json.loads(html, object_pairs_hook=OrderedDict)

    return data


def get_RhashRate():
    data = get_jason_data()
    #getting hash rate
    RhashRateStr =  data['reportedHashRate']
    RhashRateNum = ""
    x = 0
    while RhashRateStr[x] != ' ':
        RhashRateNum += RhashRateStr[x]
        x += 1

    RhashRate = float(RhashRateNum)
    return RhashRate
def get_ChashRate():
    data = get_jason_data()
    #getting hash rate
    ChashRateStr =  data['hashRate']
    ChashRateNum = ""
    x = 0
    while ChashRateStr[x] != ' ':
        ChashRateNum += ChashRateStr[x]
        x += 1

    ChashRate = float(ChashRateNum)
    return ChashRate

def check_11th_min():
    c_time = time.time()
    day = 60 * 60 * 24
    today = c_time % day
    minutes_today = int(today / 60)
    if minutes_today % 10 == 1:
        return True
    return False

def call_message():
    RhashRate = get_RhashRate()
    ChashRate = get_ChashRate()
    if ChashRate == 0:
        # Any phone number / Must be a valid Twilio number
        message1 = client.api.account.messages.create(to="+12223334444", from_="+13334445555", body="Miner is at abnormal low levels, please check.")


        call = client.api.account.calls\
              .create(to="+12223334444",  # Any phone number
                      from_="+13334445555", # Must be a valid Twilio number
                      url="https://demo.twilio.com/docs/voice.xml")


def main():

    call_message()
    print('reportedHashRate: ',get_RhashRate(), 'currentHashRate',get_ChashRate())


    min_11 = check_11th_min()
    while min_11 == False:
        min_11 = check_11th_min()

    while 1 > 0:

        #10 min break
        init_time = int(time.time())
        loop_time = int(time.time())
        while loop_time - init_time < 600:
            loop_time = time.time()

        call_message()


main()
