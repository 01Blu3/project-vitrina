from app.users import *
from dotenv import load_dotenv
from flask import Flask, render_template
import os


load_dotenv()
app = Flask(__name__)
app.url_map.host_matching = True

if __name__== "__main__":
    app.run()



""" Route names post-fix """
# -aboutme
# -work
# -education
# -hobbies
# -places

@app.route('/')
def index():
    return render_template('work.html', title="Xavier's Profile", name="Xavier",
                           work_length="Jan 30/2023 - April 30/2023",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           career=xavier_career,  # Uses xavier_career dict to fill out details
                           user_education=xavier_education,
                           url=os.getenv("URL"))


""" Xavier Flask Routes """
@app.route('/xavier-aboutme')
def xav_aboutme():
    return render_template('about.html', title="Xavier's Profile", name="Xavier", contact_info=xavier_about["contact"], about_me=xavier_about["aboutme"],
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           user_hobbies=xavier_hobby,
                           url=os.getenv("URL"))


@app.route('/xavier-work')
def xav_work():
    return render_template('work.html', title="Xavier's Profile", name="Xavier",
                           work_length="Jan 30/2023 - April 30/2023",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           career=xavier_career,  # Uses xavier_career dict to fill out details
                           user_education=xavier_education,
                           url=os.getenv("URL"))


@app.route('/xavier-education')
def xav_education():
    return render_template('education.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           url=os.getenv("URL"))


@app.route('/xavier-hobbies')
def xav_hobby():
    return render_template('hobbies.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           user_hobbies=xavier_hobby,
                           education_route='xav_education',
                           places_route='xav_places',
                           url=os.getenv("URL"))


@app.route('/xavier-places')
def xav_places():
    return render_template('places.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route='xav_aboutme',
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           mapper=xavier_mapper,
                           url=os.getenv("URL"))