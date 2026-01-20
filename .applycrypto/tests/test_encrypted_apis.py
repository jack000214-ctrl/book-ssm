"""
암호화 API 테스트
자동 생성된 테스트 코드입니다.
"""

import json
import pytest
import requests
from pathlib import Path
from typing import Dict, Any


BASE_URL = "http://localhost:8000"


@pytest.fixture
def base_url():
    """API 테스트용 기본 URL"""
    return BASE_URL


@pytest.fixture
def test_data():
    """테스트 데이터 로드"""
    test_data_path = Path(__file__).parent / "test_data.json"
    with open(test_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('test_cases', [])


@pytest.fixture
def api_client(request):
    """HTTP client for API testing"""
    class APIClient:
        def __init__(self, base_url, test_item):
            self.base_url = base_url
            self.test_item = test_item
        
        def request(self, method, url, **kwargs):
            # 라벨 형식 URL을 지원합니다 (예: '"/api/x",method=RequestMethod.POST')
            url_str = str(url)
            m = None
            try:
                import re as _re
                m = _re.match(r'^"([^"]+)"(?:,\s*method=\s*RequestMethod\.([A-Z]+))?$', url_str)
            except Exception:
                m = None
            if m:
                path = m.group(1)
                if m.group(2):
                    method = m.group(2)
                full_url = f"{self.base_url}{path}"
            else:
                full_url = f"{self.base_url}{url}"
            
            # Request 정보 저장
            request_info = f"{method} {url}\n"
            if kwargs.get('json'):
                import json as json_module
                request_info += f"Body:\n{json_module.dumps(kwargs['json'], indent=2, ensure_ascii=False)}"
            else:
                request_info += "Body: (empty)"
            
            self.test_item.api_request_info = request_info
            
            try:
                response = requests.request(method, full_url, **kwargs)
                
                # Response 정보 저장
                response_info = f"Status: {response.status_code}\n"
                try:
                    response_info += f"Body:\n{json_module.dumps(response.json(), indent=2, ensure_ascii=False)}"
                except:
                    body_preview = response.text[:500] if response.text else "(empty)"
                    response_info += f"Body:\n{body_preview}"
                
                self.test_item.api_response_info = response_info
                
                return response
            except requests.exceptions.RequestException as e:
                pytest.fail(f"Request failed: {e}")
    
    return APIClient(BASE_URL, request.node)


class TestEmpController:
    """Test suite for EmpController"""
    
    def test_login_success(self, api_client, test_data):
        """
        Test: POST /api/login
        Description: Test login
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/login' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/login"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/api/login',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_login_invalid_input(self, api_client, test_data):
        """
        Test: POST /api/login with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/login' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/login"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/api/login',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /api/login")

    def test_get_user_info_success(self, api_client, test_data):
        """
        Test: POST /api/getUserInfo
        Description: Test getUserInfo
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/getUserInfo' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/getUserInfo"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/api/getUserInfo',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_user_info_invalid_input(self, api_client, test_data):
        """
        Test: POST /api/getUserInfo with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/getUserInfo' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/getUserInfo"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/api/getUserInfo',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /api/getUserInfo")

    def test_get_emps_success(self, api_client, test_data):
        """
        Test: GET /api/emps
        Description: Test getEmps
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_emps_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps")

    def test_init_success(self, api_client, test_data):
        """
        Test: GET /api/emps/init
        Description: Test init
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/init' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/init"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/init',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_init_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/init with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/init' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/init"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/init',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/init")

    def test_get_length_success(self, api_client, test_data):
        """
        Test: GET /api/emps/getLength
        Description: Test getLength
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/getLength' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/getLength"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/getLength',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_length_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/getLength with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/getLength' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/getLength"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/getLength',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/getLength")

    def test_del_emp_by_batch_success(self, api_client, test_data):
        """
        Test: GET /api/emps/delEmpByBatch
        Description: Test delEmpByBatch
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/delEmpByBatch' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/delEmpByBatch"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/delEmpByBatch',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_del_emp_by_batch_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/delEmpByBatch with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/delEmpByBatch' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/delEmpByBatch"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/delEmpByBatch',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/delEmpByBatch")

    def test_add_emp_by_get_success(self, api_client, test_data):
        """
        Test: GET /api/emps/addEmpByGet
        Description: Test addEmpByGet
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/addEmpByGet' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/addEmpByGet"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/addEmpByGet',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_add_emp_by_get_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/addEmpByGet with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/addEmpByGet' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/addEmpByGet"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/addEmpByGet',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/addEmpByGet")

    def test_add_emp_by_post_success(self, api_client, test_data):
        """
        Test: POST /api/emps/addEmpByPost
        Description: Test addEmpByPost
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/addEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/emps/addEmpByPost"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/api/emps/addEmpByPost',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_add_emp_by_post_invalid_input(self, api_client, test_data):
        """
        Test: POST /api/emps/addEmpByPost with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/addEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/emps/addEmpByPost"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/api/emps/addEmpByPost',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /api/emps/addEmpByPost")

    def test_edit_emp_by_post_success(self, api_client, test_data):
        """
        Test: POST /api/emps/editEmpByPost
        Description: Test editEmpByPost
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/editEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/emps/editEmpByPost"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/api/emps/editEmpByPost',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_edit_emp_by_post_invalid_input(self, api_client, test_data):
        """
        Test: POST /api/emps/editEmpByPost with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/editEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /api/emps/editEmpByPost"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/api/emps/editEmpByPost',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /api/emps/editEmpByPost")

    def test_query_success(self, api_client, test_data):
        """
        Test: GET /api/emps/query
        Description: Test query
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/query' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/query"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/query',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_query_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/query with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/query' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/query"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/query',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/query")

    def test_get_datas_success(self, api_client, test_data):
        """
        Test: GET /api/emps/getDatas
        Description: Test getDatas
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/getDatas' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/getDatas"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/api/emps/getDatas',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_datas_invalid_input(self, api_client, test_data):
        """
        Test: GET /api/emps/getDatas with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/api/emps/getDatas' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /api/emps/getDatas"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/api/emps/getDatas',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /api/emps/getDatas")


class TestEmployeeController:
    """Test suite for EmployeeController"""
    
    def test_get_emps_success(self, api_client, test_data):
        """
        Test: GET /emps
        Description: Test getEmps
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emps' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emps"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emps',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_emps_invalid_input(self, api_client, test_data):
        """
        Test: GET /emps with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emps' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emps"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emps',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emps")

    def test_get_length_success(self, api_client, test_data):
        """
        Test: GET /emps/getLength
        Description: Test getLength
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emps/getLength' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emps/getLength"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emps/getLength',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_length_invalid_input(self, api_client, test_data):
        """
        Test: GET /emps/getLength with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emps/getLength' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emps/getLength"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emps/getLength',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emps/getLength")

    def test_del_emp_success(self, api_client, test_data):
        """
        Test: GET /emp/delete
        Description: Test delEmp
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/delete' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/delete"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emp/delete',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_del_emp_invalid_input(self, api_client, test_data):
        """
        Test: GET /emp/delete with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/delete' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/delete"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emp/delete',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emp/delete")

    def test_del_emp_by_batch_success(self, api_client, test_data):
        """
        Test: GET /emp/delEmpByBatch
        Description: Test delEmpByBatch
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/delEmpByBatch' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/delEmpByBatch"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emp/delEmpByBatch',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_del_emp_by_batch_invalid_input(self, api_client, test_data):
        """
        Test: GET /emp/delEmpByBatch with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/delEmpByBatch' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/delEmpByBatch"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emp/delEmpByBatch',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emp/delEmpByBatch")

    def test_query_success(self, api_client, test_data):
        """
        Test: GET /emp/query
        Description: Test query
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/query' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/query"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emp/query',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_query_invalid_input(self, api_client, test_data):
        """
        Test: GET /emp/query with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/query' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/query"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emp/query',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emp/query")

    def test_add_emp_success(self, api_client, test_data):
        """
        Test: GET /emp/addEmpByGet
        Description: Test addEmp
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/addEmpByGet' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/addEmpByGet"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/emp/addEmpByGet',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_add_emp_invalid_input(self, api_client, test_data):
        """
        Test: GET /emp/addEmpByGet with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/addEmpByGet' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /emp/addEmpByGet"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/emp/addEmpByGet',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /emp/addEmpByGet")

    def test_add_emp_success(self, api_client, test_data):
        """
        Test: POST /emp/addEmpByPost
        Description: Test addEmp
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/addEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /emp/addEmpByPost"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/emp/addEmpByPost',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_add_emp_invalid_input(self, api_client, test_data):
        """
        Test: POST /emp/addEmpByPost with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/addEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /emp/addEmpByPost"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/emp/addEmpByPost',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /emp/addEmpByPost")

    def test_edit_success(self, api_client, test_data):
        """
        Test: POST /emp/editEmpByPost
        Description: Test edit
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/editEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /emp/editEmpByPost"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'POST',
            '/emp/editEmpByPost',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_edit_invalid_input(self, api_client, test_data):
        """
        Test: POST /emp/editEmpByPost with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/emp/editEmpByPost' and tc['api']['http_method'] == 'POST':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for POST /emp/editEmpByPost"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'POST',
                '/emp/editEmpByPost',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for POST /emp/editEmpByPost")

    def test_get_data_success(self, api_client, test_data):
        """
        Test: GET /data
        Description: Test getData
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/data' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /data"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/data',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_data_invalid_input(self, api_client, test_data):
        """
        Test: GET /data with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/data' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /data"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/data',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /data")

    def test_get_chart_success(self, api_client, test_data):
        """
        Test: GET /chart
        Description: Test getChart
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/chart' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /chart"
        
        # Get success scenario
        success_scenario = test_case['test_scenarios'][0]
        request_data = success_scenario['request']
        
        # Make request
        response = api_client.request(
            'GET',
            '/chart',
            json=request_data if request_data else None,
            timeout=10
        )
        
        # Verify response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text[:200]}"
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
            
            # Check for encrypted fields
            encrypted_fields = success_scenario.get('encrypted_fields', [])
            if encrypted_fields:
                print(f"Encrypted fields in response: {encrypted_fields}")
                # Verify encrypted fields are present
                for field in encrypted_fields:
                    print(f"  - {field} (should be encrypted)")
        except json.JSONDecodeError:
            pytest.fail(f"Response is not valid JSON: {response.text[:200]}")
    
    def test_get_chart_invalid_input(self, api_client, test_data):
        """
        Test: GET /chart with invalid input
        """
        # Find matching test data
        test_case = None
        for tc in test_data:
            if tc['api']['url'] == '/chart' and tc['api']['http_method'] == 'GET':
                test_case = tc
                break
        
        assert test_case is not None, f"Test case not found for GET /chart"
        
        # Get invalid scenario
        if len(test_case['test_scenarios']) > 1:
            invalid_scenario = test_case['test_scenarios'][1]
            request_data = invalid_scenario['request']
            
            # Make request
            response = api_client.request(
                'GET',
                '/chart',
                json=request_data if request_data else None,
                timeout=10
            )
            
            # Verify it handles invalid input gracefully (400, 401, 403, 422, or 500)
            assert response.status_code in [400, 401, 403, 422, 500], f"Invalid input should be rejected, got: {response.status_code}"
        else:
            pytest.skip(f"No invalid input scenario for GET /chart")


