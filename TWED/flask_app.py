from flask import Flask, request

from processing_encryption import do_calculation
from processing_decryption import do_decryption

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def home_page():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>TWED</title>
  </head>
  <body>
<br><br><br><br><br>

    <a href="/encryption"><button type="button" class="btn btn-primary btn-lg btn-block"><i class="fas fa-lock"></i>&nbsp;&nbsp;&nbsp;&nbsp;Encryption</button></a><br><br>
<a href="/decryption"><button type="button" class="btn btn-secondary btn-lg btn-block"><i class="fas fa-lock-open"></i>&nbsp;&nbsp;&nbsp;&nbsp;Decryption</button></a>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
 `  <script src="https://kit.fontawesome.com/5de545e21a.js" crossorigin="anonymous"></script>
  </body>
</html>

'''.format()


#####################################################################################

@app.route("/encryption", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = (request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = int(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return '''
            <html>
<head>
  <meta charset="UTF-8">
  <title>TWED Encryption</title>
  <link rel="stylesheet" href="/static/css/hell.css">
  <link rel="stylesheet" href="/static/css/copytooltip.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<!-- partial:index.partial.html -->
<div class="wrapper">
	<div class="container">
		<h1>Here's Your Encrypted String</h1>

		<form class="form">
			<input type="text" value="{result}" id="myInput" READONLY>
			<br/>
			<br/>
			<br/>
			<br/>
			<br/>
			<br/>
			<div class="tooltip">
                <button onclick="myFunction()" onmouseout="outFunc()">
                <span class="tooltiptext" id="myTooltip">Copy to clipboard</span>
                COPY
                </button>
            </div>
            <br/>
            <br/>

		</form>

	</div>



	<ul class="bg-bubbles">
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>

</div>
<!-- partial -->
<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script  src="/static/javascript/widgets.js"></script>
<script  src="/static/javascript/copycat.js"></script>

</body>
</html>


            '''.format(result=result)

    return '''
    <!DOCTYPE html>
    <html lang="en" >
    <head>
        <meta charset="UTF-8">
        <title>TWED Encryption</title>
        <link rel="stylesheet" href="/static/css/hell.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        {errors}
        <!-- partial:index.partial.html -->
        <div class="wrapper">
	        <div class="container">
		        <h1>Encryption</h1>

		        <form class="form" method="post" action="./encryption">
			        <textarea name="number1" placeholder="String" rows="4" cols="50"></textarea>
			        <input name="number2" type="password" placeholder="Password">
			        <button type="submit" id="login-button">Encrypt</button>
		        </form>
	        </div>

        	<ul class="bg-bubbles">
		        <li></li>
		        <li></li>
	        	<li></li>
		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>

		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>
		        <li></li>
        	</ul>
        </div>



        <!-- partial -->
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script  src="/static/javascript/widgets.js"></script>

</body>
</html>

    '''.format(errors=errors)


#############################################################################

@app.route("/decryption", methods=["GET", "POST"])
def decryption_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = (request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</font></p>\n".format(request.form["number1"])
        try:
            number2 = int(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.The Password Must Be a Number</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_decryption(number1, number2)
            return '''
               <!-- <html>
                    <body background="https://1.bp.blogspot.com/-OOIYu-25fvg/XXc-_JYqSCI/AAAAAAAABEM/hf_QV4eYRHw2Wd5ixENawrwRyGcsatI0ACLcBGAs/s1600/web-design-2906159.jpg">
                        <center>
                        <p><h3><font color="white">The result is</h3><br/><h1> {result}</h1></font></p>
                        <p><a href="/"><font color="white">Click here to calculate again</font></a>
                        </center>
                    </body>
                </html> -->
                <html>
<head>
  <meta charset="UTF-8">
  <title>TWED Decryption</title>
  <link rel="stylesheet" href="/static/css/hell.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<!-- partial:index.partial.html -->
<div class="wrapper">
	<div class="container">
		<h1>Here's Your Decrypted String</h1>

		<form class="form">
			<input type="text" value="{result}" id="myInput">
			<button id="login-button" onclick="myFunction()">COPY</button>
		</form>
	</div>

	<ul class="bg-bubbles">
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>
<!-- partial -->
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script  src="/static/javascript/widgets.js"></script>
<script  src="/static/javascript/afterencrypt.js"></script>

</body>
</html>


            '''.format(result=result)

    return '''
        <!-- <html>
            <body background="https://1.bp.blogspot.com/-OOIYu-25fvg/XXc-_JYqSCI/AAAAAAAABEM/hf_QV4eYRHw2Wd5ixENawrwRyGcsatI0ACLcBGAs/s1600/web-design-2906159.jpg">
            <center>
                {errors}
                <br/>
                <br/><br/>
                <br/><br/>
                <br/><br/>
                <br/>
                <p><h1><font color="white" face="arial">Enter your Encrypted String And Password:</font></p>
                <form method="post" action=".">
                    <p><textarea name="number1" rows="4" cols="50" placeholder="Text"></textarea></p>
                    <p><input name="number2" type="password" placeholder="Password"/></p>
                    <p><input type="submit" value="Decrypt" /></p>
                </form>
                </h1>
            </center>
            </body>
        </html> -->

        <!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>TWED Decryption</title>
  <link rel="stylesheet" href="/static/css/hell.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
{errors}
<!-- partial:index.partial.html -->
<div class="wrapper">
	<div class="container">
		<h1>Decryption</h1>

		<form class="form" method="post" action="./decryption">
			<textarea name="number1" placeholder="String" rows="4" cols="50"></textarea>
			<input name="number2" type="password" placeholder="Password">
			<button type="submit" id="login-button">Decrypt</button>
		</form>
	</div>

	<ul class="bg-bubbles">
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>
<!-- partial -->
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script  src="/static/javascript/widgets.js"></script>

</body>
</html>

    '''.format(errors=errors)