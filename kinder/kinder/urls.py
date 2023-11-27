"""
URL configuration for kinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from child.views  import (
    home_page,
    )
from child.views  import (
    register,
    )
from child.views  import (
    reg_employee,
    )

from child.views  import (
    dropout_Emp,
    )

from child.views  import (
    existing_child,
    )
from child.views  import (
    search,
    )
from child.views  import (
    dropout,
    )

from child.views  import (
    home,
    )

from child.views  import (
    entity,
    )

from child.views  import (
    atendance,
    )

from child.views  import (
    emp_atendance,
    )

from child.views  import (
    concent_form,
    )

# from child.views  import (
#     updaterecord,
#     )

from child.views  import (
    updateData,
    )


from child.views  import (
    showatten,
    )


from child.views  import (
    reports,
    )

from child.views  import (
    balance_report,
    )

from child.views  import (
    emp_report,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
     path('home/',home),
    path('reg/',register),
    path('emp/',reg_employee),
    path('exist/',existing_child),
    path('report/',reports),
    path('balance_report/',balance_report),
    path('emp_reg/',emp_report),
    path('search/',search),
    path('dropout/',dropout),
    path('terminate/',dropout_Emp),
    path('entity/',entity),
    path('atendance/',atendance),
    path('atendance_emp/',emp_atendance),
    path('reg/concent_form/',concent_form),
    #path('search/updaterecord/', updaterecord, name='updaterecord')
    path('update/<id>',updateData,name="updateData"),
    path('atendance/<id>',showatten,name="showatten"),
]

