docker-settings
=========================

.. code-block:: shell

   # MySQLのimageをpull
   $ docker pull mysql:5.7

   # 確認
   $ docker images
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   mysql               5.7                 cd88b71c6c8c        2 days ago          383.4 MB

CentOS
--------------

.. code-block:: shell

   # 環境のbuild
   $ cd centos
   $ docker-compose build --no-cache

   # 環境の起動
   $ docker-compose up -d
   $ docker-compose run --rm bot bash
   # MySQLとの疎通確認
   [root@aa4a7143f3f4 app]# python3.5 connect_mysql_test.py
   {'password': 'very-secret', 'id': 1}

	# 終了
   $ docker-compose stop
   $ docker-compose down


Tips
---------


.. code-block:: shell

   # コンテナIDの確認
   $ docker ps
   # docker コンテナの削除
   $ docker rm {container id}


.. code-block:: shell

   # docker imageの確認
   $ docker images
   # docker imageの削除
   $ docker rmi {image id}
