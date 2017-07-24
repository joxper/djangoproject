from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']


def validate_category(value):
	category = value.capitalize()
	if not value in CATEGORIES and not category in CATEGORIES:
		raise ValidationError("is not a valid category")