import allure
import pytest


class Test01():
    @pytest.mark.parametrize("a", [1, 2, 3])
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('我是测试步骤001')
    def test01(self, a):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert a != 2

    def test02(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        assert 1