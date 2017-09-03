from django.utils.decorators import classonlymethod

def func(a, b='b', c='c', *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print()
    print(args)

    print()
    print(kwargs)
    print()
    print('-------------')


# func('a')

# func(a='A')

# func('a', 'b')
#
# func('a', 'b', 'c')
#
# func('a', 'b', 'c', 'd', 'e')
#
# func('a', 'b', 'c', 'd', 'e', f='f', g='g')


# func('a', 'b', 'd', 'e', f='f', g='g')

# func('a', 'b', 'd', 'e', f='f', g='g')

class LogoutView(object):

    @classonlymethod
    def as_view(cls, **initkwargs):
        print('class initkwargs')
        print(initkwargs)
        print()

        def view(request, *args, **kwargs):
            print('viewargs')
            print(args)
            print()
            print('view kwargs')
            print(kwargs)
        return view


def logout(request, next_page=None, template_name='registration/logged_out.html',
           redirect_field_name='REDIRECT_FIELD_NAME', extra_context=None, *args, **kwargs):
    # for key in ['next_page', 'template_name', 'redirect_field_name', 'extra_context']:
    #     if key not in kwargs.keys():
    #         kwargs[key] = locals()[key]

    return LogoutView.as_view(**kwargs)(request, next_page, template_name, redirect_field_name, extra_context, *args, **kwargs)

request = 'request'
next_page = 'next_page'
template_name = 'template'

logout(request, next_page, template_name, 'a', 'b', c='c', d='d')


def logout2(request, next_page=None,
           template_name='registration/logged_out.html',
            redirect_field_name='REDIRECT_FIELD_NAME',
            extra_context=None, **kwargs):
    print('next page', next_page)
    print('template', template_name)
    print('redirect', redirect_field_name)
    print('extra', extra_context)
    print(kwargs)
    print(locals())

# logout2(request, b='b', next_page='C', redirect_field_name='red', extra_context='ex', template_name='temp')
