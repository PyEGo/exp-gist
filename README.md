# exp-gist

## Description
Experimental results on hard-gists dataset

## Architecture
* **hard-gists-ego** folder stores PyEGo-generated Dockerfile.<br/>
  The folder structure is as follow:
```$xslt
.
├── <gist-id>
│   ├── Dockerfile # PyEGo-generated Dockerfile
│   └── snippet.py # gist
├── <gist-id>
...
└── <gist-id>
```
* **hard-gists-reqs** folder stores Pipreqs-generated requirements.txt<br/>
  The folder structure is as follow:
```$xslt
.
├── <gist-id>
│   ├── Dockerfile # Template-generated Dockerfile
│   ├── requirements.txt # Pipreqs-generated requirements.txt
│   └── snippet.py # gist (The same as hard-gists-ego)
├── <gist-id>
...
└── <gist-id>
```
* **hard-gists-me** folder stores DockerizeMe-generated Dockerfile.<br/>
  The folder structure is as follow:
```$xslt
.
├── <gist-id>
│   ├── Dockerfile # DockerizeMe-generated Dockerfile
│   └── snippet.py # gist (The same as hard-gists-ego)
├── <gist-id>
...
└── <gist-id>
```
* **hard-gists-ego-s2** and **hard-gists-ego-s3** stores PyEGo-generated Dockerfile( respectively implement strategy 2 and 3).<br/>
  The folder structure is the same as hard-gists-ego's(implement default strategy, strategy1)<br/>
  Our strategies are describe as follow:
  
  |id|select strategy|optimization objective |
  |----|-----|-----|
  |1|select-one|approximate|
  |2|select-all|approximate|
  |3|select-one|exact|
  
* **Log** folder stores execution logs. 
  We dockerize projects(build docker images and run images in container) based on Dockerfile or requirements.txt,
  and then records execution results into logs.<br/>
  The folder structure is as follow:
```$xslt
.
├── PyEGo.log # log for PyEGo(implement strategy1)
├── PyEGo-s2.log # log for PyEGo(implement strategy2)
├── PyEGo-s3.log # log for PyEGo(implement strategy3)
├── DockerizeMe.log # log for DockerizeMe
└── Pipreqs.log # log for Pipreqs
```  
* **results.csv** stores results of experiments on all projects.

