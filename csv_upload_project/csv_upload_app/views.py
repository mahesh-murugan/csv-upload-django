from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from csv_upload_app.forms import CSVUploadForm
import csv
import datetime

from csv_upload_app.models import Employee

# Create your views here.


class CSVUploadView(FormView):
    template_name = "csv_upload_app/index.html"
    form_class = CSVUploadForm
    success_url = reverse_lazy('csv-upload-view')
    
    def get_context_data(self):
        context = super().get_context_data()
        # print(Employee.objects.all())
        context['employees'] = Employee.objects.all()
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = self.form_class(self.request.POST, self.request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                csv_file = csv.reader(file.read().decode('utf-8').splitlines(), delimiter=",")
                
                first_row = [header.strip() for header in next(csv_file)]    
                
                employee_id = first_row.index('Employee ID')
                employee_name = first_row.index('Name')
                dob = first_row.index('Date Of Birth')
                address = first_row.index('Address')
                department = first_row.index('Department')

                # print(employee_id, employee_name, dob, address, department)

                for row in csv_file:
                    Employee.objects.update_or_create(
                        employee_id=row[employee_id],
                        name = row[employee_name].strip(),
                        dob = datetime.datetime.strptime(row[dob], "%d-%m-%Y").strftime("%Y-%m-%d"),
                        address = row[address],
                        department = row[department]
                    )
        return super().form_valid(form)
