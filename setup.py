from setuptools import setup, find_packages

setup(
    # 배포할 패키지의 이름을 적는다. setup.py 파일을 가지는 폴더 이름과 동일하게 한다.
    name            = 'algorithm_hagyun',
    # 배포할 패키지의 버전을 적는다.
    version         = '0.1',
    # 배포할 패키지에 대한 설명을 작성한다.
    description     = 'Python Algorithm',
    # 배포하는 사람의 이름을 작성
    author          = 'Ha Gyun Kim',
    # 배포하는 사람의 메일주소를 작성한다.
    author_email    = 'imkimhagyun@naver.com',
    # 배포하는 패키지의 url을 적는다. 보통 github 링크를 적는다.
    url             = 'https://github.com/hagyun93/algorithm_hagyun',
    # 배포하는 패키지의 다운로드 url을 적는다.
    download_url    = 'https://github.com/hagyun93/algorithm_hagyun/archive/master.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적는다. ex) install_requires=['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install 할 때 함께 install 된다.
    install_requires    =   [],
    # 등록하고자 하는 패키지를 적는 곳
    # find_packages 라이브러리를 이용하기 때문에 아래와 같이 적는다.
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적는다.
    packages        = find_packages(exclude= []),
    # 패키지의 키워드를 적는다.
    keywords        = ['pypi deploy'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적는다.
    python_requires = '>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함
    package_data    = {},
    zip_safe        = False,
    # pypi에 등록될 메타 데이터를 설정
    # 실제 빌드에는 영향을 주지 않는다.
    classifiers     = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)