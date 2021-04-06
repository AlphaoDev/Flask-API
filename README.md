# Flask-API
 Flask API (client-server) in Docker.



This Flask API is an Docker container host monitoring tool and a client-side tool for logging statistics.  If you want to set up the same infrastructure follow this tutorial.

## Server Installation

Create your application directory and go it. For example :

```bash
$ mkdir /opt/docker/app_python | cd /opt/docker/app_python
```

Copy server files in your current directory and make sure that you have a data folder for sharing statistics.



Now, access to crontab configuration via :

```bash
$ sudo crontab -e
```

And add this lines :

| /etc/crontab                                                 |
| ------------------------------------------------------------ |
| * * * * * ( /usr/bin/python3 /opt/docker/app_python/stats.py )<br/>* * * * * ( sleep 10 ; /usr/bin/python3 /opt/docker/app_python/stats.py )<br/>* * * * * ( sleep 20 ; /usr/bin/python3 /opt/docker/app_python/stats.py )<br/>* * * * * ( sleep 30 ; /usr/bin/python3 /opt/docker/app_python/stats.py )<br/>* * * * * ( sleep 40 ; /usr/bin/python3 /opt/docker/app_python/stats.py )<br/>* * * * * ( sleep 50 ; /usr/bin/python3 /opt/docker/app_python/stats.py ) |

It will reload stats.py file every 10 seconds.



Build your image in your application directory and you can run it :

```bash
$ sudo docker build --tag app_python .
```

```bash
$ sudo docker run -p 5000:5000 -v /opt/docker/app_python/data:/data --rm app_python
```



#### Explanation of the files and folders

| File or folder   | Details                                              |
| ---------------- | ---------------------------------------------------- |
| data/            | Folder where statistics will be saved in stats file. |
| stats            | File where statistics will be saved.                 |
| Dockerfile       | Dockerfile used to build the app_python image.       |
| app.py           | Main Python file of Flask API.                       |
| stats.py         | Python file that refresh statistics datas.           |
| requirements.txt | Required modules installed in the image.             |



## Client

Create your application directory and go it. For example :

```bash
$ mkdir /opt/docker/app_python | cd /opt/docker/app_python
```

Copy client files in your current directory and make sure that you have a logs folder for sharing logs.



Change your server IP address in the client.py file:

```python
checkAPI("http://@IP:5000/api/server/")
```



Build your image in your application directory and you can run it :

```bash
$ sudo docker build --tag app_python .
```

```bash
$ sudo docker run -v /opt/docker/app_python/logs:/logs --rm app_python
```



#### Explanation of the files and folders

| File or folder   | Details                                              |
| ---------------- | ---------------------------------------------------- |
| logs/            | Folder where statistics will be saved in stats file. |
| XX-XX-XX_xx      | File where logs will be saved.                       |
| Dockerfile       | Dockerfile used to build the app_python image.       |
| client.py        | Main Python file of logger client.                   |
| entrypoint.sh    | Entrypoint file in container.                        |
| requirements.txt | Required modules installed in the image.             |



Now you have access to your supervision logs on the client !