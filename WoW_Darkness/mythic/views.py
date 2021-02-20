from django.shortcuts import render


def test_view(request):
    timer = {
        'timer_1': '1',
        'timer:2': '2',
        'timer_3': '3',
        'timer_4': '4',
    }
    return render(request, 'mythic.html', {'timer_1': {'timer': '1'},
                                            'timer:2': '2',
                                            'timer_3': '3',
                                            'timer_4': '4',
                                           })
