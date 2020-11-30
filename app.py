import numpy
import torch
from flask import Flask,request,jsonify,render_template
from enc_dec import Transliteration_EncoderDecoder_Attention

app = Flask(__name__)
model = torch.load(open('./model.pt', 'rb'), map_location = torch.device('cpu'))
model.eval()


@app.route('/')
def home():
	return render_template("home.html", prediction_text = '')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
    	name = request.form['fname']
        #print(name)            
    	prediction = model.infer(name,model)
    	return render_template('home.html', prediction_text = 'Hindi word be {}'.format(prediction))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.infer(data.upper(),model)

    return jsonify(prediction)
    
if __name__ == "__main__":
	app.run(port = 5000)