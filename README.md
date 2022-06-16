# simple-http-server

Simple http server using python3's built-in [http.server](https://docs.python.org/3/library/http.server.html) module with a PUT extenstion to be able to upload/send files to a hosting server quickly.

**Note** that the `http.server` is not suited for production evironments since it only implements basic security. This project meets my usecase requirements but may not fullfill yours. There are many prod ready alternatives - one I found suitable was [gunicorn](https://gunicorn.org/).

## How-to

1) Run `main.py` on your server machine that should receive files
1) Test locally: `curl -i -X PUT --upload-file path/to/your/file.txt http://localhost:8000`
1) Test on internal network: `ifconfig | grep inet` replace localhost

## Known issues

### Blocked firewall

In case the port 8000 is blocked in your firewall, you have to open it. 

For example, on RHEL/CentOS/Fedora, open port 8000 as shown below.

```
$ firewall-cmd --permanent --add-port=8000/tcp
$ firewall-cmd --reload
```

On Debian, Ubuntu you can allow the port as shown below. 

`$ sudo ufw allow 8000`

## References

* [https://stackoverflow.com/questions/39788591/python-simplehttpserver-to-receive-files](https://stackoverflow.com/questions/39788591/python-simplehttpserver-to-receive-files)
