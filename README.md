<h1>Software Engineering Project II</h1>
<h2>Group 31: <i>Determine smoker status for risk assessment using publicly available data</i>
</h2>
<h6>Tested on Python version 3.11.9</h6>
<h3>Prerequisites</h3>
<h6>To run the program, you need to install NPM and Flask.
Download NPM here : https://nodejs.org/en/download
</h6>
<h6>
To download all the dependencies:
<pre>pip install -r ./backend/requirements.txt</pre>

</h6>

<h3>Running the program</h3>
<h4>Frontend:</h4>
<h6>Go into the frontend folder by </h6>
<pre>cd  .\frontend\my-app\ </pre>
<h6>Then start the frontend server by running:</h6>
<pre>npm start</pre>

<h4>Backend:</h4>
<h6>Go into the frontend folder by </h6>
<pre>cd  .\backend </pre>
<h6>Then start the backend server by running:</h6>
<pre>python server.py</pre>
<h4>Sometimes the server is booting up slow, if it takes an awful lot  of time, try to kill the run with ctrl-c and then run the command again</h4>
<h4>If you are running it locally, allow invalid certificates from localhost. If you are using Chrome, then go to chrome://flags/ then search for localhost.
There should be a line like "Allow invalid certificates for resources loaded from localhost.", then enable it. Similary on edge, just type this to the searchbar: edge://flags/#allow-insecure-localhost and then enable it.
</h4>
<h3>Using the app</h3>
<h4>You have to log in to the account first, before logging through the account itself from our page to accept the scanning. (Instgram api made us to do this way)</h4>
<h4>Only those account works which are added as testers</h4>
<h4>For demonstration purposes only, we created two instagram accounts (you can upload images and comments, if you would like to test your own pictures out with it)<h4>
<h4>username: @group31nonsmoker and @sweng31smoker password is GetPranked123! for both</h4>
<h4>Once you are logged in to one these account, you can go back to our page, and click on the login to Instagram button, which would redirect to instagram, and would have a pop up notification, where if you want to be scanned, you would have to click on accept</h4>
<h4>Then enter your name, and click on analyze, if everything works well, the report should be available in pictures*2 seconds time</h4>


