from flask import Blueprint, render_template
from apps.app import db 
from apps.models import (
     aboard_publication, domestic_publication,
    aboard_conference, domestic_conference, member_spec,
    present_member, past_member, home_content, activity_photo
)

from flask import request, redirect
from flask import  url_for


soda = Blueprint(
    "soda",
    __name__,
    template_folder="templates",
    static_folder = "static",
)


@soda.route("/")
def index():
    home_contents = home_content.query.all()
    return render_template("soda/home.html", home_contents=home_contents)



@soda.route("/people")
def people():
    member_specs = member_spec.query.all()
    present_members = present_member.query.all()
    return render_template("soda/people.html", member_specs= member_specs, present_members = present_members)


@soda.route("/gallery")
def gallery():
    activity_photos = activity_photo.query.all()
    return render_template("soda/gallery.html", activity_photos = activity_photos)

@soda.route("/intro")
def intro():
    return render_template("soda/intro.html")

@soda.route("/domain")
def domain():
    return render_template("soda/domain.html")

@soda.route("/prof")
def prof():
    return render_template("soda/prof.html")



@soda.route("/graduate")
def graduate():
    past_members = past_member.query.all()
    return render_template("soda/graduate.html", past_members= past_members)



@soda.route("/public")
def public():
    aboard_publications = aboard_publication.query.all()
    domestic_publications = domestic_publication.query.all()
    domestic_conferences = domestic_conference.query.all()
    aboard_conferences = aboard_conference.query.all()
    return render_template("soda/public.html", aboard_publications = aboard_publications,domestic_publications =domestic_publications, domestic_conferences = domestic_conferences, aboard_conferences = aboard_conferences)


@soda.route("/add", methods=["GET"])
def add_page():
    return render_template("soda/public_form.html")



# 저널 추가 

@soda.route("/add_publication", methods=["POST"])
def add_publication():  
    title = request.form.get("title")
    authors = request.form.get("authors")
    reference = request.form.get("reference")
    pub_type = request.form.get("pub_type")       
    if pub_type == "abroad":
        new_pub = aboard_publication(
                    title=title,
                    authors=authors,
                    reference = reference,
            )
    elif pub_type == "domestic":
        new_pub = domestic_publication(
                    title=title,
                    authors=authors,
                    reference = reference,
                )
    db.session.add(new_pub)
    db.session.commit()
    return redirect(url_for("soda.add_page")) 


# 컨퍼런스 추가 

@soda.route("/add_conference", methods=["POST"])
def add_conference():  
    title = request.form.get("title")
    conference_name = request.form.get("conference_name")
    date = request.form.get("date")
    confer_type = request.form.get("confer_type")       
    if confer_type == "abroad":
        new_confer = aboard_conference(
                    title=title,
                    conference_name=conference_name,
                    date = date,
            )
    elif confer_type == "domestic":
        new_confer = domestic_conference(
                    title=title,
                    conference_name=conference_name,
                    date = date,
                )
    db.session.add(new_confer)
    db.session.commit()
    return redirect(url_for("soda.add_page")) 


# 멤버 스펙 추가


@soda.route("/add_spec", methods=["POST"])
def add_spec():
    member = request.form.get("member")
    people = request.form.get("people")
    title = request.form.get("title")
    organi =  request.form.get("organi")
    date =  request.form.get("date")
    price = request.form.get("price")

    new_spec = member_spec(member = member,
                           people=people, 
                           title=title,
                           organi= organi,
                           date= date,
                           price = price)
    db.session.add(new_spec)
    db.session.commit()
    return redirect(url_for("soda.add_page"))



# 멤버 추가
from flask import current_app, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import uuid


@soda.route("/add_member", methods=["POST"])
def add_member():
    member = request.form.get("member")
    degree = request.form.get("degree")
    department = request.form.get("department")
    email = request.form.get("email")
    interest_part = request.form.get("interest_part")
    affiliation = request.form.get("affiliation")
    member_type = request.form.get("member_type")       
    profile_image_file = request.files.get('profile_image')
    # 2. 파일 처리: 파일이 존재하면 저장하고, 없으면 기본값 사용
    db_filename = 'default.jpg' # DB에 저장될 파일명 기본값


    if profile_image_file and profile_image_file.filename != '':
        original_filename = secure_filename(profile_image_file.filename)
    
    # --- 💡 여기가 수정된 부분입니다 ---
    # 파일 이름에 '.'이 있는지 확인하여 확장자를 안전하게 추출합니다.
        if '.' in original_filename:
            extension = original_filename.rsplit('.', 1)[1].lower()
        else:
        # 확장자가 없는 경우, 업로드를 거부하거나 기본 확장자를 지정할 수 있습니다.
        # 여기서는 이미지 파일이므로 임의로 'jpg'를 부여합니다.
            extension = 'jpg'
    # --- 💡 여기까지 ---

        unique_filename = str(uuid.uuid4()) + '.' + extension
    
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
        profile_image_file.save(save_path)
    
        db_filename = unique_filename

    # 3. DB에 저장: member_type에 따라 올바른 객체 생성
    if member_type == "present":
        new_member = present_member(
            member=member,
            profile_image=db_filename, 
            degree=degree,
            department=department,
            email=email,
            interest_part=interest_part,
        )
    elif member_type == "past":
        new_member = past_member(
            member=member,
            profile_image=db_filename,  
            degree=degree,
            department=department,
            email=email,
            affiliation=affiliation,
        )

    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for("soda.add_page"))



# 홈 콘텐츠 추가

@soda.route("/add_home_content", methods=["POST"])
def add_home_content():

    date =  request.form.get("date")
    title =  request.form.get("title")
    content =  request.form.get("content")

    new_home_content = home_content(
                           date= date,
                           title = title,
                           content = content)
    db.session.add(new_home_content)
    db.session.commit()
    return redirect(url_for("soda.add_page"))



# 활동 사진 추가 

@soda.route("/add_activity", methods=["POST"])
def add_activity():
    title  = request.form.get("title")
    date = request.form.get("date")
    people = request.form.get("people")
    venue = request.form.get("venue")    
    activity_image_file = request.files.get('activity_image')
    # 2. 파일 처리: 파일이 존재하면 저장하고, 없으면 기본값 사용
    db_filename = 'default.jpg' # DB에 저장될 파일명 기본값


    if activity_image_file and activity_image_file.filename != '':
        original_filename = secure_filename(activity_image_file.filename)
    
    # --- 💡 여기가 수정된 부분입니다 ---
    # 파일 이름에 '.'이 있는지 확인하여 확장자를 안전하게 추출합니다.
        if '.' in original_filename:
            extension = original_filename.rsplit('.', 1)[1].lower()
        else:
        # 확장자가 없는 경우, 업로드를 거부하거나 기본 확장자를 지정할 수 있습니다.
        # 여기서는 이미지 파일이므로 임의로 'jpg'를 부여합니다.
            extension = 'jpg'
    # --- 💡 여기까지 ---

        unique_filename = str(uuid.uuid4()) + '.' + extension
    
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER_2'], unique_filename)
        activity_image_file.save(save_path)
    
        db_filename = unique_filename

        new_activity = activity_photo(
            title= title,
            activity_image=db_filename,  
            date =date ,
            people=people,
            venue=venue,
        )

    db.session.add(new_activity)
    db.session.commit()
    return redirect(url_for("soda.add_page"))


@soda.route("delete_publication", methods=["POST"])
def delete_publication():
    title_to_delete = request.form['title_to_delete']
    title_obj_1 = domestic_publication.query.filter_by(title=title_to_delete).first()
    title_obj_2 = aboard_publication.query.filter_by(title=title_to_delete).first() 
    if title_obj_1:
        try:
            db.session.delete(title_obj_1)
        except Exception as e:
            db.session.rollback()
    if title_obj_2:
        try:
            db.session.delete(title_obj_2)
        except Exception as e:
            db.session.rollback()         
    db.session.commit()
    return redirect(url_for("soda.add_page"))


@soda.route("delete_conference", methods=["POST"])
def delete_conference():
    title_to_delete = request.form['title_to_delete']
    title_obj_1 = domestic_conference.query.filter_by(title=title_to_delete).first()
    title_obj_2 = aboard_conference.query.filter_by(title=title_to_delete).first() 
    if title_obj_1:
        try:
            db.session.delete(title_obj_1)
        except Exception as e:
            db.session.rollback()
    if title_obj_2:
        try:
            db.session.delete(title_obj_2)
        except Exception as e:
            db.session.rollback() 
    db.session.commit()
    return redirect(url_for("soda.add_page"))



@soda.route("delete_spec", methods=["POST"])
def delete_spec():
    title_to_delete = request.form['title_to_delete']
    member_to_delete = request.form['member_to_delete']
    obj = member_spec.query.filter_by(title=title_to_delete, member = member_to_delete).first() 
    if obj:
        try:
            db.session.delete(obj)
        except Exception as e:
            db.session.rollback()
    db.session.commit()
    return redirect(url_for("soda.add_page"))    




@soda.route("delete_member", methods=["POST"])
def delete_member():
    member_name_to_delete = request.form['member_to_delete']
    member_obj_1 = present_member.query.filter_by(member=member_name_to_delete).first()
    member_obj_2 = past_member.query.filter_by(member=member_name_to_delete).first() 
    if member_obj_1:
        try:
            db.session.delete(member_obj_1)
        except Exception as e:
            db.session.rollback()
    if member_obj_2:
        try:
            db.session.delete(member_obj_2)
        except Exception as e:
            db.session.rollback() 
    db.session.commit()
    return redirect(url_for("soda.add_page"))  

@soda.route("delete_home_content", methods=["POST"])
def delete_home_content():
    title_to_delete = request.form['title_to_delete']
    obj = home_content.query.filter_by(title=title_to_delete).first()
    if obj:
        try:
            db.session.delete(obj)
        except Exception as e:
            db.session.rollback()
    db.session.commit()
    return redirect(url_for("soda.add_page"))     

@soda.route("delete_activity", methods=["POST"])
def delete_activity():
    title_to_delete = request.form['title_to_delete']
    obj = activity_photo.query.filter_by(title=title_to_delete).first()
    if obj:
        try:
            db.session.delete(obj)
        except Exception as e:
            db.session.rollback()
    db.session.commit()
    return redirect(url_for("soda.add_page"))    