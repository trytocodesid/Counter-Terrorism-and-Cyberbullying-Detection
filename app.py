#Importing the Libraries
import numpy as np
from flask import Flask, render_template,request,make_response
import mysql.connector
from mysql.connector import Error
from random import randint
from sklearn import compute
import json  #json request
from datetime import date
from datetime import datetime
import flask
import os
import nltk
import cv2

from werkzeug.utils import secure_filename
import glob


emails=""
#Loading Flask and assigning the model variable
app = Flask(__name__)
app=flask.Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dataloader')
def dataloader():
    return render_template('dataloader.html')

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route('/Usernotify')
def Usernotify():
    global emails
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    sql_Query = "SELECT tweetss,results,Dates FROM `tweets` where email='"+emails+"'"
    cursor.execute(sql_Query)
    print(sql_Query)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()
    return render_template('Usernotify.html',data=data)


@app.route('/breport')
def breport():
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    sql_Query = "SELECT * FROM userdata where Stat='Suspended'"
    cursor.execute(sql_Query)
    print(sql_Query)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()
    return render_template('breport.html',data=data)




@app.route('/planning')
def planning():
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    sql_Query = "SELECT userdata.Phone,userdata.Addr,tweets.Dates,tweets.tweetss,userdata.Email,tweets.results FROM userdata INNER JOIN tweets ON userdata.Email=tweets.email"
    cursor.execute(sql_Query)
    print(sql_Query)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()
    return render_template('planning.html',data=data)


@app.route('/userpage')
def userpage():
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    global emails
    sql_Quer = "SELECT userdata.Uname, tweets.tweetss FROM userdata INNER JOIN tweets ON userdata.Email=tweets.email "
    cursor.execute(sql_Quer)
    print(sql_Quer)
    data = cursor.fetchall()
    print(data)
    return render_template('userpage.html',data=data)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/loaddata')
def loaddata():
    os.system("python Download_twitter_Api.py")
    return render_template('dashboard.html')

@app.route('/preprocess')
def preprocess():
    os.system("python preprocessor.py")
    return render_template('dashboard.html')


@app.route('/store')
def store():
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    data=request.args['tweets']
    print(data)
    global emails
    print(emails)
    presentime = datetime.now()
    print("Today date is: ", presentime)
    cursor = connection.cursor()
    sql_Query = "insert into tweets(email,tweetss,Dates)  values('"+emails+"','"+data+"','"+str(presentime)+"')"
    cursor.execute(sql_Query)
    print(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    print(data)
    import pandas as pd
    from nltk.tokenize import sent_tokenize, word_tokenize
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    val=data.lower()
    print ("Input given :"+ str(val))
    


    # Tokenization
    tokens=sent_tokenize(val)
    print("Tokens are :")
    print(tokens)


    wtokens=word_tokenize(val)
    print("Word Tokens are :")
    print(wtokens)




    # Stopword removal
    common_words = open("common_words.txt", "r")

    with open("common_words.txt") as f:
      lineList = f.readlines()
      print(lineList)
      #print("------------------1")
    print(common_words)
    cwlist = [line.rstrip('\n') for line in common_words.readlines()]
    #print("------------------2")
    print(cwlist)


    stop_words = cwlist
    #print("------------------3")
    print(stop_words)



    filtered_sentence = [w for w in wtokens if not w in stop_words[0]]


    filtered_sentence = [] 
    #flag=0
    for w in wtokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    '''for w in wtokens:
        for i in range(len(stop_words)):
            if w!=stop_words[i][0]:
                flag=1
                break
        if(flag==0):
            filtered_sentence.append(w)'''
    mylst = set(filtered_sentence)
    finalized_words = list(mylst)
    #print(filtered_sentence)
    print("****************************************")
    print("Finalized Words:")
    print(finalized_words)
    dataset=["hit","kill","unhappy","suicide","depress","sad","undesirable","suicidal","negative","die","end","weltschmerz","agony","agonized","agonised","apprehension","dread","dreaded","mid life crisis","misgiving","nervousness","nervous","uneasiness","uneasy","abasement","abjection","blahs","bleakness","bummer","cheerlessness","cheerless","dejection","desolation","desolated","desperation","desperate","despondency","discouragement","discourage","dispiritedness","distress","distressed","dole","dolefulness","dolor","downheartedness","downhearted","dreariness","dullness","dull","dumps","dump","ennui","gloom","gloominess","heavyheartedness","hopelessness","hopeless","lowness","low","melancholia","melancholy","misery","miserable","mortification","qualm","sadness","sorrow","trouble","troubled","unhappiness","vapors","woefulness","worry","abjectness","blue funk","disconsolation","heaviness of heart","lugubriosity","the blues","adversity","anguish","calamity","cross","crux","difficulty","disease","disorder","distress","grief","hardship","hardships","illness","ill","infirmity","misery","misfortune","ordeal","pain","plague","plight","scourge","sickness","sick","sorrow","suffering","suffered","torment","trial","tribulation","trouble","woe","annoying","biting","caustic","cutting","galling","hard to take","hateful","hurtful","nasty","rough","rubbing the wrong way","sharp","spiky","unpleasant","abominable","alarming","appalling","atrocious","deplorable","depressing","dire","disgusting","distressing","dreadful","fearful","frightful","ghastly","grody","gross","gruesome","grungy","harrowing","hideous","horrendous","horrible","horrific","horrifying","nasty","offensive","raunchy","repulsive","shocking","stinking","synthetic","tough","ugly","unpleasant","unsightly","adverse","disagreeable","discouraged","discouraging","displeasing","distressed","gloomy","grim","melancholy","troubled","troubling","unfavorable","unfortunate","unhappy","unpleasant","atrocious","bleak","depressing","depressive","dismal","dispiriting","distressing","doleful","dreary","foreboding","funereal","gloomy","horrible","lugubrious","mournful","ominous","oppressive","sad","sinister","sombre","threatening","black","cheerless","comfortless","dark","discouraging","disheartening","dismal","drear","dreary","funereal","gloomy","grim","hard","harsh","hopeless","joyless","lonely","melancholy","mournful","oppressive","sad","somber","unpromising","black","cheerless","comfortless","dark","discouraging","disheartening","dismal","drear","dreary","funereal","gloomy","grim","hard","harsh","hopeless","joyless","lonely","melancholy","mournful","oppressive","sad","somber","unpromising","dejections","despondency","doldrums","dumps","gloom","gloominess","glumness","heavy hearts","low spirits","melancholies","moodiness","mournfulness","sadness","the dismals","the mopes","unhappiness","cold feet","dejection","depression","despair","disappointment","discomfiture","dismay","downheartedness","hopelessness","loss of confidence","low spirits","dying","quit","torture","pain","kill","killed","killer","stress","stressed","I quit","can't take it anymore","died","dead","death","deadly","suicide","hitting hard","hard hitting","failure","fail","failed","fault","faulty","despair","rude","rudeness","numb","numbness","reject","rejection","violence","hate","hatred","reject","rejection","rejected","lonely","lone","alone","dissatisfied","suicidal","negative thoughts","filthy","pity","depression ","depressed","chronic"]
    # Emotion recognizer
    emotion='Not depressed'
    for fnword in finalized_words:
        print(fnword)
        
        for i in range(len(dataset)):
                if dataset[i] in fnword:
                        emotion='Statement contains Cyberbullying words'
                        break;
    print(emotion)
    print(val)
    negations=[ " not "," don't "," won't "," no "," never "," can't "," dont "," wont "," cant "," nor "," neither "," none "," no one "," nobody "," nowhere "," not "," hardly "," scarely "," barely "," doesn't "," doesnt "," isn't "," isnt "," wasn't "," wasnt "," shouldn't "," shouldnt "," wouldn't "," couldn't "," wouldnt "," couldnt " ]
    for i in range(len(negations)):
        #print(negations[i])
        if negations[i] in val:
            if emotion=="Statement contains Cyberbullying words":
                    emotion="Anomaly Detected"
                    break
            elif emotion=="Statement does not contains Cyberbullying words":
                    emotion="Normal Tweet"
                    break
    if "not well" in val:
        if emotion=="Statement contains Cyberbullying words":
            emotion="Statement does not contains Cyberbullying words"
            
        elif emotion=="Statement does not contains Cyberbullying words":
            emotion="Statement contains Cyberbullying words"
            
        
    '''
    if " not " in val:
            if emotion=="Statement contains Depression":
                    emotion="Statement does not contains Depression"
            elif emotion=="Statement does not contains Depression":
                    emotion="Statement contains Depression"
    
    if " not " in val:
            if emotion=="Statement contains Depression":
                    emotion="Statement does not contains Depression"
            elif emotion=="Statement does not contains Depression":
                    emotion="Statement contains Depression"
    '''
    print(val +" : "+emotion)
    print("-------------------")
    print (emotion)

    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    sql_Query = "select Bullycount from userdata where Email='"+emails+"'"
    print(sql_Query)
    cursor.execute(sql_Query)
    query_op = cursor.fetchall()
    rcount = int(query_op[0][0])
    print(rcount, flush=True)
    if emotion=="Statement contains Cyberbullying words":
        rcount=rcount+1

    if rcount>=5:
        sql_Query = "update userdata set Bullycount= %s, Stat='Suspended' where Email= %s"
        cursor.execute(sql_Query)
    else:
        sql_Query = "update userdata set Bullycount="+str(rcount)+" where Email='"+emails+"'"
        cursor.execute(sql_Query)
        
    connection.commit() 
    connection.close()
    cursor.close()
    
    msg="Data saved successfully"
    resp = make_response(json.dumps(msg))
    print(msg, flush=True)
    return resp



@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    print("request :"+str(request), flush=True)
    if request.method == 'POST':
        emotion=""
        print('File')
        prod_mas = request.files['first_image']
        print(prod_mas)
        filename = secure_filename(prod_mas.filename)
        prod_mas.save(os.path.join("F:\\Upload\\", filename))

        #csv reader
        fn = os.path.join("F:\\Upload\\", filename)
        
        connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
        global emails
        print(emails)
        presentime = datetime.now()
        print("Today date is: ", presentime)
        cursor = connection.cursor()
        sql_Query = "insert into tweets(email,tweetss,Dates)  values('"+emails+"','"+filename+"','"+str(presentime)+"')"
        cursor.execute(sql_Query)
        print(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
       
        width = 400
        height = 400
        dim = (width, height)


        #cv2.imshow("org",gray)
        #cv2.waitKey()
        ci=cv2.imread(fn)
        gray= cv2.cvtColor(ci,cv2.COLOR_BGR2GRAY)
        thresh = cv2.cvtColor(ci, cv2.COLOR_BGR2HSV)
        cv2.imwrite("static/Threshold/"+filename,thresh)
        #cv2.imshow("org",thresh)
        #cv2.waitKey()

        lower_green = np.array([34, 177, 76])
        upper_green = np.array([255, 255, 255])
        hsv_img = cv2.cvtColor(ci, cv2.COLOR_BGR2HSV)
        binary = cv2.inRange(hsv_img, lower_green, upper_green)
        cv2.imwrite("static/Binary/"+filename,gray)
        #cv2.imshow("org",binary)
        #cv2.waitKey()

        gray= cv2.cvtColor(ci,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
        cv2.imwrite('thresh.jpg',thresh)
        featureval=os.stat('thresh.jpg').st_size

        print(featureval)

        val=featureval
        flist=[]
        with open('model.h5') as f:
            for line in f:
                flist.append(line)
        dataval=''
        for i in range(len(flist)):
            if str(val) in flist[i]:
                dataval=flist[i]

        dataval=dataval.replace('\n','')
        #print('------------')
        #print(dataval)
        strv=dataval.split('-')
        print(strv)
        

        if str(strv[0])!='':
            emotion="Anomaly Detected"
        else:
            emotion="Normal Tweet"
        
        print(emotion)
        

            
        connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
        cursor = connection.cursor()
        sql_Query = "select Bullycount from userdata where Email='"+emails+"'"
        print(sql_Query)
        cursor.execute(sql_Query)
        query_op = cursor.fetchall()
        print(query_op)
        rcount = int(query_op[0][0])
        print(rcount, flush=True)
        if emotion=="Anomaly Detected":
            rcount=rcount+1

        if rcount>=5:
            sql_Query = "update userdata set Bullycount="+str(rcount)+",Stat='Suspended' where Email='"+emails+"'"
            cursor.execute(sql_Query)
        else:
            sql_Query = "update userdata set Bullycount="+str(rcount)+" where Email='"+emails+"'"
            cursor.execute(sql_Query)
            
        connection.commit() 
        connection.close()
        cursor.close()
    
        msg=emotion
        resp = make_response(json.dumps(msg))
        return resp


@app.route('/analyze')
def analyzenew():
    data=request.args['data']
    print(data)
    import pandas as pd
    from nltk.tokenize import sent_tokenize, word_tokenize
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    val=data.lower()
    print ("Input given :"+ str(val))
    


    # Tokenization
    tokens=sent_tokenize(val)
    print("Tokens are :")
    print(tokens)


    wtokens=word_tokenize(val)
    print("Word Tokens are :")
    print(wtokens)




    # Stopword removal
    common_words = open("common_words.txt", "r")

    with open("common_words.txt") as f:
      lineList = f.readlines()
      print(lineList)
      #print("------------------1")
    print(common_words)
    cwlist = [line.rstrip('\n') for line in common_words.readlines()]
    #print("------------------2")
    print(cwlist)


    stop_words = cwlist
    #print("------------------3")
    print(stop_words)



    filtered_sentence = [w for w in wtokens if not w in stop_words[0]]


    filtered_sentence = [] 
    #flag=0
    for w in wtokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    '''for w in wtokens:
        for i in range(len(stop_words)):
            if w!=stop_words[i][0]:
                flag=1
                break
        if(flag==0):
            filtered_sentence.append(w)'''
    mylst = set(filtered_sentence)
    finalized_words = list(mylst)
    #print(filtered_sentence)
    print("****************************************")
    print("Finalized Words:")
    print(finalized_words)
    dataset=["hit","kill","unhappy","bomb","terrorist","tower","poison","suicide","depress","sad","undesirable","suicidal","negative","die","end","weltschmerz","agony","agonized","agonised","apprehension","dread","dreaded","mid life crisis","misgiving","nervousness","nervous","uneasiness","uneasy","abasement","abjection","blahs","bleakness","bummer","cheerlessness","cheerless","dejection","desolation","desolated","desperation","desperate","despondency","discouragement","discourage","dispiritedness","distress","distressed","dole","dolefulness","dolor","downheartedness","downhearted","dreariness","dullness","dull","dumps","dump","ennui","gloom","gloominess","heavyheartedness","hopelessness","hopeless","lowness","low","melancholia","melancholy","misery","miserable","mortification","qualm","sadness","sorrow","trouble","troubled","unhappiness","vapors","woefulness","worry","abjectness","blue funk","disconsolation","heaviness of heart","lugubriosity","the blues","adversity","anguish","calamity","cross","crux","difficulty","disease","disorder","distress","grief","hardship","hardships","illness","ill","infirmity","misery","misfortune","ordeal","pain","plague","plight","scourge","sickness","sick","sorrow","suffering","suffered","torment","trial","tribulation","trouble","woe","annoying","biting","caustic","cutting","galling","hard to take","hateful","hurtful","nasty","rough","rubbing the wrong way","sharp","spiky","unpleasant","abominable","alarming","appalling","atrocious","deplorable","depressing","dire","disgusting","distressing","dreadful","fearful","frightful","ghastly","grody","gross","gruesome","grungy","harrowing","hideous","horrendous","horrible","horrific","horrifying","nasty","offensive","raunchy","repulsive","shocking","stinking","synthetic","tough","ugly","unpleasant","unsightly","adverse","disagreeable","discouraged","discouraging","displeasing","distressed","gloomy","grim","melancholy","troubled","troubling","unfavorable","unfortunate","unhappy","unpleasant","atrocious","bleak","depressing","depressive","dismal","dispiriting","distressing","doleful","dreary","foreboding","funereal","gloomy","horrible","lugubrious","mournful","ominous","oppressive","sad","sinister","sombre","threatening","black","cheerless","comfortless","dark","discouraging","disheartening","dismal","drear","dreary","funereal","gloomy","grim","hard","harsh","hopeless","joyless","lonely","melancholy","mournful","oppressive","sad","somber","unpromising","black","cheerless","comfortless","dark","discouraging","disheartening","dismal","drear","dreary","funereal","gloomy","grim","hard","harsh","hopeless","joyless","lonely","melancholy","mournful","oppressive","sad","somber","unpromising","dejections","despondency","doldrums","dumps","gloom","gloominess","glumness","heavy hearts","low spirits","melancholies","moodiness","mournfulness","sadness","the dismals","the mopes","unhappiness","cold feet","dejection","depression","despair","disappointment","discomfiture","dismay","downheartedness","hopelessness","loss of confidence","low spirits","dying","quit","torture","pain","kill","killed","killer","stress","stressed","I quit","can't take it anymore","died","dead","death","deadly","suicide","hitting hard","hard hitting","failure","fail","failed","fault","faulty","despair","rude","rudeness","numb","numbness","reject","rejection","violence","hate","hatred","reject","rejection","rejected","lonely","lone","alone","dissatisfied","suicidal","negative thoughts","filthy","pity","depression ","depressed","chronic"]
    # Emotion recognizer
    emotion='Not depressed'
    for fnword in finalized_words:
        print(fnword)
        
        for i in range(len(dataset)):
                if dataset[i] in fnword:
                        emotion='Statement contains Cyberbullying words'
                        break;
    print(emotion)
    print(val)
    negations=[ " not "," don't "," won't "," no "," never "," can't "," dont "," wont "," cant "," nor "," neither "," none "," no one "," nobody "," nowhere "," not "," hardly "," scarely "," barely "," doesn't "," doesnt "," isn't "," isnt "," wasn't "," wasnt "," shouldn't "," shouldnt "," wouldn't "," couldn't "," wouldnt "," couldnt " ]
    for i in range(len(negations)):
        #print(negations[i])
        if negations[i] in val:
            if emotion=="Statement contains Cyberbullying words":
                    emotion="Anomaly Detected"
                    break
            elif emotion=="Statement does not contains Cyberbullying words":
                    emotion="Normal Tweet"
                    break
    if "not well" in val:
        if emotion=="Statement contains Cyberbullying words":
            emotion="Statement does not contains Cyberbullying words"
            
        elif emotion=="Statement does not contains Cyberbullying words":
            emotion="Statement contains Cyberbullying words"
            
        
    '''
    if " not " in val:
            if emotion=="Statement contains Depression":
                    emotion="Statement does not contains Depression"
            elif emotion=="Statement does not contains Depression":
                    emotion="Statement contains Depression"
    
    if " not " in val:
            if emotion=="Statement contains Depression":
                    emotion="Statement does not contains Depression"
            elif emotion=="Statement does not contains Depression":
                    emotion="Statement contains Depression"
    '''
    print(val +" : "+emotion)
    print("-------------------")
    print (emotion)
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    cursor = connection.cursor()
    sql_Query = "UPDATE tweets SET results = '"+emotion+"'  WHERE  tweetss= '"+val+"';"
    cursor.execute(sql_Query)
    print(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    nb=compute.NBAccuracy()
    dt=compute.DTAccuracy()
    knn=compute.KNNAccuracy()
    svm=compute.SvmAccuracy()
    rf=compute.RFAccuracy()
    return render_template('dashboard.html',pred=emotion,nb=nb,dt=dt,knn=knn,svm=svm,rf=rf)

@app.route('/board')
def emotion_detection():
    os.system('python depression_sentiment_analysis.py')
    return render_template('dashboard.html')


""" REGISTER CODE  """

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    connection = mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    uname = request.args['uname']
    name = request.args['name']
    pswd = request.args['pswd']
    email = request.args['email']
    phone = request.args['phone']
    addr = request.args['addr']
    value = randint(123, 99999)
    uid="User"+str(value)
    print(addr)
        
    cursor = connection.cursor()
    sql_Query = "insert into userdata(Uid,Uname,Name,Pswd,Email,Phone,Addr,Bullycount,Stat) values('"+uid+"','"+uname+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"',0,'Active')"
        
    cursor.execute(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data saved successfully"
    #msg = json.dumps(msg)
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp




"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    import datetime
        
    connection=mysql.connector.connect(host='localhost',database='flaskfndb',user='root',password='')
    global emails
    lgemail=request.args['email']
    emails=lgemail
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    cursor = connection.cursor()
    sq_query="select count(*) from userdata where Email='"+lgemail+"' and Pswd='"+lgpssword+"' and Stat='Active'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp


   


    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
