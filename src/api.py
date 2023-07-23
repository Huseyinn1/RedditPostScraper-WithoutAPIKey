from database import RedditPost,engine
from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
import requests
app = Flask(__name__)



Session = sessionmaker(bind=engine)

@app.route("/posts", methods=["POST"])
def create_post():
    post_data = request.get_json()
    post = RedditPost(**post_data)
    session = Session()
    session.add(post)
    session.commit()
    session.close()
    return jsonify({"message": f"Post with title '{post.title}' added successfully!"})


@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    session = Session()
    post = session.query(RedditPost).filter_by(id=post_id).first()
    session.close()
    if post:
        post_data = {
            "id": post.id,
            "title": post.title,
            "author": post.author,
            "likes": post.likes,
            "date": post.date,
            "content": post.content,
            "url": post.url,
            "comment": post.comment
        }
        return jsonify(post_data)
    else:
        return jsonify({"message": f"Post with ID '{post_id}' not found!"})


@app.route("/posts", methods=["GET"])
def get_all_posts():
    session = Session()
    posts = session.query(RedditPost).all()
    session.close()
    post_list = []
    for post in posts:
        post_data = {
            "id": post.id,
            "title": post.title,
            "author": post.author,
            "likes": post.likes,
            "date": post.date,
            "content": post.content,
            "url": post.url,
            "comment": post.comment
        }
        post_list.append(post_data)
    return jsonify(post_list)

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    session = Session()
    post = session.query(RedditPost).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()
        session.close()
        return jsonify({"message": f"Post with ID '{post_id}' deleted successfully!"})
    else:
        session.close()
        return jsonify({"message": f"Post with ID '{post_id}' not found!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
