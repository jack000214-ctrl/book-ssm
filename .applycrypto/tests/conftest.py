"""
pytest configuration
"""
import json
import os
from pathlib import Path
import pytest


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--config",
        action="store",
        default="config.json",
        help="Path to config.json file"
    )


def pytest_configure(config):
    """Load configuration from config.json"""
    config_path = config.getoption("--config")
    
    # 절대 경로가 아니면 프로젝트 루트 기준으로 변환
    if not Path(config_path).is_absolute():
        config_path = Path(__file__).parent.parent / config_path
    
    # config.json 로드
    api_base_url = None
    if Path(config_path).exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                api_base_url = config_data.get('API_BASE_URL')
        except Exception as e:
            print(f"Warning: Failed to load config from {config_path}: {e}")
    
    # 환경 변수 우선, 그 다음 config.json, 마지막으로 기본값
    if 'API_BASE_URL' in os.environ:
        api_base_url = os.environ['API_BASE_URL']
    elif api_base_url is None:
        api_base_url = "http://localhost:8080"
    
    # pytest config에 저장
    config.api_base_url = api_base_url


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    테스트 리포트에 상세 정보 추가
    HTML 리포트에 endpoint, method, request, response 정보 표시
    """
    outcome = yield
    report = outcome.get_result()
    
    # 테스트 실행 단계(call)에서만 extra 정보 추가
    if report.when == "call":
        try:
            from pytest_html import extras
            
            extra_info = []
            
            # docstring에서 endpoint와 method 추출
            if item.function.__doc__:
                doc = item.function.__doc__.strip()
                if "Test:" in doc:
                    test_line = [line for line in doc.split('\n') if 'Test:' in line][0]
                    parts = test_line.replace('Test:', '').strip().split()
                    if len(parts) >= 2:
                        method = parts[0]
                        endpoint = parts[1]
                        
                        extra_info.append(extras.html(
                            f'<div style="margin: 10px 0; padding: 10px; background: #f5f5f5; border-left: 4px solid #2196F3;">'
                            f'<strong>Endpoint:</strong> <code>{endpoint}</code><br>'
                            f'<strong>Method:</strong> <code>{method}</code>'
                            f'</div>'
                        ))
            
            # request/response 정보 추가
            if hasattr(item, 'api_request_info'):
                req = item.api_request_info
                extra_info.append(extras.html(
                    f'<div style="margin: 10px 0; padding: 10px; background: #fff3e0; border-left: 4px solid #ff9800;">'
                    f'<strong>Request:</strong><pre style="margin: 5px 0; padding: 10px; background: white; overflow: auto;">{req}</pre>'
                    f'</div>'
                ))
            
            if hasattr(item, 'api_response_info'):
                res = item.api_response_info
                extra_info.append(extras.html(
                    f'<div style="margin: 10px 0; padding: 10px; background: #e8f5e9; border-left: 4px solid #4caf50;">'
                    f'<strong>Response:</strong><pre style="margin: 5px 0; padding: 10px; background: white; overflow: auto;">{res}</pre>'
                    f'</div>'
                ))
            
            if extra_info:
                report.extras = extra_info
                
        except ImportError:
            # pytest-html이 없으면 무시
            pass
