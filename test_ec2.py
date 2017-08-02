#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mock import Mock
import os
import pytest
import start_stop_ec2


def test_func(monkeypatch):
    cwd = Mock(return_value='/')
    monkeypatch.setattr(os, 'getcwd', cwd)
    assert os.getcwd == '/'
