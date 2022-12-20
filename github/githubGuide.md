#### **git 폴더 만들기**
---
- git init 입력
    - 숨김폴더로 지정되어 안보일수도 있음

#### **github push 방법**
---
- github 계정에 가서 프로젝트에 대한 새로운 regitory를 만든다.
- 폴더에서 git bash here 접속한다.
- regitory 할당
~~~ 
git remote add origin https://github.com//ajcltm//~~~
~~~

- 등록된 regitory 확인
~~~
git remote -v
~~~

- github에 업로드
~~~
git push origin ---all
~~~

- push할때 아래 메세지가 나타나면

> This is usually caused by another repository pushing hint: to the same ref.

- 아래와 같이 입력하면 강제로 push 됨
~~~
git push -f origin master
~~~
- 또는 아래와 같이 입력해주고 창닫고(경고메세지는 무시) 다시 push 시도하면 됨
~~~
git pull origin master 
~~~

#### **commit 방법**
---
~~~
git add folderName/fileName.py
git commit -m "메세지 내용"
git push origin --all
~~~

#### **github clone 방법**
---
- 아래 입력
~~~
git clone https://github.com/ajcltm/projectName.git 
~~~

#### **commit 취소하기**
---
[방법 1] commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
~~~
git reset --soft HEAD^
~~~

#### **staged 확인하기**
---
~~~
git diff --name-only --cached
~~~