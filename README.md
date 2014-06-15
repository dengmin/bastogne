# Bastogne

高清电影下载站
---


所有数据采集自imax.im和互联网，仅供学习研究之用。



## 安装：

测试数据可用 `mongoimport` 从data目录 导入 MongoDB。

### 默认数据中影片图片是豆瓣的链接，由于访问限制部分图片无法正常显示。

解决办法：

* 从[图片压缩包](http://pan.baidu.com/s/1jGn5l8U)下载图片
其中图片名称采用 
`urlsafe_b64encode(url.encode()).decode() + '.jpg'` 生成（url为movie['image'])，手动修改图片地址。

* 使用`tools/local_image.py` 工具将movie['image']修改为演示站点图片源（不保证永久有效）



## 演示站点: [riable](http://www.riable.com)

目前演示站点部署在windows azure的小型虚拟机上

* Linux(ubuntu) + nginx + MongoDB + Python3


## api

通过title参数获取电影信息

http://bastogne.chinacloudapp.cn/api/movie?title=阿甘正传


## TODO
* 直接根据豆瓣id添加新的电影条目
* 同步豆瓣电影评论