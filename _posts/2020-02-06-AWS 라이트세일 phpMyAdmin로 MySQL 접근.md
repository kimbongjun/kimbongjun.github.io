---
layout: post
title: AWS 라이트세일 phpMyAdmin로 MySQL 접근
tags: 
- aws
- mysql
image: "/images/posts/200123_Bitnami_logo.png"
categories: [web]
last_modified_at: 2020-02-06
---

{% highlight markdown %}
[To Do List]

1. Windows 환경에서 phpMyAdmin 접속
2. Mac OS X 환경에서 phpMyAdmin 접속
{% endhighlight %}

#### 1. Windows 환경에서 phpMyAdmin 접속 (※ [참고](https://docs.bitnami.com/aws/faq/get-started/access-phpmyadmin/){:target="\_blank"})

`준비물` 
1. [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){:target="\_blank"}
1. ppk 파일
1. 라이트세일의 Public IP
1. bitnami 비밀번호 (ssh에서 `cat bitnami_application_password` 을 통해 얻음)

준비물이 갖춰졌다면 Putty를 실행한다.

##### 첫째, `Session` -> Public IP를 입력한다.
##### 둘째, `Connection - SSH - Auth` -> Pravite Key 경로를 입력해준다.
##### 셋째, `Connection - SSH - Tunnels` -> Source post, Destination을 추가해준다. `SSL을 적용해줬다면 localhost:443 으로 Destination을 기입`
##### 넷째, `Connection - Data` Auto-login username에 bitnami 입력.
##### 다섯째, `Session`으로 다시 이동 후 Saved Sessions를 통해 현재까지 입력한 내용들을 저장해준다.
##### 여섯째, `Session`의 Open 버튼을 클릭하여 SSH가 정상적으로 접속되는지 확인한다.
##### 일곱째, 브라우저의 주소창에 http://127.0.0.1:8888/phpmyadmin/ 에 접속해서 phpMyAdmin 로그인 화면이 나오면 성공. `계정정보는 root / bitnami 비밀번호`