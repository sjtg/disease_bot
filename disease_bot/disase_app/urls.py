#urls 

from django.conf.urls import include, url

from .views import diseaseview

urlpatterns = [
	url(r'^b893e18af97148763ddacdb5f09ea75faeb65de4d49f56b0c5/?$', diseaseview.as_view())

]
