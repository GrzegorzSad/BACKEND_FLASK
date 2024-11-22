from app.api import bp

from app.models import Post

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return {'posts': [post.to_dict() for post in posts]}

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)
    if post in None:
        return {'error': 'post not found'}, 404
    return post.to_dict()