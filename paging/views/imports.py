import math

from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.db.models import Q

from paging.models import *
