---
layout: post
title: AWS 라이트세일 phpMyAdmin로 MySQL 접근
tags: 
- aws
- mysql
image: "/images/posts/phpmyadmin.png"
categories: [web]
last_modified_at: 2020-02-06
---

{% highlight markdown %}
[To Do List]

1. Windows 환경에서 phpMyAdmin 접속
2. Mac OS X 환경에서 phpMyAdmin 접속
{% endhighlight %}

#### 1. Windows 환경에서 phpMyAdmin 접속 (※ [참고](https://docs.bitnami.com/aws/faq/get-started/access-phpmyadmin/){:target="\_blank"})

{% highlight markdown %}
[준비물]
1. Putty
2. ppk 파일
3. 라이트세일의 Public IP
4. bitnami 비밀번호 (ssh에서 `cat bitnami_application_password` 을 통해 얻음)
{% endhighlight %}

준비물이 갖춰졌다면 [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){:target="\_blank"}를 실행한다.

##### 첫째, `Session` -> Public IP를 입력한다.
![phpmyadmin](/images/posts/200206-aws-phpmyadmin.png "phpmyadmin")
##### 둘째, `Connection - SSH - Auth` -> Pravite Key 경로를 입력해준다.
![phpmyadmin1](/images/posts/200206-aws-phpmyadmin-1.jpg "phpmyadmin1")
##### 셋째, `Connection - SSH - Tunnels` -> Source post, Destination을 추가해준다. (SSL을 적용해줬다면 localhost:443 으로 Destination을 기입)
![phpmyadmin2](/images/posts/200206-aws-phpmyadmin-2.png "phpmyadmin2")
##### 넷째, `Connection - Data` Auto-login username에 `bitnami` 입력.
![phpmyadmin3](/images/posts/200206-aws-phpmyadmin-3.jpg "phpmyadmin3")
##### 다섯째, `Session`으로 다시 이동 후 Saved Sessions를 통해 현재까지 입력한 내용들을 저장해준다.
![phpmyadmin4](/images/posts/200206-aws-phpmyadmin-4.jpg "phpmyadmin4")
##### 여섯째, `Session`의 Open 버튼을 클릭하여 SSH가 정상적으로 접속되는지 확인한다.
![phpmyadmin5](/images/posts/200206-aws-phpmyadmin-5.jpg "phpmyadmin5")
##### 일곱째, 브라우저의 주소창에 http://127.0.0.1:8888/phpmyadmin/ 으로 접속해서 phpMyAdmin 로그인 화면이 나오면 성공. (계정정보는 root / bitnami 비밀번호)
![phpmyadmin6](/images/posts/200206-aws-phpmyadmin-6.png "phpmyadmin6")

#### 2. Mac OS X 환경에서 phpMyAdmin 접속

{% highlight markdown %}
[준비물]
1. pem 파일 (라이트세일 로그인 후 다운로드 가능)
2. 라이트세일의 Public IP
3. bitnami 비밀번호 (ssh에서 `cat bitnami_application_password` 을 통해 얻음)
{% endhighlight %}

준비물이 갖춰졌다면 terminal을 실행시킨다.

##### 첫째, Terminal 에서 `ssh -N -L 8888:127.0.0.1:80 -i KEYFILE bitnami@SERVER-IP` 다음과 같이 입력한다.  
ex. ssh -N -L 8888:127.0.0.1:80 -i /Users/bongjour/Downloads/bongjour.pem bitnami@123.456.789.10

![phpmyadmin7](/images/posts/200206-aws-phpmyadmin-7.png "phpmyadmin7")

참고, 위에는 ssh 연결에 대한 Command 이고, 접속을 원한다면 다음과 같이 입력해주면 된다.  
`ssh -i /Users/bongjour/Downloads/bongjour.pem bitnami@123.456.789.10`

##### 둘째, 브라우저의 주소창에 http://127.0.0.1:8888/phpmyadmin/ 으로 접속해서 phpMyAdmin 로그인 화면이 나오면 성공. (계정정보는 root / bitnami 비밀번호)
