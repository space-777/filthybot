import Location
from osuapi import OsuApi, ReqConnector
import requests


api_read = open("osuapikey.txt")
Token_read = open("Token.txt")

TOKEN = Token_read.readline()
apicode = api_read.readline()


api = OsuApi(apicode, connector=ReqConnector())

user = api.get_user("XavierSchiller")

print(user[0].user_id)
