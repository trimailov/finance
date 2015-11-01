from django.contrib.auth.models import User

import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'admin%d' % n)
    password = 'secret'
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
