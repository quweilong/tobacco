from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from tobacco import settings
from .models import PermissionsManagement
import time
# Create your views here.
class PermissionsView(APIView):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    def get(self, request):
        # 取到所有父节点
        objects = PermissionsManagement.objects.filter(parent_permissions_id=0)
        parent_nodes = list()
        for items in objects:
            parent_node = {
                'id': items.permissions_id,
                'name': items.permissions_name,
                'ProSort': '1',
                'remark': "",
                'pid': '',
                'isEdit': 'false',
                'children': []
            }
            objs = PermissionsManagement.objects.filter(parent_permissions_id=items.permissions_id)
            if objs:
                parent_nodes.append(PermissionsView.getTree(self,parent_node))
                pass
            else:
                parent_nodes.append(parent_node)
        return HttpResponse(json.dumps(parent_nodes, ensure_ascii=False))

    def post(self, request):
        items = request.data
        for item in items:
            PermissionsManagement.objects.all().delete()
            permissions_name = item['name']
            permissions_id = item['id']
            parent_permissions_id = item['pid']
            obj = PermissionsManagement.objects.create(create_time=self.current_time, update_time=self.current_time,
                                                       permissions_name=permissions_name,
                                                       permissions_id=permissions_id,
                                                       parent_permissions_id=parent_permissions_id)
            obj.save()
            # 如果存在 则调取递归
            if item['children']:
                PermissionsView.tree(self,item['children'])
        response = {}
        return HttpResponse(response)

    def delete(self,request):
        id = request.data['id']
        PermissionsManagement.objects.filter(permissions_id=id).delete()
        response = {}
        return HttpResponse(response)

    def tree(self,items):
        # 递归遍历所有子节点
        for item in items:
            permissions_name = item['name']     # 名称
            permissions_id = item['id']         # id
            parent_permissions_id = item['pid'] # 父id
            obj = PermissionsManagement.objects.create(create_time=self.current_time, update_time=self.current_time,
                                                           permissions_name=permissions_name,
                                                           permissions_id=permissions_id,
                                                           parent_permissions_id=parent_permissions_id)
            obj.save()
            PermissionsView.tree(self,item['children'])

    def getTree(self,parent_node):
        objs = PermissionsManagement.objects.filter(parent_permissions_id=parent_node['id'])
        for obj in objs:
            dict = {
                'id': obj.permissions_id,
                'name': obj.permissions_name,
                'ProSort': '1',
                'remark': "",
                'pid': '',
                'isEdit': 'false',
                'children': []
            }
            parent_node['children'].append(dict)
            PermissionsView.getTree(self,dict)
        return parent_node





