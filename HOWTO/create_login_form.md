<h1>Steps to create forms (login) and button</h1>
<h2>Step 1:</h2>
<p>- Create config file and add a security code for REQUIRED CSRF security protocol for the all the forms</p>
<p>New file will be name "app.config" and place in package app. This config file is environment config file.</p>
<p>/app/app.config</p>
<pre>
app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my secret key"
</pre>
<h2>Step 2:</h2>
<p>Create a python config file that will read the config variable from server environment</p>
<p>/app/config.py</p>
<pre>
import os
class Config(object):#inherit characteristics from Object object
    #attribute of Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this is my secret key" #if reading from environment fail then will get the phrase after or keyword
</pre>

