from django.urls import path, include  # Import necessary components from Django's URL handling module
from api import views  # Import views from your 'api' app 


# URL Configuration (urlpatterns)
# -------------------------------
urlpatterns = [
    # API Endpoint Inclusion
    # -------------------------
    path('api/', include('api.urls')), 
    # This line does the following:
    #   - Matches any URL starting with '/api/'
    #   - Delegates further URL matching to the 'urlpatterns' defined in the 'api.urls' file.
    #   - This keeps your API endpoints organized in their own file for better project structure.

]