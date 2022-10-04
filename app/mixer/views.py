import json

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import A, RequestConfig
import django_tables2

from calc.views import is_ajax
from mixer.forms import MixerAddForm
from mixer.models import Mixer, MixerHistory
from mixer.tables import MixerHistorySumTable, MixerHistoryTable, MixerTable
from project.utils import DataMixin


# Create your views here.
@login_required
def mixer(request):
    context = DataMixin.get_user_context(title="Миксеры", btn_name="добавить")
    context['form'] = MixerAddForm
    qs = Mixer.objects.filter(user=request.user)
    
    extra_columns=[]
    extra_columns.append(('history', django_tables2.LinkColumn('mixer_history', text="История",
                                                              args=[A('pk'), ], verbose_name='История')))
    extra_columns.append(('delete', django_tables2.LinkColumn('mixer_del', text="Удалить",
                                                                  args=[A('pk'), ], verbose_name='Удалить')))
    my_table = MixerTable(qs, extra_columns=extra_columns)
    RequestConfig(request, paginate={'per_page': 10}).configure(my_table)
    context['table'] = my_table

    return render(request, 'mixer/index.html', context=context)


@login_required
def mixer_add(request):
    context = DataMixin.get_user_context(title="Миксеры", btn_name="добавить")
    form = MixerAddForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('mixer_index')
    context['form'] = form
    return render(request, 'mixer/index.html', context=context)


@login_required
def mixer_del(request, pk):
    Mixer.objects.get(pk=pk, user=request.user).delete()
    return redirect('mixer_index')


from django.db.models.functions import Concat
from django.db.models import F, Sum, Value, CharField



@login_required
def mixer_zero(request, pk, pomp):
    m = Mixer.objects.get(pk=pk, user=request.user)
    setattr(m, f"z_p{pomp}",  MixerHistory.objects.aggregate(total=Sum(f"p{pomp}"))['total'] or 0  )
    setattr(m, f"z_v{pomp}",  MixerHistory.objects.aggregate(total=Sum(f"v{pomp}"))['total'] or 0 )
    m.save()
    return redirect("mixer_history", pk)
    
@login_required
def mixer_history(request, pk):
    m = Mixer.objects.get(pk=pk, user=request.user)
    context = DataMixin.get_user_context(title="Миксер история", btn_name=None)
    extra_columns = []
    sum_extra_columns = []
    data = {}
    data_sum = {}
    
    for i in  m.mixer_fileds:
        data["t_"+i] = Concat(F(i), Value('/'), F(i.replace('p','v')),  output_field=CharField())
        data_sum[i] =   Sum(i)
        data_sum[i.replace('p', 'v')] =   Sum(i.replace('p', 'v'))
        
    qs     =  MixerHistory.objects.filter(mixer=pk,).annotate(**data)
    sum_qs = MixerHistory.objects.filter(mixer=pk,).aggregate( **data_sum)
    sum_data = {}
    for i in m.mixer_fileds:
        if hasattr(m, i ):
            extra_columns.append(("t_"+i , django_tables2.Column(getattr(m, i ))))
            # sum_extra_columns.append(("t_" + i, django_tables2.Column(getattr(m, i))))
            sum_extra_columns.append(("t_" + i,
                                          django_tables2.LinkColumn(
                                          viewname="mixer_zero",
                                        args=[m.pk, i.replace('p', '')],
                                        verbose_name=getattr(m, i)))
                                     )
            p = sum_qs.get(i) or 0 - getattr(m,f'z_{i}' or 0)
            v= sum_qs.get(i.replace('p','v')) or 0 -getattr(m, f"z_{i.replace('p','v')}") or 0
            sum_data[f"t_{i}"] = f"{round(p,2)}/{round(v,2)}"
   

    my_table = MixerHistoryTable(qs, extra_columns = extra_columns)
    RequestConfig(request, paginate={'per_page': 10}).configure(my_table)

    sum_table = MixerHistorySumTable([sum_data,], extra_columns=sum_extra_columns)
    RequestConfig(request, paginate={'per_page': 10}).configure(sum_table)
    
    context['table'] = my_table
    context['sum_table'] = sum_table
    context['mixer'] = m
    return render(request, 'mixer/history.html', context=context)


@csrf_exempt
def mixer_history_add(request):
    print(f'mixer_history_add')
    try:
    
        print('request POST', request.POST)
        print('request GET', request.GET)
        print('request body', request.body)
        data = json.loads(request.body)
        print('data', data)
        pk    = data.get('mixer_id')
        token = data.get('token')
        try:
            h = Mixer.objects.get(pk=pk, token=token)
            print(f'pk {pk} token {token}')
        except Mixer.DoesNotExist as e:
            return HttpResponse(f"Не найден в системе pk {pk} token {token} ")
        except Exception as e:
            raise  Http404

        h = MixerHistory()
        h.mixer_id=pk
        p1 = data.get('p1', None)
        p2 = data.get('p2', None)
        p3 = data.get('p3', None)
        p4 = data.get('p4', None)
        p5 = data.get('p5', None)
        p6 = data.get('p6', None)
        p7 = data.get('p7', None)
        p8 = data.get('p8', None)
        v1 = data.get('v1', None)
        v2 = data.get('v2', None)
        v3 = data.get('v3', None)
        v4 = data.get('v4', None)
        v5 = data.get('v5', None)
        v6 = data.get('v6', None)
        v7 = data.get('v7', None)
        v8 = data.get('v8', None)
        s =  data.get('s', None)

        h.p1 = p1
        h.p2 = p2
        h.p3 = p3
        h.p4 = p4
        h.p5 = p5
        h.p6 = p6
        h.p7 = p7
        h.p8 = p8
        h.v1 = v1
        h.v2 = v2
        h.v3 = v3
        h.v4 = v4
        h.v5 = v5
        h.v6 = v6
        h.v7 = v7
        h.v8 = v8
        h.s = s
        h.save()
    except Exception as e :
        raise e
    return HttpResponse("Ok")


@login_required
def mixer_history_clear(request, pk):
    m = Mixer.objects.get(pk=pk, user=request.user)
    MixerHistory.objects.filter(mixer=m).delete()
    return redirect('mixer_index')