docker-settings
=========================

.. code-block:: shell

   # MySQLのimageをpull
   $ docker pull mysql:5.7
   # データストア用のbusyboxのimageをpull
   # docker pull busybox

   # 確認
   $ docker images
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   mysql               5.7                 cd88b71c6c8c        2 days ago          383.4 MB
   busybox             latest              e02e811dd08f        5 weeks ago         1.093 MB

CentOS
--------------

.. code-block:: shell

   # 環境のbuild
   $ cd centos
   $ docker-compose build --no-cache

   # beproudbotのソースコードがあるフォルダをマウントする為、docker-compose.yamlを編集する
   $ vim docker-compose.yaml


::

   volumes:
   # write your beproudbot path
   # sample
   # - /Users/wan/Work/bp/beproudbot:/beproudbot
   ※ここに上記を参考にコンテナと共有するフォルダのパスを記載する


.. code-block:: shell

   # 環境の起動
   $ docker-compose up -d
   $ docker-compose run --rm app bash
   # MySQLとの疎通確認
   [root@aa4a7143f3f4 app]# python3.5 connect_mysql_test.py
   {'password': 'very-secret', 'id': 1}

.. code-block:: shell

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


.. code-block:: shell

   # DataVolumeContainerからDataVolumeをバックアップ
   # Docker 1.8.x and below
   $ docker run --rm --volumes-from mysql-datastore -v $(pwd):/backup busybox tar cvf /backup/backup.tar /var/lib/mysql
   # --rm: コンテナのプロセスが終了すると、コンテナを削除
   # --volumes-from: DataVolumeContainer名を指定
   # -v {host}:{container}: ホストのディレクトリをコンテナのディレクトリにマウント
   # busybox: DataVolumeバックアップに使用するimage名
   # tar cvf /backup/backup.tar /var/lib/mysql: コンテナで実行するコマンド


.. code-block:: shell

   # DataVolumeContainerにDataVolumeをレストア
   # Docker 1.8.x and below
   $ docker run --rm --volumes-from mysql-datastore -v $(pwd):/backup busybox tar cvf /backup/backup.tar /var/lib/mysql


.. code-block:: shell

   # MySQLコンテナに接続
   $ docker exec -it mysql bash
   root@38ecc8a8cbad:/# mysql -u root -p
