import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Lấy kết quả test cho từng giai đoạn setup/call/teardown
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)