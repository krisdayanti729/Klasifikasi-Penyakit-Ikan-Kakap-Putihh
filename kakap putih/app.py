from flask import Flask, render_template, request
import numpy 
import joblib
app = Flask(__name__)


modelnb = joblib.load('model/kakap.pkl')

def prediksi_penyakit(Gejala):
	hasil_prediksi = modelnb.predict(Gejala)[0]
	if hasil_prediksi == 1:
		hasil_prediksi = "Trichodiniasis"
	elif hasil_prediksi == 2:
		hasil_prediksi = "Cryptoccaryon Irritans"
	elif hasil_prediksi == 3:
		hasil_prediksi = "Diplectanum"
	elif hasil_prediksi == 4:
		hasil_prediksi = "Vibrio"
	elif hasil_prediksi == 5:
		hasil_prediksi = "Streptococcus"
	elif hasil_prediksi == 6:
		hasil_prediksi = "Flexibacter Maritimus"
	elif hasil_prediksi == 7:
		hasil_prediksi = "VNN"        
	return hasil_prediksi


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=["GET","POST"]) # function untuk menarik data dari html
def tarik_data():
	if request.method == 'POST':
		Gejala = []
		Gejala.append(int(request.form['G001']))
		Gejala.append(int(request.form['G002']))
		Gejala.append(int(request.form['G003']))
		Gejala.append(int(request.form['G004']))
		Gejala.append(int(request.form['G005']))
		Gejala.append(int(request.form['G006']))
		Gejala.append(int(request.form['G007']))
		Gejala.append(int(request.form['G008']))
		Gejala.append(int(request.form['G009']))
		Gejala.append(int(request.form['G010']))
		Gejala.append(int(request.form['G011']))
		Gejala.append(int(request.form['G012']))
		Gejala.append(int(request.form['G013']))
		Gejala.append(int(request.form['G014']))
		Gejala.append(int(request.form['G015']))
		Gejala.append(int(request.form['G016']))
		Gejala.append(int(request.form['G017']))
		Gejala.append(int(request.form['G018']))
		Gejala.append(int(request.form['G019']))
		Gejala.append(int(request.form['G020']))
		Gejala.append(int(request.form['G021']))
		Gejala.append(int(request.form['G022']))
		Gejala.append(int(request.form['G023']))
		Gejala.append(int(request.form['G024']))
		Gejala = [Gejala]
		
		hasil_prediksi = prediksi_penyakit(Gejala)
		print(hasil_prediksi)
		return render_template('index.html', prediksi_penyakit=hasil_prediksi)
	else:
		return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0")