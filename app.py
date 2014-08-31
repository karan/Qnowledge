import re

from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests
from purl import URL

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/url=<path:q_link>')
def get_answers(q_link):
    url = URL(q_link)
    if url.domain() not in ['quora.com', 'www.quora.com']:
        return 'error, not quora'

    url = URL(
        scheme='https',
        host='www.quora.com',
        path=url.path(),
        query='share=1').as_string()

    soup = BeautifulSoup(requests.get(url).text)

    question = {}
    question['url'] = url
    question['title'] = soup.find("div", {"class": "question_text_edit"}).text
    question['topics'] = [topic.text for topic in soup.find_all("span", {"class": "TopicName"})]
    question['details'] = soup.find("div", {"class": "question_details_text"}).text

    answers = []

    divs = soup.find_all("div", {"class": "pagedlist_item"})
    
    try:
        ans_count = soup.find("div", {"class": "answer_count"}).text.strip()
        count = int(re.match(r'(\d+) Answers', ans_count).groups()[0])
    except:
        return jsonify(question=question, answers=answers)

    question['answer_count'] = count

    count = len(divs) - 1 if count < 6 else 6
    for i in range(count):
        one_answer = {
            'votes': '-1',
            'rank': 0,
            'answer': ''
        }
        author = {
            'name': 'Anonymous'
        }
        try:
            author['name'] = divs[i].find("div", {"class": "author_info"}).find("span", {"class": "feed_item_answer_user"}).find("a", {"class": "user"}).string
            author['bio'] = divs[i].find("div", {"class": "author_info"}).find("span", {"class": "feed_item_answer_user"}).find_all("span", {"class": "rep"})[1].find("span", {"class": "hidden"}).text
        except:
            author['bio'] = ''
        one_answer['author'] = author

        one_answer['votes'] = divs[i].find("span", {"class":"count"}).text

        html_block = divs[i].find("div", {"id": re.compile("(.*)_container")}).contents
        answer_html = ''

        return jsonify(question=question, answers=answers, one_answer=one_answer, html_block=html_block)

        for p in range(len(html_block) - 1):
            answer_html += str(html_block[p])
        one_answer['answer_html'] = answer_html
        one_answer['answer'] = divs[i].find("div", {"class": "answer_content"}).text
        one_answer['rank'] = i + 1
        answers.append(one_answer)

    return jsonify(question=question, answers=answers)

@app.route('/search=<path:s_link>')
def get_questions(s_link):
    url = URL(s_link)
    if url.domain() not in ['quora.com', 'www.quora.com']:
        return 'error, not quora'

    url = URL(
        scheme='https',
        host='www.quora.com',
        path=url.path(),
        query='share=1').as_string()

    soup = BeautifulSoup(requests.get(url).text)

    question = {}
    question['url'] = url
    question['title'] = soup.find("div", {"class": "question_text_edit"}).text
    question['topics'] = [topic.text for topic in soup.find_all("span", {"class": "TopicName"})]
    question['details'] = soup.find("div", {"class": "question_details_text"}).text

    answers = []

    divs = soup.find_all("div", {"class": "pagedlist_item"})
    
    try:
        ans_count = soup.find("div", {"class": "answer_count"}).text.strip()
        count = int(re.match(r'(\d+) Answers', ans_count).groups()[0])
    except:
        return jsonify(question=question, answers=answers)

    question['answer_count'] = count

    count = len(divs) - 1 if count < 6 else 6
    for i in range(count):
        one_answer = {
            'votes': '-1',
            'rank': 0,
            'answer': ''
        }
        try:
            author = {}
            author['name'] = divs[i].find("div", {"class": "author_info"}).find("span", {"class": "feed_item_answer_user"}).find("a", {"class": "user"}).string
            author['bio'] = divs[i].find("div", {"class": "author_info"}).find("span", {"class": "feed_item_answer_user"}).find_all("span", {"class": "rep"})[1].find("span", {"class": "hidden"}).text
        except:
            author['name'] = 'Anonymous'
            author['bio'] = ''
        one_answer['author'] = author

        return jsonify(question=question, answers=answers, one_answer=one_answer)

        one_answer['votes'] = divs[i].find("span", {"class":"numbers"}).text

        html_block = divs[i].find("div", {"id": re.compile("(.*)_container")}).contents
        answer_html = ''
        for p in range(len(html_block) - 1):
            answer_html += str(html_block[p])
        one_answer['answer_html'] = answer_html
        one_answer['answer'] = divs[i].find("div", {"class": "answer_content"}).text
        one_answer['rank'] = i + 1
        answers.append(one_answer)

    return jsonify(question=question, answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
