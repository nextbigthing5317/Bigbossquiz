from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, Response, request, redirect, url_for,jsonify     
from firebase import firebase
import random
import jwt
import pyrebase
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle

model = pickle.load(open('model.pkl','rb'))

firebaseConfig = {
  apiKey: "AIzaSyDD7zfvx2SjdfDESN9SMapLQXYIuf2YIX4",
  authDomain: "big-boss-e0cb7.firebaseapp.com",
  "databaseURL": "https://big-boss-e0cb7-default-rtdb.firebaseio.com/",
  projectId: "big-boss-e0cb7",
  storageBucket: "big-boss-e0cb7.appspot.com",
  messagingSenderId: "786301332598",
  appId: "1:786301332598:web:4ee4d6d09600b7c9c30357",
  measurementId: "G-0SBHH1LEVF"
};

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sitemap.xml")
def sitemap():
  return render_template("sitemap.xml")

def contestants(output):

    Dict = {1 : ["Oviya","Riythvika","Mugen","Losliya","Aari","Tharshan","Raju","Ciby"], 2 : 
    ["Gayathri","Mahat","Vanitha","Archana","Niroop","Snehan","Aishwarya","Suresh","Abishek"], 3 :
    ["Ramya NSK","Sandy","Gabriella","Velmurugan","Aajeedh","Isaivani","Chinnaponnu","Iykki","Imman"], 4 :
    ["Juliana","Sakthi","Madhumitha","Meera","Anitha","Vaishnavi","Ganja","Suja","Thamarai"], 5 :
    ["Aarav","Sanam","Ramya","Balaji Murugadoss","Rio","Priyanka","Varun","Shariq"], 6 :
    ["Anuya","Nadia","Ananth","Mamathi","Nithya","Mohan","Fathima","Suchitra","Vaiyapuri"], 7 :
    ["Ganesh","Balaji","Ponnambalam","Cheran","Saravanan","Ramesh","Abhinay","Mathumitha"], 8 :
    ["Namitha","Vijayalakshmi","Yashika","Mumtaj","Sherin","Sakshi","Kasthuri","Abhirami","Rekha"], 9 :
    ["Harish","Bindu","Raiza","Janani","Kavin","Shivani","Samyuktha","Akshara","Pavani"], 10 :
    ["Harathi","Som","Suruthi","Bharani","Reshma","Sendrayan","Daniel","Kaajal","Nisha"]}

    r = Dict[output]
    return random.choice(r)

@app.route("/refresh/", methods=["GET","POST"])
def refresh():
    if request.method == "POST":
      return home()

@app.route("/people/", methods=["GET","POST"])
def people():
    if request.method == "POST":
        Q1 = int(request.form['q1'])
        Q2 = int(request.form['q2'])
        Q3 = int(request.form['q3'])
        Q4 = int(request.form['q4'])
        Q5 = int(request.form['q5'])
        Q6 = int(request.form['q6'])        
        Q7 = int(request.form['q7']) 
        Q8 = int(request.form['q8']) 
        Q9 = int(request.form['q9'])
        Q10 = int(request.form['q10'])        
        Q11 = int(request.form['q11']) 
        
        name = str(request.form['name'])
        
        arr = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11]; 
        result = contestants(model.predict([arr])[0])
       
        
        firebase = pyrebase.initialize_app(firebaseConfig)
        db=firebase.database()
        data=db.child(result).get()
        text=data.val()[0]
        img=data.val()[1]
        des=data.val()[2]
    
    return render_template('result.html',text = text,image=img,desc=des,name=name)


@app.route("/redirecting")
def redirecting():
    return render_template("index.html")

#if __name__ == "__main__":
    
#    firebase = firebase.FirebaseApplication("https://tamilnews-28a69-default-rtdb.firebaseio.com/",None)
 #   app.run(debug=True)
  #  print("running")

if __name__ == "__main__":
    app.run(debug=True)
