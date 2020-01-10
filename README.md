# padwy
个人博客

服务器更新的数据数据上传到github

1.git status 查看git是否有修改内容需要提交

2.git add 指向需要提交的内容文件

3.git commit -m "更新的说明"(如失败,输入下面代码 rm -f ./.Git/index.lock )

4.git push origin master 提交到远程仓库

数据迁移

python manage.py makemigrations

python manage.py migrate

拉取最新代码

git fetch --all

git reset --hard origin/master

git fetch 下载远程最新的。

git reset master 分支重置

本地代码强制覆盖git代码

git push origin master --force

deactivate #退出虚拟环境

重启服务器:

1.cd ~/sites/

2.source env/bin/activate #进入虚拟环境

3.cd padwy

gunicorn --bind unix:/tmp/wwvihs.cn.socket padwy.wsgi:application&