from django.forms import ModelForm,TextInput,Select,Textarea,FileInput
from diff.models import InterfaceModel

class CreateForm(ModelForm):
    class Meta:
        model = InterfaceModel
        fields = ['testurl','defaulturl','querycount','topn','pn','countrepeat','statusflag','resultflag','threadnum','reason','remark','selfdata']
        widgets = {
            'testurl': TextInput(attrs={'class':'form-control','id':'interfacetask-testurl'}),
            'defaulturl': TextInput(attrs={'class':'form-control','id':'interfacetask-defaulturl'}),
            'querycount': Select(attrs={'class':'form-control','id':'interfacetask-querycount'}),
            'topn': Select(attrs={'class':'form-control','id':'interfacetask-topn'}),
            'pn': Select(attrs={'class':'form-control','id':'interfacetask-pn'}),
            'countrepeat': Select(attrs={'class':'form-control','id':'interfacetask-countrepeat'}),
            'statusflag': TextInput(attrs={'class':'form-control','id':'interfacetask-statusflag'}),
            'resultflag': TextInput(attrs={'class':'form-control','id':'interfacetask-resultflag'}),
            'threadnum': Select(attrs={'class':'form-control','id':'interfacetask-threadnum'}),
            'reason': Select(attrs={'class':'form-control','id':'interfacetask-reason'}),
            'remark': Textarea(attrs={'class':'form-control','id':'interfacetask-remark','rows':3}),
            'selfdata': FileInput(attrs={'class':'form-control','id':'interfacetask-selfdata'}),
        }
