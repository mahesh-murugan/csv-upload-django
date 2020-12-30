from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from csv_upload_app.forms import CSVUploadForm
import csv
import datetime

from csv_upload_app.models import Employee

# Create your views here.

# view for csv upload 
class CSVUploadView(FormView):
    template_name = "csv_upload_app/index.html"
    form_class = CSVUploadForm
    success_url = reverse_lazy('csv-upload-view')
    
    def get_context_data(self):
        context = super().get_context_data()
        # print(Employee.objects.all())
        """ Query all the employees from Employee model """
        """ pass all employees queryset through context"""
        context['employees'] = Employee.objects.all()
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = self.form_class(self.request.POST, self.request.FILES)
            """ checks whether the form is valid or not """
            if form.is_valid():
                """ taking out the file object from form """
                file = form.cleaned_data['file']
                
                """ decode the bytes file to string and splited by newlines to a list """
                """ using csv reader function separated the string using delimiter as , """
                csv_file = csv.reader(file.read().decode('utf-8').splitlines(), delimiter=",")
                
                """ first row of the csv file is headings, assigned in a list"""
                first_row = [header.strip() for header in next(csv_file)]    
                
                """ assigning the corresponding index of the heading """
                employee_id = first_row.index('Employee ID')
                employee_name = first_row.index('Name')
                dob = first_row.index('Date Of Birth')
                address = first_row.index('Address')
                department = first_row.index('Department')

                # print(employee_id, employee_name, dob, address, department)

                """ looping through csv file """
                for row in csv_file:
                    """ Update or create employee """
                    Employee.objects.update_or_create(
                        employee_id=row[employee_id],
                        name = row[employee_name].strip(),
                        dob = datetime.datetime.strptime(row[dob], "%d-%m-%Y").strftime("%Y-%m-%d"),
                        address = row[address],
                        department = row[department]
                    )
        return super().form_valid(form)
