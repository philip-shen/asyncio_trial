# asyncio_trial
Asyncoio trial purpose

## Concurrency Test

Results:
asynchronous vs processpool vs threadpool vs sequential
![alt tag](https://i.imgur.com/WEPlrM6.jpg)

Step 1. 
Serve Side: Setup Web Server on Google Colud Platform (GCP) for testing purpose
![alt tag](https://i.imgur.com/R92L5hY.jpg)

Step 2.
Modules Installation:

On `Linux`:

```bash
(venv3) [root@CentOS python3-concurrency]# pip install -r requirements-linux.txt
```

On `Windows`（Without `uvloop`）:

```bash
(Flask_trial) d:\project\Python\asyncio_trial\concurrency> pip install -r requirements-win32.txt
```

Step 3.

Asynchronous：

Round 1:
![alt tag](https://i.imgur.com/kE6QwCF.jpg)

Round 2:
![alt tag](https://i.imgur.com/yJBM4IL.jpg)

Round 3:
![alt tag](https://i.imgur.com/XqBEggO.jpg)

ThreadPool:

Round 1:
![alt tag](https://i.imgur.com/qG8akLQ.jpg)

Round 2:
![alt tag](https://i.imgur.com/C3ibM29.jpg)

Round 3:
![alt tag](https://i.imgur.com/qkgRBvg.jpg)

ProcessPool:

Round 1:
![alt tag](https://i.imgur.com/dzHo7vc.jpg)

Round 2:
![alt tag](https://i.imgur.com/G9oTi1i.jpg)

Round 3:
![alt tag](https://i.imgur.com/7cLp6wu.jpg)

Sequence：

Round 1:
![alt tag](https://i.imgur.com/ZJOBGdm.jpg)

## Decorators
``` 
Decorators are “wrappers”, which means that they let you execute code before and after the function they decorate without modifying the function itself.
``` 

## Git from a foloder of repoA to repoB 
Step 1. 

![alt tag](https://i.imgur.com/ERx0VpM.jpg)

Step 2. 

![alt tag](https://i.imgur.com/Y1fIuTL.jpg)

Step 3. 

![alt tag](https://i.imgur.com/8UduWdr.jpg)

Step 4. 

![alt tag](https://i.imgur.com/7gBHKId.jpg)

Step 5. 

![alt tag](https://i.imgur.com/6UjGeWY.jpg)

Step 6. 

![alt tag](https://i.imgur.com/TYWFkeZ.jpg)

Step 7. 

![alt tag](https://i.imgur.com/TCIvnia.jpg)

Step 8. 

![alt tag](https://i.imgur.com/ntbiEH8.jpg)

Step 9. Previous log to add new Repo.

![alt tag](https://i.imgur.com/21of7W5.jpg)

Step 10. Error Msg

![alt tag](https://i.imgur.com/rCbMWOd.jpg)

Step 11. 

![alt tag](https://i.imgur.com/9CRpPGi.jpg)

Step 12. Done!

![alt tag](https://i.imgur.com/manguxu.jpg)

## Reference 
* [A Declarative HTTP Client for Python](https://github.com/prkumar/uplink)
* [Q: How can I make a chain of function decorators in Python?](https://gist.github.com/Zearin/2f40b7b9cfc51132851a)
* [How to use *args and **kwargs in Python](http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)
* [Can you explain closures (as they relate to Python)?](https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python)
* [How to make a chain of function decorators?](https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators#answer-739665)
* [[教學] Git搬運repository部分檔案至新repository 如何轉移部分檔案至新的repo並能保留舊有commit](https://xenby.com/b/126-%E6%95%99%E5%AD%B8-git%E6%90%AC%E9%81%8Brepository%E9%83%A8%E5%88%86%E6%AA%94%E6%A1%88%E8%87%B3%E6%96%B0repository)
* [python3-concurrency sequential vs processpool vs threadpool vs asynchronous](https://github.com/wangy8961/python3-concurrency)