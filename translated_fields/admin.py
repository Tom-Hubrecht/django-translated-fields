from typing import Any, Dict

from django.contrib.admin.options import ModelAdmin
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from translated_fields.fields import show_language_code

__all__ = ("TranslatedFieldAdmin",)


class TranslatedFieldAdmin(ModelAdmin):
    def changelist_view(
        self, request: HttpRequest, extra_context: Dict[str, Any] = None
    ) -> TemplateResponse:
        with show_language_code(True):
            response = super().changelist_view(request, extra_context)
            if hasattr(response, "render"):
                response.render()
            return response

    def changeform_view(self, *args, **kwargs) -> HttpResponse:
        with show_language_code(True):
            response = super().changeform_view(*args, **kwargs)
            if hasattr(response, "render"):
                response.render()
            return response
