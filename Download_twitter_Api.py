from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'ji9vCqDbFcGhsypHxCjMqduzS'
consumer_secret = 'AUVEoLydwVa7hZibP4AtDjLCMEnCEr5mSoPbV9rdj72dBDkG24'
access_token = '172229939-sdWHOaIKoRHQMedUI7HgcJjsVyzlJaC88k2zsUNj'
access_secret = '9mF59UuOsswC3CKDKVVjsGjTWrAbaUFqhIT7KMh4eQEFB'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])
