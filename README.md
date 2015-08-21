# oneblog
基于flask的个人博客应用

独立部署
-----
python run.py


uwsgi
-----
* uwsgi /home/work/website/example.com/uwsgi.ini -d /home/work/log/uwsgi/example.com.log
* service nginx start