from django.shortcuts import render

# Create your views here.


def example_view(request):
    return render(request,'my_app/example.html')


def variables(request):

    my_var ={
        'first_name' : 'lucas',
        'last_name' : 'juesi',
        'some_list' : [1,2,3,4,4],
        'some_dict' : {
            'insidekey': 'inside_value',
            'anotherkey': 'another_value',

            }
    }

    return render(request, 'my_app/variables.html', context=my_var)