from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class PostForm(forms.ModelForm):

    date_exp = forms.DateField(required=False, input_formats=['%d-%m-%Y'])

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.fields['date_exp'].widget.attrs={ 'placeholder': 'DD-MM-YYYY'}
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit_change', 'Submit', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "post_home" %}>Reset</a>'))

    class Meta:
        model = Post
        fields = ('name', 'content', 'date_exp')