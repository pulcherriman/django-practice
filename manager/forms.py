from django.forms import ModelForm
from manager.models import Task
from datetimewidget.widgets import DateTimeWidget

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = "__all__"
		dateTimeOptions = {
			'format': 'yyyy-mm-dd',
			'autoclose': True,
			'showMeridian': True
		}
		widgets = {
			'date': DateTimeWidget(options=dateTimeOptions)
		}