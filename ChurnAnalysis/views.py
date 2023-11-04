from django.shortcuts import render, redirect
from .forms import RecordForm
import csv

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():

            customerID =form.cleaned_data['customerID']
            gender=form.cleaned_data['gender']
            SeniorCitizen=form.cleaned_data['SeniorCitizen']
            Partner=form.cleaned_data['Partner']
            Dependents=form.cleaned_data['Dependents']
            tenure=form.cleaned_data['tenure']
            PhoneService=form.cleaned_data['PhoneService']
            MultipleLines=form.cleaned_data['MultipleLines']
            InternetService=form.cleaned_data['InternetService']
            OnlineSecurity=form.cleaned_data['OnlineSecurity']
            OnlineBackup=form.cleaned_data['OnlineBackup']
            DeviceProtection=form.cleaned_data['DeviceProtection']
            TechSupport=form.cleaned_data['TechSupport']
            StreamingTV=form.cleaned_data['StreamingTV']
            StreamingMovies=form.cleaned_data['StreamingMovies']
            Contract=form.cleaned_data['Contract']
            PaperlessBilling=form.cleaned_data['PaperlessBilling']
            PaymentMethod=form.cleaned_data['PaymentMethod']
            MonthlyCharges=form.cleaned_data['MonthlyCharges']
            TotalCharges=form.cleaned_data['TotalCharges']
            Churn=form.cleaned_data['Churn']



            csv_file_path = 'E:\\powerbi\\Telco-Customer-Churn.csv'


            with open(csv_file_path, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([customerID,gender,SeniorCitizen,Partner,Dependents,
                                 tenure,PhoneService,MultipleLines,InternetService,
                                 OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport
                                 ,StreamingTV,StreamingMovies,Contract,PaperlessBilling,
                                 PaymentMethod,MonthlyCharges,TotalCharges,Churn])

            return redirect('success.html')  # Redirect to a success page

    else:
        form = RecordForm()

    return render(request, 'index.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')