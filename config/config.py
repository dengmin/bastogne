"""配置文件

"""

conf = {
    #分页中每页显示影片数量
    'MOVIE_NUM': 10,
    #分类中显示的分类数目
    'GENRES_NUM': 100,
    'YEAR': {
        'start': 1930,
        'end': 2014,
    },
    'HOT_MOVIE': {
        #显示数目
        'num': 12,
        #最低点击数目
        'hot': 3,
    }
}


settings = {
    "app": 'Bastogne',
    "template_path": "templates",
    "static_path": "static",
    "cookie_secret": "entercookiesecret",
    "login_url": "/login",
    "xsrf_cookies": True,
    "debug": False,
}

#百度统计代码
tongji_code = """
<script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "//hm.baidu.com/hm.js?23bf9b84f74b05c2b22e17b62fe14844";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
</script>
"""