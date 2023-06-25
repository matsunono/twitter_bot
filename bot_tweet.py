import tweepy
import glob
import random
import datetime

def Tweet_Commander(client, in_path, comander_flag = 0, old_num = 0, freq = 4):
	dt_now = datetime.datetime.now()
	if dt_now.hour % freq == 0 and dt_now.minute == 0 and dt_now.second == 0:
		if comander_flag == 0:
			old_num = Rand_Tweet(client, in_path, old_num)
			comander_flag = 1
		else:
			comander_flag = 1
	else:
		comander_flag = 0
	return comander_flag, old_num

def Rand_Tweet(client, in_path, old_num = 0):
	files = glob.glob(in_path + '/*.txt')
	file_max = len(files)
	rand_num = random.randrange(0, file_max, 1)
	while rand_num == old_num:
		rand_num = random.randrange(0, file_max, 1)
	txt_data = Read_Text(files[rand_num])
	print(txt_data)
	client.create_tweet(text = txt_data)
	old_num = rand_num
	return old_num

def Set_Client(bearar_token, consumer_key, consumer_secret, access_token_key, access_token_secret):
	client = tweepy.Client(
		bearer_token = bearar_token,
		consumer_key = consumer_key,
		consumer_secret = consumer_secret,
		access_token = access_token_key,
		access_token_secret = access_token_secret
	)
	return client

def Read_Text(file):
	f = open(file, 'r', encoding='utf-8')
	txt_data = f.read()
	f.close()
	return txt_data