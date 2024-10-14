from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
# from .views import UserListAPIView, UserCreateAPIView, UserProfileListAPIView, UserProfileDetailAPIView, FriendListCreateAPIView, FriendDetailAPIView, MatchHistoryListCreateAPIView, MatchHistoryDetailAPIView, TournamentListCreateAPIView, TournamentDetailAPIView, SetupTwoFactorView, ConfirmTwoFactorAuthView, TwoFactorSetupTemplateView, TwoFactorConfirmTemplateView


urlpatterns = [
	# path("auth/", obtain_auth_token),
	# path("", views.home), TwoFactorTemplateView
]