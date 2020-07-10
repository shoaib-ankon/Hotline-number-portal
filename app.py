# importing libraries 
from flask import Flask,render_template, request 
from flask_mail import Mail, Message 

app = Flask(__name__) 
mail = Mail(app)

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 




@app.route("/") 
def index():
	return render_template('mail.html') 
	


@app.route("/submit", methods=['post']) 
def submitting():
	shift = request.form.get('shift')
	isem3 = request.form.get('isem3')
	csm7 = request.form.get('csm7')
	csm8 = request.form.get('csm8')
	rnbm1 = request.form.get('rnbm1')
	rnbm5 = request.form.get('rnbm5')
	rnbm9 = request.form.get('rnbm9')
	cmpm = request.form.get('cmpm')
	total = "Dear Liton Bhai,"+"\n"+"Please forward these hotlines to respective numbers."+"\n"+"Shift - "+shift+"\n"+"\n"+"#58003- "+isem3+"\n"+"\n"+"#58007- "+csm7+"\n"+"#58008- "+csm8+"\n"+"\n"+"#58001- "+rnbm1+"\n"+"#58005- "+rnbm5+"\n"+"#58009- "+rnbm9+"\n"+"\n"+cmpm+"\n"+"\n"+"\n"+"Best Regards,"+"\n"+"ISEM Team"
	msg = Message( 
				'SOC hotline divert for home office', 
				sender ='', 
				recipients = ['']
				) 
	msg.body = total
	mail.send(msg) 
	return 'Thank You. Mail has been sent.'	
	

if __name__ == '__main__': 
	app.run(debug = True)
