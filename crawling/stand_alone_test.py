import django
from django.conf import settings
from django.conf import global_settings
from mysite import settings as mysetting
django.conf.settings.configure(default_settings=global_settings, INSTALLED_APPS=mysetting.INSTALLED_APPS, DATABASES = mysetting.DATABASES, DEBUG=True)
django.setup()


from realestate.models import Address

addr = Address(si_code=1, si_name='test_crawling', gu_code=2, gu_name="gu_test", dong_code=3, dong_name="dong_test")
addr.save()
print "store crawling data db test 1"
