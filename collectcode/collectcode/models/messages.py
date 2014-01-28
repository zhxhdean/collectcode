#-*-coding:utf8-*-
from django.conf import settings

SUCCESS = u'操作成功!'

NOVALUE_USER = u'用户名不能空'

INVALID_USER = u'无效的用户'

INVALID_PASSWORD = u'密码错误'

NOVALUE_PASSWORD = u'密码不能空'

PROGRAM_EXCEPTION = u'程序异常'

MIN_LENGTH_5 = u'字符长度最少5'

MAX_LENGTH_10 = u'字符长度不能超过10'

MAX_LENGTH_20 = u'字符长度不能超过20'

MAX_LENGTH_30 = u'字符长度不能超过30'

MAX_LENGTH_250 = u'字符长度不能超过250'

NOVALUE_TITLE = u'标题不能空'

NOVALUE_NOTE = u'内容不能空'

INVALID_REQUEST = u'无效请求'

NOVALUE_EMAIL = u'email不能空'

INVALID_EMAIL = u'email格式不正确'

NOVALUE_COMMENT = u'留言不能空'

NOVALUE_URL = u'link地址不能为空'

NOVALUE_TEXT = u'不能为空'

INVALID_URL = u'url格式不正确'

INVALID_SUFFIX = u'上传图片格式不正确,只支持%s' %''.join(settings.ALLOW_SUFFIX)

UPLOAD_MAX_SIZE = u'上传文件超出最大限制,%sM' %settings.UPLOAD_MAX_SIZE

