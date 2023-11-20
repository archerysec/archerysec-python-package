#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @FileName      : example
# @Time          : 2023-11-20 10:05:09
# @Author        : wensaus
# @description   :
"""

from archeryPy import api

# Set Archery url
host = 'https://127.0.0.1:8080'

# Setup archery connection
archery = api.ArcheryRestApi(host)

# 获取token
authenticate = archery.archery_auth('admin', 'admin123')

# 刷新token
archery.archery_auth_refresh(authenticate['refresh'])

# 验证token
archery.archery_auth_verify(authenticate['token'])

# 列出所有SQL上线工单（过滤，分页）
archery.archery_workflow_list

# 提交一条SQL上线工单
archery.archery_workflow_submit

# 审核工单
archery.archery_workflow_audit

# 列出指定用户待审核清单（过滤，分页）
archery.archery_workflow_auditlist

# 执行一条工单
archery.archery_workflow_execute

# 获取某个工单的日志（分页）
archery.archery_workflow_log

# 对提供的SQL进行语法检查
archery.archery_workflow_sqlcheck
