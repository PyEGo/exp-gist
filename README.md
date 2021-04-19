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
* **hard-gists-ego-s2** stores PyEGo-generated Dockerfile(implement select-all strategy).<br/>
  The folder structure is the same as hard-gists-ego's(implement default strategy, select-one)<br/>
  Our strategies are describe as follow:
  
  |id|select strategy|
  |----|-----|
  |1|select-one|
  |2|select-all|
  
* **Log** folder stores execution logs. 
  We dockerize projects(build docker images and run images in container) based on Dockerfile or requirements.txt,
  and then records execution results into logs.<br/>
  The folder structure is as follow:
```$xslt
.
├── PyEGo.log # log for PyEGo(implement strategy1)
├── PyEGo-s2.log # log for PyEGo(implement strategy2)
├── DockerizeMe.log # log for DockerizeMe
└── Pipreqs.log # log for Pipreqs
```  
* **results_hard_gists.csv** stores results of experiments on all projects.

