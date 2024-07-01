from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q


from movies.models import Filmwork


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ["get"]

    def get_queryset(self):
        filmworks = Filmwork.objects.values(
            "id",
            "created",
            "modified",
            "title",
            "description",
            "creation_date",
            "rating",
            "type",
        ).annotate(
            genres=ArrayAgg("genre__name", distinct=True),
            actors=ArrayAgg(
                "person__full_name",
                filter=Q(personfilmwork__role="actor"),
                distinct=True,
            ),
        )

        return filmworks  # Сформированный QuerySet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            "results": list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
