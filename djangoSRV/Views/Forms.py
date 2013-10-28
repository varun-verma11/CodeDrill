from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class StudentRegisterForm(forms.Form):
	username = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField(help_text='A valid email address')
	school = forms.CharField()
	year = forms.CharField()
	Class = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	repeat_password = forms.CharField(widget=forms.PasswordInput())

	def clean_repeat_password(self):
		password1 = self.cleaned_data.get("password", "")
		password2 = self.cleaned_data['repeat_password']
		if password1 != password2:
			raise forms.ValidationError(_("The passwords you entered did not match!"))
		return password2

class TeacherRegisterForm(forms.Form):
	username = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField(help_text='A valid email address')
	school = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	repeat_password = forms.CharField(widget=forms.PasswordInput())
	def clean_repeat_password(self):
		password1 = self.cleaned_data.get("password", "")
		password2 = self.cleaned_data['repeat_password']
		if password1 != password2:
			raise forms.ValidationError(_("The passwords you entered did not match!"))
		return password2

class SubmitCodeForm(forms.Form):
	code = forms.CharField(widget=forms.Textarea)

