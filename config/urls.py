from handler import base, index, movie, api


urls = [
    (r'/', index.MovieHandler),
    (r'/movie', index.MovieHandler),
    (r'/post/(\d{0,5})', movie.PostHandler),
    (r'/search', index.SearchHandler),

    (r'/api/movie', api.MovieHandler),
    #用于捕获未定义url（404）
    (r".*", base.BaseHandler),
]
