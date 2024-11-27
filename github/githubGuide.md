#### **git 폴더 만들기**
---
- 숨김폴더로 지정로 지정됨
~~~git
git init 입력
~~~

#### **git 설정**
---
~~~git
$ git config --global user.name "Kenneth"
$ git config --global user.email "kenneth@pigno.se"
~~~

#### **github 원격등록**
---
- github 계정에 가서 프로젝트에 대한 새로운 regitory를 생성해야함
- regitory 할당
~~~git 
git remote add origin https://github.com/ajcltm/projectName.git
~~~

- 등록된 regitory 확인
~~~git
git remote -v
~~~

#### **github 업로드***
---
- github에 업로드
~~~git
git push origin ---all
~~~
- push할때 아래 메세지가 나타나면 아래와 같이 입력하면 강제로 push 됨
> This is usually caused by another repository pushing hint: to the same ref.
~~~
git push -f origin master
~~~
- 또는 아래와 같이 입력해주고 창닫고(경고메세지는 무시) 다시 push 시도하면 됨
~~~
git pull origin master 
~~~

#### **github 다운로드(clone)**
---
~~~git
git clone https://github.com/ajcltm/projectName.git
~~~

#### **commit 방법**
---
- stage 등록
~~~git
git add folderName/fileName.py # 특정파일 staging
git add .  # ignore파일 제외하고 staging
git add *  # ignore파일 포함 staging
~~~

- status 확인
~~~git
$ git status
~~~

- staged 확인하기
~~~
git diff --name-only --cached
~~~

- commit
~~~git
git commit -m "메세지 내용"
~~~

- commit 취소하기
~~~git
# 바로 이전 단계로 인덱스와 워킹트리를 버리고 리셋.
$ git reset HEAD^ --hard

# 바로 두번째 전 단계로 인덱스와 워킹트리를 버리고 리셋.
$ git reset HEAD~2 --hard

# 특정 리비전의 기록으로 인덱스는 버리고 워킹트리를 보존하여 리셋.
$ git reset 991ee8c --mixed
~~~
#### **github clone 방법**
---
- 아래 입력
~~~
git clone https://github.com/ajcltm/projectName.git 
~~~

#### **branch**
---
- branch 등록
~~~git
git branch new_branch
~~~

- branch 접속
~~~git
git checkout new_branch
~~~

- branch 삭제
~~~git
git branch -D new # 삭제
git push origin :new_branch  # 원격저장소 등록 ( ":" 붙여야함)
~~~