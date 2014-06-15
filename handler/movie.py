from .base import BaseHandler
from tornado.web import authenticated


class PostHandler(BaseHandler):
    def get(self, pid):
        post = self.db.movie.find_one({'id': int(pid)})
        if post is None:
            self.send_error(404)
        else:
            #每访问一次热度加1
            self.db.movie.update({'id': int(pid)}, {'$inc': {'hot': 1}})
            self.render('post/index.html', post=post, side=self.get_side())