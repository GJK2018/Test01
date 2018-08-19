import allure
import pytest


class Test01():
    @pytest.mark.parametrize("a", [1, 2, 3])
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert a != 2