# -*- coding: utf-8 -*-
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = "WKKql59c7afgt7LB8HglYwDq9"
csecret = "bX5nJ8TjPetkZtEyw3tKMck14MZqSnpuDo5hMTGGKhHYbLKVeN"
atoken = "861422254273507333-GiIWJiX3XMQQXna4A3LCrMTXlvLPWFW"
asecret = "uPLG5fexyKTnS4W8918zp5KZtnOOlTjygXLXRvFwjTiKh"

santiago = [ -70.454080, -33.325721, -70.815256,-33.592670] 

file =  open('tweets.txt', 'a')

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        data=json.loads(data)
        date=data['created_at']
        idstr=data['id_str']
        twitt=data['text'].replace('\n',' ')
        location=data['geo']
        if location==None:
            location='None'
        try:
            texto=idstr.encode('utf-8')+"|"+date.encode('utf-8')+"|"+twitt.encode('utf-8')+"|"+location.encode('utf-8')+'\n'
        except:
            texto=""
        file.write(texto)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    print 'Empezando...'

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, StdOutListener())
    #Here on track you can filter by specific words, but you can also filter by location or by username
    twitterStream.filter(track=['@MayolPresidente','@guillier', '@sebastianpinera','@carolinagoic', '@BeaSanchezYTu','@labeasanchez','@mjossandon','@AlbertoMayol','@felipekast'])
