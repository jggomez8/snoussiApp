from django.urls import path
from core.rrhh.views.employee.views import *
import core.rrhh.views.symptomsemp.admin.views as vsympemp_admin
import core.rrhh.views.symptomsemp.employee.views as vsympemp_employee
import core.rrhh.views.biometric.employee.views as vsbiometric_employee
import core.rrhh.views.biometric.admin.views as vsbiometric_admin
from core.rrhh.views.reports.views import ReportsView

urlpatterns = [
    # employee
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    # symptomsemp admin
    path('symptomsemp/admin/', vsympemp_admin.SymptomsEmpListView.as_view(), name='symptomsemp_admin_list'),
    path('symptomsemp/admin/delete/<int:pk>/', vsympemp_admin.SymptomsEmpDeleteView.as_view(),
         name='symptomsemp_admin_delete'),
    # symptomsemp employee
    path('symptomsemp/employee/', vsympemp_employee.SymptomsEmpListView.as_view(), name='symptomsemp_employee_list'),
    path('symptomsemp/employee/add/', vsympemp_employee.SymptomsEmpCreateView.as_view(),
         name='symptomsemp_employee_create'),
    path('symptomsemp/employee/update/<int:pk>/', vsympemp_employee.SymptomsEmpUpdateView.as_view(),
         name='symptomsemp_employee_update'),
    path('symptomsemp/employee/delete/<int:pk>/', vsympemp_employee.SymptomsEmpDeleteView.as_view(),
         name='symptomsemp_employee_delete'),
    # vsbiometric_employee
    path('biometric/employee/', vsbiometric_employee.BiometricListView.as_view(), name='biometric_employee_list'),
    path('biometric/employee/add/', vsbiometric_employee.BiometricCreateView.as_view(),
         name='biometric_employee_create'),
    # vsbiometric_admin
    path('biometric/admin/', vsbiometric_admin.BiometricListView.as_view(), name='biometric_admin_list'),
    path('biometric/admin/delete/<int:pk>/', vsbiometric_admin.BiometricDeleteView.as_view(),
         name='biometric_admin_delete'),
    # reports
    path('reports/', ReportsView.as_view(), name='reports'),
]
