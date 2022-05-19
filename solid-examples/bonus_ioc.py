"""
Inversion of Control (IoC)
its not a part of the dependency inversion principle but it is closely related
In python best samples for the IoC django settings and Django Rest Framework Views
You can apply IoC C# or Java web frameworks (Built-in, Autofac, Ninject Castle Windsor...)
"""


# settings.py
CACHES={
        'default': {'BACKEND': 'django.core.cache.backends.default'},
        'locmem': {'BACKEND': 'django.core.cache.backends.locmem'},
        'local': {'BACKEND': 'django.core.cache.backends.local'},
    }


class FooView(APIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (renderers.JSONRenderer,)
    throttle_classes = (UserRateThrottle, )

