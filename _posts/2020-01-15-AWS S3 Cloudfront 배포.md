---
layout: post
title: AWS S3 와 Cloudfront 배포
tags: aws
image: "/images/posts/phpmyadmin.png"
categories: [web]
last_modified_at: 2020-01-15
---

### AWS S3 업로드와 이를 배포하기 위한 Cloudfront

##### Amazon S3 [#](https://s3.console.aws.amazon.com/s3/home){:target="\_blank"}

아마존 S3에서 버킷 생성 후 업로드 하는 과정은 굉장히 쉽다. [※ 참고](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/gsg/GetStartedWithS3.html){:target="\_blank"}  
다만 업로드 한 콘텐츠를 글로벌하게 전송, 가속화하기 위한 수단으로 Cloudfront 서비스까지 이용해야 화룡점정이라 할 수 있다.

#### - Cloudfront Console [#](https://console.aws.amazon.com/cloudfront/home){:target="\_blank"}

우선, [https://aws.amazon.com/ko/getting-started/tutorials/deliver-content-faster/](https://aws.amazon.com/ko/getting-started/tutorials/deliver-content-faster/){:target="\_blank"} 여기 링크를 참고하여 "배포"에 대한 생성을 끝마친다.

#### - Cloudfront가 할당한 도메인이 아닌 원하는 도메인으로 배포 URL 연결하기

dleov5lkjdbta.cloudfront.net 이런 도메인 구조는 흉측하고 혐오스럽다.  
깔끔한 도메인(ex: cdn.example.com)으로 바꿔주는게 정신 건강에 이롭다.

![Cloudfront](/images/posts/aws-200115-1.jpg "Cloudfront")

1. Edit Distribution으로 이동 후 Alternate Domain Names 에 원하는 도메인을 입력한다.
2. SSL Certificate 에서 Custom SSL Certificate를 체크해준다.

물론 안 될 것이다.

이유는 ACM 에서 등록이 된 주소가 아직은 없기 때문이다.  
밑에 `Request or Import a Certificate with ACM` 버튼을 클릭 후 가지고 있는 SSL 도메인을 인증해주기 위한 절차를 밟는다.

##### 1. ACM에서 기존 소유한 인증서를 가져오기

[SSL 가져오기](https://console.aws.amazon.com/acm/home?region=us-east-1#/importwizard/){:target="\_blank"} 이동

![Cloudfront2](/images/posts/aws-200115-2.png "Cloudfront2")

이미지에 표기한 위치대로 pem 파일에 대한 정보를 기입해준다.  
필자의 경우 vi 커맨드를 입력하여 pem 파일에 대한 내용을 확인 -> 붙여넣기 (물론 sudo 권한이 있어야 pem 파일의 내용을 확인할 수 있다.)

태그의 경우 purpose : website 로 기입 (이건 딱히 정답이 없는 것 같다.)

인증서를 가져오는데 성공하면 위에서 실패한 `Edit Distribution` 의 내용들을 채워줄 수 있게 된다.
Alternate Domain Names 기입 후 적용해주면 또 다시 `배포가 활성화`될 때까지 기다려야 한다. (Deployed 되는게 생각보다 오래 걸린다...)

##### 2. 도메인을 실질적으로 쓰기 위한 A레코드 값을 추가.

Route53 서비스를 이용한 도메인인 경우 route53에 콘솔로 이동 후 A레코드 추가 -> 별칭(예) -> Cloudfront 배포 선택 후 생성을 해주면 끝난다.
하지만 필자는 특이하게도 아마존 라이트세일에서 제공해주는 DNS영역에 도메인을 추가하였기에 조금 다른 방식으로 적용했다.

![Cloudfront3](/images/posts/aws-200115-3.jpg "Cloudfront3")

명령 프롬프트를 통해 cloudfront에서 배포해주는 default 도메인의 IP를 알아냈고 IP 주소를 라이트세일의 DNS 영역에 추가해주었다.

![Cloudfront4](/images/posts/aws-200115-4.jpg "Cloudfront4")

위와 같이 라이트세일의 dns 영역에 추가를 해주니 cdn.example.com 주소로 배포할 수 있게 됐다.

#### - 끝으로

혹시라도 SSL 인증서를 가져오는 부분에 있어 난항을 겪고 있다면 기존에 발급받은 인증서를 다시 검토해보는게 좋다.  
필자의 경우 SSL 가져오는 pem 입력 과정에서 오류를 겪다가 와일드카드 인증서를 재발급받고 나서 문제를 해결할 수 있었다. (물론 무료 인증서인 Letsencrypt 기준)

시간이 거듭될 수록 AWS의 다양한 서비스를 겪게되서 흥미롭다.  
짧은 식견으로 인해 기재한 내용들의 질적 수준이 낮은 점은 아쉬우나 지속적으로 공부하고 업데이트 할 요량이니 기대해달라.
