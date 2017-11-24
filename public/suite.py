# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 11:35
# @Author  : Leo_Peng
# @File    : suite.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
import unittest,time
from unittest.suite import _isnotsuite


class Suite(unittest.TestSuite):
    def run(self, result, debug=False):

        fail_count = 5
        class_num = 1
        topLevel = False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for test in self:
            case_num = 1
            if result.shouldStop:
                break
            success_flag = True
            while success_flag:
                if _isnotsuite(test):
                    self._tearDownPreviousClass(test, result)
                    self._handleModuleFixture(test, result)
                    self._handleClassSetUp(test, result)
                    result._previousTestClass = test.__class__
                    if (getattr(test.__class__, '_classSetupFailed', False) or
                            getattr(result, '_moduleSetUpFailed', False)):
                        if class_num > fail_count:
                            success_flag = False
                        else:
                            time.sleep(5)
                            result._previousTestClass = None
                            print ('%s Retrying init for %s times...' % (test.__class__, class_num))
                            class_num += 1
                        continue

                if not debug:
                    test(result)
                    print ('1')
                else:
                    test.debug()

                if result.result[-1][0] == 1 or result.result[-1][0] == 2:  # 1为Failed，2为Error
                    if case_num > fail_count:
                        success_flag = False
                    else:
                        print ('%s is Failed ! Retrying %s times...' % (test, case_num))
                        case_num += 1
                else:
                    success_flag = False

            if topLevel:
                self._tearDownPreviousClass(None, result)
                self._handleModuleTearDown(result)
                result._testRunEntered = False
        return result

    def removeTest(self, test):
        self._tests.remove(test)
