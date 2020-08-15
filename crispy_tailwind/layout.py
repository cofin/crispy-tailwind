from crispy_forms.bootstrap import Alert
from crispy_forms.layout import BaseInput


class Submit(BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag::
        submit = Submit('Search the Site', 'search this site')
    .. note:: The first argument is also slugified and turned into the id for the submit button.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "submit"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition ease-in-out duration-150"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Reset(BaseInput):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag::
        reset = Reset('Reset This Form', 'Revert Me!')
    .. note:: The first argument is also slugified and turned into the id for the reset.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "reset"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-red-600 hover:bg-red-500 focus:outline-none focus:border-red-700 focus:shadow-outline-red active:bg-red-700 transition ease-in-out duration-150"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Button(BaseInput):
    """
    Used to create a button descriptor for the {% crispy %} template tag::
        submit = Button('Search the Site', 'search this site')
    .. note:: The first argument is also slugified and turned into the id for the submit button.

    This is a customised version for Tailwind to add Tailwind CSS style by default
    """

    input_type = "button"

    def __init__(self, *args, css_class=None, **kwargs):
        if css_class is None:
            self.field_classes = "inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-50 focus:outline-none focus:border-indigo-300 focus:shadow-outline-indigo active:bg-indigo-200 transition ease-in-out duration-150"
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Alert(Alert):
    css_class = ""
