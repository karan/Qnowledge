![](https://raw.github.com/karan/Qnowledge/master/logo.png)

**Release status: Pre-Alpha**

Knowledge API for Quora.

Provides access to various details of the passed question:

- Question:
    - Title
    - Details
    - Topics
- Answers (Upto 6 top answer):
    - Author
    - Votes
    - Rank
    - Answer body

### Start

    $ pip install -r requirements.txt   # install dependencies
    $ python app.py                     # start the api

### Deploy to Heroku

    $ pip install -r requirements.txt   # install dependencies
    $ heroku create
    $ heroku addons:add newrelic
    $ (git add, git commit)
    $ git push heroku master

### Usage

**Base URL:** [http://q.goel.im](http://q.goel.im)

**Output:** JSON

### Get the question details

#### `GET /url=<url>`

Example:

`http://localhost:5000/url=https://www.quora.com/Google/What-are-the-changes-made-to-the-host-matching-phase-for-Google-Summer-Internships-from-2013-to-2014`

Output:

TODO

Donations
=============

If Qnowledge has helped you in any way, and you'd like to help the developer, please consider donating.

**- BTC: [19dLDL4ax7xRmMiGDAbkizh6WA6Yei2zP5](http://i.imgur.com/bAQgKLN.png)**

**- Flattr: [https://flattr.com/profile/thekarangoel](https://flattr.com/profile/thekarangoel)**


Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
