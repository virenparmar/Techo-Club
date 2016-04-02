from flask import *

app = Flask(__name__)

'''@app.route('/')
def layout():
	return render_template('layout.html')
'''
@app.route('/')
def home():
	return render_template('Home.html')

@app.route('/about/')
def about():
	return render_template('About.html')

@app.route('/team/')
def team():
	return render_template('Team.html')

@app.route('/activities/')
def activities():
	return render_template('Activities.html')

@app.route('/blogs/')
def blogs():
	return render_template('Blogs.html')

@app.route('/pythonblogs/')
def python():
	return render_template('python.html')

@app.route('/contact')
def contact():
	return render_template('Contact.html')

if __name__ == '__main__':
	app.run(debug=True)