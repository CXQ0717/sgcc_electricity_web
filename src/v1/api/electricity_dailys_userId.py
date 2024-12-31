# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from models import electricity


class ElectricityDailysUserid(Resource):

    def get(self, userId):
        result = electricity.get_user_dailys(userId)
        return result, 200, None