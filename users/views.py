import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from hw28 import settings
from users.models import User, Location


# Create your views here.
class UserListView(generic.ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_object = paginator.get_page(page_number)

        users = []
        for user in page_object:
            users.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "locations": list(user.locations.all().values_list("name", flat=True))
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
        }

        return JsonResponse(response, safe=False)


class UserDetailView(generic.DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "role": self.object.role,
            "age": self.object.age,
            "locations": list(self.object.locations.all().values_list("name", flat=True))
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(generic.CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "role", "age", "locations"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
            username=user_data["username"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"],
        )

        for location in user_data["locations"]:
            location_obj, created = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": list(user.locations.all().values_list("name", flat=True))
        })


class UserDeleteView(generic.DeleteView):
    model = User
    success_url = ""

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})
