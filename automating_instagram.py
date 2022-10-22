from instabot import Bot
var = Bot()
var.login(username="jone_python08",password="Kundeswhar15@")#it know thisis our infromation to 
var.follow("wscubetech")#follows this id automating 

#to upload pic 
var = Bot()
var.login(username="jone_python08",password="Kundeswhar15@")
var.upload_photo(r"upload your image links",caption="i love python")#it is upload image automatingcally


#for unfollow any person
var.unfollow("wscubetech")

#to send msg 
var.send_message("i lvoe python", ["rv_goswami", "kp_pangu"])

#to knows our followers
followers=Bot.get_user_followers("pass our username")
for i in followers:
    print(var.get_user_info(i))

#to knowing following list
following = var.get_user_following("username")
for j in following:
    print(var.get_user_info(j))

