from django.shortcuts import render, redirect
from coding.models import *
from django.http import JsonResponse


def CategoryView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'index2.html', context)


def AddSameLevel(request, id):
    node = Category.objects.get(id=id)
    child = node.get_children().last()
    print(child)
    if node.type == 'ME':
        if  not child:
            newname = 10000
        else:
            newname = int(child.name) + 10000
        name = f'0{newname}'
        Category.objects.create(name=name, slug=name, parent=node, type='MED')
    elif node.type == 'MED':
        if  not child:
            newname = 100
        else:
            newname = int(child.name) + 100
        name = f'0{newname}'
        Category.objects.create(name=name, slug=name, parent=node, type='MEDM')
    elif node.type == 'MEDM':
        if  not child:
            newname = 1
        else:
            newname = int(child.name) + 1
        name = f'0{newname}'
        Category.objects.create(name=name, slug=name, parent=node, type='Part')
    return redirect('coding:category')

def get_parent_node(request):
    node_id = request.GET.get('node_id')
    node = Category.objects.get(id = node_id)
    parent_node_info = node.parent.name
    return JsonResponse({'parent_node_info': parent_node_info})


