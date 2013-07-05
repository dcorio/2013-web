from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("symposion.schedule.views",
    #url(r"^$", "schedule_conference", name="schedule_conference"),
    url(r"^$", direct_to_template, {
        "template": "schedule_conference_tba.html"
    }, name="schedule_conference"),
    url(r"^beta", "schedule_conference", name="schedule_conference_beta"),
    url(r"^edit/$", "schedule_edit", name="schedule_edit"),
    url(r"^list/$", "schedule_list", name="schedule_list"),
    url(r"^presentations.csv$", "schedule_list_csv", name="schedule_list_csv"),
    url(r"^presentation/(\d+)/$", "schedule_presentation_detail", name="schedule_presentation_detail"),
    url(r"^([\w\-]+)/$", "schedule_detail", name="schedule_detail"),
    url(r"^([\w\-]+)/edit/$", "schedule_edit", name="schedule_edit"),
    url(r"^([\w\-]+)/list/$", "schedule_list", name="schedule_list"),
    url(r"^([\w\-]+)/presentations.csv$", "schedule_list_csv", name="schedule_list_csv"),
    url(r"^([\w\-]+)/edit/slot/(\d+)/", "schedule_slot_edit", name="schedule_slot_edit"),
    url(r"^conference.json", "schedule_json", name="schedule_json"),
)
