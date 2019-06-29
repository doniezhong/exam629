# -*- coding: utf-8 -*-
import base64
import json
import os

from django.conf import settings
from django.http import StreamingHttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from home_application.api_manager import JobApiManager
from home_application.models import Exam
from home_application.utils import now_time, now_time_str, utc_to_datetime, datetime_to_str
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception


def home(request):
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')


def curd(request):
    return render_mako_context(request, '/home_application/curd.html')


def form(request):
    return render_mako_context(request, '/home_application/form.html')


def get_app_info(request):
    client = get_client_by_request(request)
    params = {
        'target_app_code': APP_ID,
        'fields': 'bk_app_code;bk_app_name;bk_app_code;bk_app_name;introduction;creator;developer'
    }
    res = client.bk_paas.get_app_info(params)
    result_data = res['data']
    return success_result(result_data)


def api_test(request):
    now_time()
    raise Exception(now_time_str())
    script_content = '''#!/bin/bash
CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
echo -e "CPU=$CPU"'''
    job_api = JobApiManager(request)
    res = job_api.execute_and_get_log(
        bk_biz_id=2,
        script_content=script_content,
        ip_list=[{
            'ip': '10.0.1.10',
            'bk_cloud_id': 0
        }]
    )
    return success_result(res)


def test(request):
    username = request.user.username
    return success_result(username)


@try_exception('查询业务')
def search_business(request):
    client = get_client_by_request(request)
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
    }
    res = client.cc.search_business(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])


def get_all_users(request):
    client = get_client_by_request(request)
    res = client.cc.search_business()
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])


def add_exam(request):
    params = json.loads(request.body)
    params['exam_time'] = utc_to_datetime(params['exam_time'])
    obj = Exam.objects.create(**params)
    return success_result()


def get_exam_list(request):
    params = request.GET
    exam_list = Exam.objects.filter(**params)
    result_data = []
    for exam in exam_list:
        result_data.append({
            'id': exam.id,
            'site': exam.site,
            'name': exam.name,
            'type_display': '运维开发工程师' if  exam.type=='kf' else '运维自动化工程师',
            'type': exam.type,
            'exam_time': datetime_to_str(exam.exam_time),
            'status': '未开始' if exam.exam_time > now_time() else '已结束',
            'bk_biz_id': exam.bk_biz_id,
            'admin': exam.admin,
            'phone': exam.phone,
        })

    return success_result(result_data)


def delete_exam(request):
    params = json.loads(request.body)
    id = params['id']
    obj = Exam.objects.get(id=id)
    obj.delete()
    return success_result()


def download(request):
    # param = request.GET('id')
    d_path = os.path.join(settings.MEDIA_ROOT, 'exam.txt')
    file = open(d_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="exam"'
    return response


def student_import(request):
    table_data = [
        {
            'name': '张三',
            'department': 'd1',
            'score': 78,
            'mark': '错误好多'
        },
        {
            'name': '李四',
            'department': 'd2',
            'score': 88,
            'mark': ''
        },
        {
            'name': '王五',
            'department': 'd1',
            'score': 68,
            'mark': ''
        }
    ]
    xAxis = [{
            "type" : "category",
            "data" : ['d1', 'd2']
        }]
    series = [
        {
            "name": "通过",
            "type": "bar",
            "data": [1, 1]
        },
        {
            "name": "不通过",
            "type": "bar",
            "data": [1, 0]
        },
    ]
    # result_dict = {}
    # for data in table_data:
    #     if data['score'] > 80:
    #         data['result'] = '通过'
    #         department = data['department']
    #     else:
    #         data['result'] = '不通过'
    #         series[1]['data'].append(data['score'])
    #
    #     if data['department'] not in xAxis:
    #         xAxis.append(data['department'])

    result_data = {
        'table_data': table_data,
        'chart_data': {'xAxis': xAxis, 'series': series}
    }
    return success_result(result_data)
