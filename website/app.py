from flask import Flask,render_template,request
import pickle



app= Flask(__name__)

def prediction(list):
    filename = "model/liver_disease_predictor.pickle"
    with open(filename, "rb") as file:
         model = pickle.load(file)
    pred_value = model.predict([list])
    return pred_value    


@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/',methods=["POST","GET"])
def index():
   # render_template("index.html")
    if request.method == "POST":
         Age= request.form["age"]
         gender= request.form["gender"]
         bmi=request.form["BMI"]
         alc=request.form["alco"]
         smoking=request.form["Smoking"]
         gen=request.form["gentic"]
         dia=request.form["diabetes"]
         hyper=request.form["hy"]
         liver=request.form["liv"]
        
         #print(Age,gender,bmi,alc,smoking,gen,dia,hyper,liver)
         feartur_list= []
         feartur_list.append(int(Age))
         feartur_list.append(int(gender))
         feartur_list.append(float(bmi))
         feartur_list.append(float(alc))
         feartur_list.append(int(smoking))
         feartur_list.append(int(gen))
         feartur_list.append(int(dia))
         feartur_list.append(int(hyper))
         feartur_list.append(float(liver))

         #print(feartur_list)

         pred=prediction(feartur_list)
         
        # render_template("index.html")

         if pred == 0:
            return render_template("no.html")
         else:
            return render_template("yes.html") 
         
    return render_template("index.html")

    
    
          


if __name__ =="__main__":
     app.run(debug=True)
