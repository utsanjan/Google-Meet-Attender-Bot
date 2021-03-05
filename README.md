<h1 align="center">
<br>
<a href="https://github.com/utsanjan/Google-Meet-Attender-Bot/">
<img src="https://1.bp.blogspot.com/-NqnlL1QuTYQ/YEGq56HRwNI/AAAAAAAAbfs/BIhrxvNTeCE175RyGZm-DaK1s28nlupkACLcBGAsYHQ/w200-h200/imageonline-co-hueshifted.png"
alt="Google Meet Attender Bot">
</a><br>
Google Meet Attender Bot
<br>
</h1>
<p align="center">This BOT will attend your online
<br>Google Meet classes on behalf of you.
<br>No need of taking any extra stress
<br>for your online meetings.</p>

## About the Project

Chromedriver v87 has been used here.
<br>If your chrome version is not 87 then download it from [here.](https://chromedriver.chromium.org/downloads)
<br>Download it in accordance with your Chrome Browser Version.
<br>Delete `chromedriver.exe` before pushing it to heroku. (!important)

## Cloning this Repository

If git is not installed then install git from here:
<br>[Click here to Download Git](https://git-scm.com/downloads)

<br>Then run this command given below:

```sh
$ git clone https://github.com/Ryuk-me/Google-Meet-Attender-LNMEE

```

## Installation for localhost

Make sure your have `python3` and `chrome browser` installed.</br>
```sh
$ pip install -r requirements.txt
```

<i>Now run command to get Cookies</i>

```sh
python get_cookies.py
```

<i> To start BOT</i> Only use this command if you intend to use it on localhost.
```sh
python main.py
```

## Find the meeting code

```sh
https://meet.google.com/abc-defg-hij
abc-defg-hij <-- it is your meeting code.
```

## Change your meeting code

```sh
1. Download any code editor i prefer vscode.
2. Open main.py with vscode or any other editor or you can use notepad.
3. Go to line 69 and replace meet code with your meet code and save.
```


## Set your Name and Roll to send it to Chat

```bash
Go to line 75
full_name_with_roll = "Utsanjan Maity CSE/18/27"
now repalce `Utsanjan Maity CSE/18/27` with your name and roll.
```


# Deploy it on Heroku

> Why do we need it to deploy on heroku ?

* If we run it on localhost we have to always manually start it.
<br>  (And if we do that then why we should call it a BOT)

* It will consume our cpu usage, data usage and our time.
* Heroku provides free server hosting and 500hrs monthly
<br>  usage which will be more than enough for us.


## Deployment Steps

```
0. Clone the repo.
1. Install requirements `$ pip install -r requirements.txt`.
2. Run command `$ python get_cookies.py` and login to your google account.
3. Now set your meet code and your name and roll. 
5. go to heroku and create a new app and enter a unique name for your app.
6. Choose region united states.
7. Now go to settings.
8. Click on add buildpack and add the following one by one and save changes.
  $ python
  $ https://github.com/heroku/heroku-buildpack-google-chrome
  $ https://github.com/heroku/heroku-buildpack-chromedriver

9. Click on reveal configs vars

10. Add following vars one by one

    KEY                       VALUES
    CHROMEDRIVER_PATH         /app/.chromedriver/bin/chromedriver
    GOOGLE_CHROME_BIN         /app/.apt/usr/bin/google-chrome
    TZ                        Asia/Kolkata

11. Now go to Deploy Option Heroku.
12. Install heroku CLI and enter following commands one by one. 
    https://devcenter.heroku.com/articles/heroku-cli#download-and-install <-- Heroku CLI

    $ git checkout -b master
    $ heroku login
13. Open command prompt or any terminal in your current directory where all files are located.
    $ git init
    $ heroku git:remote -a your-app-name
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master

14. Then go to resource option and turn on the bot.

```

#### If you havent created account on Heroku create one from [here.](https://signup.heroku.com/)

## Tips
```sh
Turn off BOT after class is completed / when you are awake.(to save heroku dyno hours).

Turn on BOT Before Sleeping so it can attend your class while your are asleep.

If you have turned off BOT after class is completed then only turn it on after 12PM.
(If you turn on it before 12PM it will again start your meeting so be careful.) 
```


## Important Notes

```sh

Do some changes in the python file if required. 
It should then work for you as well.

Turn Off two step verification if enabled in your gmail account.

Dont use your primary gmail account.

First run get_cookie.py and get your gmail account cookies. ( NECESSARY i repeat it is NECESSARY )

Dont share these cookies with anyone.

```


## Disclaimer

<i>This <strong>BOT</strong> is created for educational purposes only.</br></i>
<i>The usage of this <strong>BOT</strong> is at the own risk of the User.</br></i>
<i>The Creator shall not be held responsible for any  misconduct on your behalf.</br></i>
<i>If by any chance your google account gets <strong>banned</strong> or <strong>suspended</strong> the creator shall not be accountable.</br></i>
<i>You are <strong>agreeing</strong> to all these <strong>conditions</strong> before downloading / cloning / forking this <strong>repository<strong>.</i>

#### <i>“Education is the most powerful weapon which you can use to change the world.”</i><strong> ― Nelson Mandela</strong></br>
<i> Attend all classes <strong>sincerely</i>.</br></br>

## Contact me  

For Queries: [My Instagram Profile](https://www.instagram.com/utsanjan/)  
[Check Out My YouTube Channel](https://www.youtube.com/DopeSatan)
