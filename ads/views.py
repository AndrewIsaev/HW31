import json
from typing import Type

from ads.models import Category, Advertisement
from django.db.models import QuerySet
from django.views import View
from django.views.generic import DetailView
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
# Create your views here.
class CategoryView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        categories: QuerySet[Category] = Category.objects.all()

        response: list = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request: HttpRequest) -> JsonResponse:
        category_data: dict = json.loads(request.body)

        category: Category = Category.objects.create(name=category_data["name"])
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        advertisements: QuerySet[Advertisement] = Advertisement.objects.all()
        response: list = []
        for advertisement in advertisements:
            response.append({
                "id": advertisement.id,
                "name": advertisement.name,
                "author": advertisement.author,
                "price": advertisement.price,
                "description": advertisement.description,
                "address": advertisement.address,
                "is_published": advertisement.is_published,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request: HttpRequest) -> JsonResponse:
        advertisement_data: dict = json.loads(request.body)
        advertisement: Advertisement = Advertisement.objects.create(**advertisement_data)
        return JsonResponse({
            "id": advertisement.id,
            "name": advertisement.name,
            "author": advertisement.author,
            "price": advertisement.price,
            "description": advertisement.description,
            "address": advertisement.address,
            "is_published": advertisement.is_published,
        }, json_dumps_params={"ensure_ascii": False})


class AdvertisementDetailView(DetailView):
    model: Type[Advertisement] = Advertisement

    def get(self, request: HttpRequest, *args: list, **kwargs: dict) -> JsonResponse:
        try:
            advertisement: Advertisement = self.get_object()
        except Advertisement.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": advertisement.id,
            "name": advertisement.name,
            "author": advertisement.author,
            "price": advertisement.price,
            "description": advertisement.description,
            "address": advertisement.address,
            "is_published": advertisement.is_published,
        }, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model: Type[Category] = Category

    def get(self, request: HttpRequest, *args: list, **kwargs: dict):
        try:
            category: Category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={"ensure_ascii": False})
