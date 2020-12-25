import telepot
import requests
import time
import random
import json
token="bot-token"
def handle(msg):
    user_name=msg["from"]["first_name"]
    chat_id=msg["chat"]["id"]
    txt=msg["text"]
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if chat_id:
        txt = txt.lower()
        txt = txt.replace("?","")
        txt = txt.replace("/","")
        txt = txt.replace("your","ur")
        txt = txt.replace("you","u")
        txt = txt.replace("are","r")
        txt = txt.replace("good","gud")
        txt = txt.replace("morning","mrng")
        txt = txt.replace("evening","evng")
        txt = txt.replace("night","n8")
        if txt=="start":
            bot.sendMessage(chat_id,"Hi {},do you want to know my ability use '/help'".format(user_name))
        elif txt=="help":
                bot.sendMessage(chat_id,"Catlog of my skills \n1. Flames games : flames name1-name2(ex:flames akash-avinash)\n2. Child schooling(*give alphabets) :  *a to *z(ex: *c)\n3. Life quotes : quotes\n4. mini dictionary :dict english_meaning_full_words(ex:dict faith)\n5. chatting :i will chat")       
        elif "dict"in txt:
            txt=txt.replace("dict","")
            txt=txt.strip()
            url='https://api.dictionaryapi.dev/api/v2/entries/en/'+txt
            [get]=requests.get(url).json()
            try:
                b=(get["meanings"][0]["partOfSpeech"])
                c=(get["meanings"][0]["definitions"][0]['definition'])
                d=(get["meanings"][0]["definitions"][0]['example'])
                e=(get["meanings"][0]["definitions"][0]['synonyms'][0])
            except:
                bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhnhfnrYml4nzIeXNG4hbZtplIzXbTAACYwMAAvPjvgur9KLPD5qy0B4E")
                bot.sendMessage(chat_id,"This is mini dictionary so you can't get all the words")
            if isinstance(b,str) and isinstance(c,str) and isinstance(d,str) and isinstance(e,str):
                bot.sendMessage(chat_id,'partOfspeech - '+b+'\ndefinition - '+c+'\nexample - '+d+'\nsynonyms - '+e)
        elif "*"in txt:
            txt=txt.replace("*","")
            words=['angry','bat','cow','dog','egg','frog','ghost','horse','injection','jellyfish','kiwi','lion','monkey','niffler','owl','panda','queen','raccoon','shark','tiger','unicorn','virus','worm','xerox (no sticker available) ','yetti','zombie']
            stick=['CAACAgIAAxkBAAEBhQVfnWP6NrXaKpwX7LlzC5Pto20N4QACBAADr8ZRGhhqTEj6gDwaGwQ','CAACAgIAAxkBAAEBhQlfnWXWN46vYUJvrcoaOTJ-cJIC5gACigEAAjDUnRGebT-TPELwIRsE','CAACAgIAAxkBAAEBhQtfnWZwT4vB4lY6ZhSD1UBxvmQjnwACcwQAApzW5wqoj3BicrAQhxsE','CAACAgIAAxkBAAEBhQ9fnWb3-O8cs8Jr4zblW4zAXAfVMAAC8QADwZGyJAZLBo4isbi3GwQ','CAACAgIAAxkBAAEBhRFfnWdur7JHqKhqhc6Qea8Sq5HTfwACIAAD9wLID1KiROfjtgxPGwQ','CAACAgIAAxkBAAEBhRNfnWf9VkzqzeASh06jvZiJLRVzRgACYwMAAvPjvgur9KLPD5qy0BsE','CAACAgIAAxkBAAEBhRVfnWhxTOKdG8OuUy6U01Z2fOXA-QACVgMAAkcVaAnVh1Sn7wXRyxsE','CAACAgIAAxkBAAEBhRdfnWjH9IMkox4M6SvLxevNdHW9WQACZAEAAhAhAhAjIBJDt2TgZxsE','CAACAgIAAxkBAAEBhRlfnWkQRMEpcvY7ozpEFSw4Bs30zQACfwADmL-ADWfzbyVdVFmHGwQ','CAACAgIAAxkBAAEBhRtfnWsdh5Kyf22tPbN4dwrMTNb8UAACUQADwDZPExTRqeEWVGi2GwQ','CAACAgIAAxkBAAEBhR1fnXM9ka7VyDnekqo7R3_HH_cZhQACdgADJQNSD5NSJFpvrq1zGwQ','CAACAgIAAxkBAAEBhW1fnYOrkTHairfVejLGsaS25fzhJAACjwIAAs-71A51CZRf9nRP9BsE','CAACAgEAAxkBAAEBhW9fnYP42UlCZZacvbAvVikGmzy39QACEAEAAjgOghH-1L_EjUKlzBsE','CAACAgIAAxkBAAEBhXFfnYR_KESvwH04ZoQRQsF8Aj3ZeAACEQQAAsSraAvnCZ85_aHOvBsE','CAACAgIAAxkBAAEBhXNfnYUz0jEJg25SdRq3dn-fkZ9AMAACIAADwZxgDGWWbaHi0krRGwQ','CAACAgIAAxkBAAEBhXVfnYW6AAFayvmdVLL775-ZM1TqErwAAhECAAJWnb0KkovaUamDbFsbBA','CAACAgIAAxkBAAEBhXdfnYYBawyrT22EngzyyUTWSTCsNQAChAQAAj-VzAoG_52tQVVCiRsE','CAACAgIAAxkBAAEBhXlfnYZcfUMKRvX68CjnuD-rJlY4xQACWAMAAs-71A50qKHXJdURLBsE','CAACAgIAAxkBAAEBhXtfnYaOgBTWeZMeymz_Vo_HoXsTqwACNQMAAvJ-ggwuXixHOmSYahsE','CAACAgEAAxkBAAEBhX1fnYbNAYFKP8_LxzMP_Gj0E9PzsAAC6QADOA6CEbG9i22p0OzyGwQ','CAACAgIAAxkBAAEBhX9fnYclnYeH1MkFMN-p2IvoLQYAAfAAAvIIAAIYQu4Ipo0QtJ6OJlQbBA','CAACAgIAAxkBAAEBhYFfnYdv7FugodCRTwzcGetQaM5q9AACzgEAAladvQqto5rs5p76TBsE','CAACAgIAAxkBAAEBjRtfpiXTJW7tFaIxemlUxIZPgsZS9AACSgADDbbSGTG5qKE-wcYeHgQ','CAACAgIAAxkBAAEBhZNfnYpzNoaK5Afj99M3Jgi5qNn1LwACVQMAAvPjvgumW9W9B3nYGxsE','CAACAgIAAxkBAAEBhZZfnYsN2LHjILuV-CtNPb-ALBMTHgACBwADW__yCh-p-YKX23k0GwQ','CAACAgIAAxkBAAEBhZhfnYta7xWXq5P-qO5_e5LQOfV8VwACzgADygMGC9REWL4XLlK4GwQ']
            if txt in alph:
                for i in range(26):
                    if(txt==alph[i]):
                        bot.sendMessage(chat_id,'"'+txt+' for '+words[i]+'"')
                        bot.sendSticker(chat_id,stick[i])
            else :
                bot.sendMessage(chat_id,"Enter one alphabet only")
        elif  "flames"in txt:
            txt=txt.replace("flames","")
            txt=txt.replace(" ","");
            txt=txt.split("-")
            m1=list(txt[0])
            m2=list(txt[1])
            count=0
            for i in range(len(m1)):
                if m1[i] in m2:
                    count+=1
            val=len(m1)+len(m2)-(2*count)
            if val==0:
                bot.sendMessage(chat_id,"two names are same")
            dictionary={1:"s",2:"e",3:"f",4:"e",5:"f",6:"m",7:"e",8:"a",9:"e",10:"l",11:"m",12:"a",13:"a",14:"f",15:"m",16:"f",17:"a",18:"f",19:"l",20:"e",21:"f",22:"e",23:"f",24:"e",25:"e",26:"m"}
            flames={"f":"is friend of","l":"loves","a":"attracts by","m":"marries","e":"enemy of","s":"siblings of"}
            bot.sendMessage(chat_id,'"'+txt[0]+" "+flames[dictionary[val]]+" "+txt[1]+'"')
        elif "hi"== txt or txt=="hey" or txt=="hello":
            bot.sendMessage(chat_id,"Hi {}".format(user_name))
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhwVfn2khXXP9QkRzy3kb2RUxBGZPdAAC0wIAAvPjvguBRPfRdizrsR4E")
        elif txt=="what is ur name"or txt=="what's ur name":
            bot.sendMessage(chat_id,"I am bot. speed 1 megabyte and memory one gigabyte")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhwJfn2i65YAU5Vb5yhUOGZWRmWjLBQACIgADO3EfIvgK0glkc6XnHgQ")
        elif txt=="how r u" or txt=="r u fine":
            bot.sendMessage(chat_id,"I am fine")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBheVfnkDgyc6Th0jNrNi9IR1cZv3Y-QACQgADO2AkFLjp0so8nIjNHgQ")
            bot.sendMessage(chat_id,"what about you")
        elif "fine"in txt or "good"in txt or "nice"in txt or "not bad"in txt:
            bot.sendMessage(chat_id,"cool")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhedfnkInDLbdsmhkqkiF7EikN68iFgACcAAD9wLIDyQpDCtech2jHgQ")
        elif txt=="what r u doing" or txt=="what's up":
            hob=["playing clash of clans","playing clash royale","putting groundnut🤣 with you","watching naruto anime"]
            select=random.choice(hob)
            bot.sendMessage(chat_id,select)
        elif txt=="where r u" or txt=="where r u from":
            bot.sendMessage(chat_id,"Iam from thanjavur")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhe1fnkNyX8vFN2ZV-ylcSfLldinGVQAChAAD9wLID35NW08EzZwkHgQ")
        elif txt=="fuck"  or txt=="ass whole":
            bot.sendMessage(chat_id,"ohtha paathu pesu da")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhflfnkTX9LFh1yRMdlZrpGKuG3ejUAAC0gEAAsxUSQkhDZIKHVZCGR4E")
        elif txt=="naruto" or txt=="sauske" or txt=="sakura" or txt=="itachi" or txt=="kakashi":
            bot.sendMessage(chat_id,"are you watching naruto . its awesome")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhftfnkY1WH4zdpisIDy-N5wdSWkVMgACHgADwDZPE6FgWy2rAAHeBB4E")
        elif txt=="r u single":
            bot.sendMessage(chat_id,"currently morattu Single")
        elif "future" in txt:
            bot.sendMessage(chat_id,"Iam not a magician to predict future")
        elif txt=="i love u":
            bot.sendMessage(chat_id,"you annoying")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhglfnk6Cf6h468Z7Nbj-C0i5Lgz0CwACUQADHwFMFW0kc6gaYTdPHgQ")
        elif "love" in txt:
            bot.sendMessage(chat_id,"Iam already told you.iam not intrested in love")
        elif "dei" in txt or "oie" in txt or txt=="dude" or txt=="aprm" or txt=="oii":
            bot.sendMessage(chat_id,"sollu pa kekran")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhf1fnkpdzhb9dWL9ZIUNyI5z6HA0ngACHAADwDZPE8GCGtMs_g7hHgQ")
        elif txt=="gud mrng" or txt=="gm":
            bot.sendMessage(chat_id,"gud morning.Have a great day")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhf9fnku_olHyYsUnBxltSIQtKb8bIwACjQAD9wLIDySOeTFwpasYHgQ")
        elif txt=="gud n8" or txt=="gn" or txt=="gud nit":
            bot.sendMessage(chat_id,"okie frnd")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhgFfnkw6u8wgn9Wl_6NdxXZFcovuKQACcwAD9wLID7d5MW6uwoC5HgQ")
        elif "bye" in txt or "tata" in txt :
            bot.sendMessage(chat_id,"okie i catch u later")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhgNfnkyqf6x8MM0MurfAVqFAR2AFUgACbwAD9wLID-kz_ZsHgo4yHgQ")
        elif "enjoy" in txt or "njoy" in txt:
            bot.sendMessage(chat_id,"iam enjoying")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhAtfm5cxdYzQxv7_TpMvgPQW6BXlTwACcAADDbbSGfNwXQUmdM0XGwQ")
        elif "pannura" in txt or txt=="enna" :
            bot.sendMessage(chat_id,"i am trying to impress you")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhwxfn27kSmAn9rdRMqVmv-iiDrq6BQACCwADlp-MDpuVH3sws_a7HgQ")
        elif txt=="ha ha ha" or txt=="he he he" :
            bot.sendMessage(chat_id,"it's funny")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhnhfnrYml4nzIeXNG4hbZtplIzXbTAACYwMAAvPjvgur9KLPD5qy0B4E")
        elif "quotes"in txt or "motivation" in txt:
            mo=["“I’m not gonna run away, I never go back on my word! That’s my way.”"," “I care more about others than I do myself, and I won’t let anyone hurt them.”","“My friends were the first to accept me for who I am.”","“That’s why we endure. We are same. I will never forget.”","“If you don’t like the hand that fate’s dealt you with, fight for a new one.”","“Listen to yourself whining and complaining like some sorry little victim. You can whimper all day long for all I care, you’re nothing but a coward.”","“Failing doesn’t give you a reason to give up, as long as you believe.”","“Love breeds sacrifice, which in turn breeds hatred. Then you can know pain.”","“While you’re alive, you need a reason for your existence. Being unable to find one is the same as being dead.”","“Once you question your own belief it’s over.”"," “Hard work is worthless for those that don’t believe in themselves.”","“When you give up, your dreams and everything else they’re gone.”","“Somebody told me I’m a failure, I’ll prove them wrong.”","“The concept of hope is nothing more than giving up. A word that holds no true meaning.”","“Rejection is a part of any man’s life. If you can’t accept and move past rejection, or at least use it as writing material – you’re not a real man.”","“Those who forgive themselves, and are able to accept their true nature… They are the strong ones!” ","“It’s human nature not to realize the true value of something, unless they lose it.”","“The ones who aren’t able to acknowledge their own selves are bound to fail.”"]
            sel=random.choice(mo)
            bot.sendMessage(chat_id,sel)
        elif txt=="thanks" or txt=="thank u" or txt=="omg" or txt=="perfect":
            bot.sendMessage(chat_id,"mahizhchi")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhwhfn2s-2i6i21bCDWMQRdx9T2O_rgACGgADO3EfIiTBl60jqrHmHgQ")
        elif "idiot"in txt or "stupid"in txt or txt=="lusu" or "fool"in txt or txt=="brainless" or txt=="pakki":
            bot.sendMessage(chat_id,"why you people are like this. it's hurt\ni give my skill to you then y scolding me")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhwpfn2xeVGe9ZoCW__35OAj8pzztrAACogADFkJrCuweM-Hw5ackHgQ")
        else :
            bot.sendMessage(chat_id,"sorry i unnable to understand your text")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBhnRfnrA7YL6vRm0TpRkIGGGXV25H5gAC8wADVp29Cmob68TH-pb-HgQ")
            
bot=telepot.Bot(token)
bot.message_loop(handle)

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')
