from instabot import Bot
import glob, os

try: 
	os.remove('config/' + 'YOURUSER' + '_uuid_and_cookie.json')
except:
    pass
    
bot = Bot ()

bot.login(username = (YOURUSER), password = (YOURPASS))

os.chdir("images")
for file in glob.glob("*.jpg"):
	bot.upload_photo(file, caption = "#instagram #instagood #love #like #follow #photography #photooftheday #instadaily #likeforlikes #picoftheday #fashion #bhfyp #beautiful #instalike #me #likes #followforfollowback #smile #followme #myself #art #photo #happy #style #likeforfollow #life #l #nature #followers #bhfyp")
						^ # aqui é a descrição da foto #
