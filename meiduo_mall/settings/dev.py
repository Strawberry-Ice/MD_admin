"""
Django settings for meiduo_mall project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import datetime
import os  # 操作系统ubuntu模块
import sys  # python模块
from datetime import timedelta

# sys.path#导入包的路径

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
'''
__file__===>当前文件名dev.py
os.path.abspath()===>/home/python/Desktop/meiduo_tbd39/meiduo_mall/meiduo_mall/settings/dev.py
os.path.dirname()===>/home/python/Desktop/meiduo_tbd39/meiduo_mall/meiduo_mall/settings
os.path.dirname()===>/home/python/Desktop/meiduo_tbd39/meiduo_mall/meiduo_mall
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 指定应用的导包路径为meiduo_mall/apps
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
    "backend.meiduo.site"  # 用作负载均衡的集群服务器域名
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'django_crontab',  # 定时任务

    # 完整导包路径
    # 'meiduo_mall.apps.users.apps.UsersConfig',
    'users',
    'verifycations',
    'contents',
    'oauth',
    'areas',
    'goods',
    'carts',
    'orders',
    'payments',
]

MIDDLEWARE = [
    # 首行
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 补充Jinja2模板引擎环境
            'environment': 'meiduo_mall.utils.jinja2_env.jinja2_environment',
        },
    },
]

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'x',  # 数据库用户密码
        'NAME': 'meiduo_mall_db'  # 数据库名字
    },
    # 'slave': {
    #     'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
    #     'HOST': '192.168.203.151',  # 数据库主机
    #     'PORT': 8306,  # 数据库端口
    #     'USER': 'root',  # 数据库用户名
    #     'PASSWORD': 'mysql',  # 数据库用户密码
    #     'NAME': 'meiduo_tbd39'  # 数据库名字
    # },
}

# 数据库路由规则
# DATABASE_ROUTERS = ['meiduo_mall.utils.db_router.MasterSlaveDBRouter']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 开启django"时区"功能：保存到数据库中到关于日期到数据，会同一转化成UTC（0时区）时间
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 静态文件访问的url路径
STATIC_URL = '/static/'
# 静态文件的磁盘路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 指定静态文件的存放目录
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 缓存
CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/0",  # 可改：ip、port、db
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "image_code": {  # 图形验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "sms_code": {  # 短信验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "history": {  # 浏览记录
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {  # 购物车
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
# 指定session的保存方案
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# 日志：当运行出错时，记录在日志中，方便后续修改
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'logs/meiduo.log'),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# 指定用户模型类
AUTH_USER_MODEL = 'users.User'  # 应用名称.模型类名称

# 指定认证后端
# 手机号和用户名都能够作为登陆依据
AUTHENTICATION_BACKENDS = [
    'meiduo_mall.utils.authenticate.MeiduoModelBackend',
]

# 指定登录视图URL地址
LOGIN_URL = '/login/'

# QQ授权登录的信息
QQ_CLIENT_ID = '101518219'
QQ_CLIENT_SECRET = '418d84ebdc7241efb79536886ae95224'
QQ_REDIRECT_URI = 'http://www.meiduo.site:8000/oauth_callback'

# 邮箱服务器配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 指定邮件后端
EMAIL_HOST = 'smtp.163.com'  # 发邮件主机
EMAIL_PORT = 25  # 发邮件端口
EMAIL_HOST_USER = 'hmmeiduo@163.com'  # 授权的邮箱
EMAIL_HOST_PASSWORD = 'hmmeiduo123'  # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = '美多商城<hmmeiduo@163.com>'  # 发件人抬头
# 邮箱验证链接
EMAIL_VERIFY_URL = 'http://www.meiduo.site:8000/emails/verification/'

# fdfs的访问域名
FDFS_URL = 'http://image.meiduo.site:8888/'
# 指定文件存储类型
DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fdfs.storage.FdfsStorage'

# Haystack
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://192.168.47.128:9200/',  # Elasticsearch服务器ip地址，端口号固定为9200
#         'INDEX_NAME': 'meiduo_tbd39',  # Elasticsearch建立的索引库的名称
#     },
# }

# 当添加、修改、删除数据时，自动生成索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# # 页大小
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2

# 支付宝配置
ALIPAY_APPID = '2016082100304973'  # 商家账号
ALIPAY_DEBUG = True  # 设置为True表示使用沙箱，设置为False则为正式环境
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'  # 支付网关，固定
ALIPAY_RETURN_URL = 'http://www.meiduo.site:8000/payment/status/'  # 支付成功后，支付宝返回的地址

# 定时任务
CRONJOBS = [
    # 每1分钟生成一次首页静态文件
    ('*/1 * * * *', 'contents.crons.generate_index_html',
     '>> ' + os.path.join(os.path.dirname(BASE_DIR), 'logs/crontab.log'))
]
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'  # 支持中文

# 配置跨域白名单
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8080",
    'http://www.meiduo.site:8080',
    'http://api.meiduo.site:8000',
]

# 允许携带cookie值
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_METHODS = [
#     "POST",
#     "GET",
# ]

# CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# datetime.datetime(year=2019, month=7, day=9, hour=11, minute=43, second=56) # 时间点对象
# datetime.timedelta(days=10) 对像，代表十天（时间段）
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=100),  # token有效期为100天
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'meiduo_admin.jwt_response_handler.customer_jwt_response_payload_handler',
    # 自定义函数构建最终jwt返回的结果：添加username和user_id
}
