package com.mybatis.service;

import java.util.List;
import java.util.Map;

import com.mybatis.beans.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mybatis.beans.Department;
import com.mybatis.beans.Employee;
import com.mybatis.dao.DepartmentMapper;
import com.mybatis.dao.EmployeeMapper;

import k_sign.CryptoService;

@Service
public class EmployeeService {

	@Autowired
	private EmployeeMapper employeeMapper;

	@Autowired
	private DepartmentMapper deptMapper;
	public List<Employee> getEmps(){
		List<Employee> employees = employeeMapper.getEmps();
		for (Employee employee : employees) {
			// Decrypt JUMIN
			employee.setJuminNumber(k_sign.CryptoService.decrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
			// Decrypt Name
			employee.setLastName(k_sign.CryptoService.decrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
			// Decrypt Birth Date
			employee.setDayOfBirth(k_sign.CryptoService.decrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));
		}
		return employees;
	}

	public void delete(Integer id) {
		// TODO Auto-generated method stub
		employeeMapper.deleteEmpById(id);

	}

	public void update(Employee employee)
	{
		// Encrypt JUMIN
		employee.setJuminNumber(k_sign.CryptoService.encrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
		// Encrypt Name
		employee.setLastName(k_sign.CryptoService.encrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
		// Encrypt Birth Date
		employee.setDayOfBirth(k_sign.CryptoService.encrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));

		employeeMapper.updateEmp(employee);
	}
	public void save(Employee employee) {
		// TODO Auto-generated method stub
		Department dept = deptMapper.getDeptById(employee.getDept().getId());
		employee.setDept(dept);
		// Encrypt JUMIN
		employee.setJuminNumber(k_sign.CryptoService.encrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
		// Encrypt Name
		employee.setLastName(k_sign.CryptoService.encrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
		// Encrypt Birth Date
		employee.setDayOfBirth(k_sign.CryptoService.encrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));

		employeeMapper.addEmp(employee);

	}

	public Employee getEmpById(Integer id) {
		Employee employee = employeeMapper.getEmpById(id);
		// Decrypt JUMIN
		employee.setJuminNumber(k_sign.CryptoService.decrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
		// Decrypt Name
		employee.setLastName(k_sign.CryptoService.decrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
		// Decrypt Birth Date
		employee.setDayOfBirth(k_sign.CryptoService.decrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));
		return employee;
	}

	public List<Employee> getEmpsByPage(Integer pageIndex,Integer size) {
		List<Employee> employees = employeeMapper.getEmpsByPage(pageIndex,size);
		for (Employee employee : employees) {
			// Decrypt JUMIN
			employee.setJuminNumber(k_sign.CryptoService.decrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
			// Decrypt Name
			employee.setLastName(k_sign.CryptoService.decrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
			// Decrypt Birth Date
			employee.setDayOfBirth(k_sign.CryptoService.decrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));
		}
		return employees;
	}
	public int getLength()
	{
		return employeeMapper.getLength();
	}

	public List<Employee>  query(String condition) {
		List<Employee> employees = employeeMapper.query(condition);
		for (Employee employee : employees) {
			// Decrypt JUMIN
			employee.setJuminNumber(k_sign.CryptoService.decrypt(employee.getJuminNumber(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
			// Decrypt Name
			employee.setLastName(k_sign.CryptoService.decrypt(employee.getLastName(), k_sign.CryptoService.P20, K_SIGN_NAME));
			// Decrypt Birth Date
			employee.setDayOfBirth(k_sign.CryptoService.decrypt(employee.getDayOfBirth(), k_sign.CryptoService.P30, K_SIGN_DOB));
		}
		return employees;
	}

	public List<Map<String, Object>> getDatas() {
		// TODO Auto-generated method stub
		List<Map<String, Object>> data = employeeMapper.getDatas();
		for (Map<String, Object> map : data) {
			// Decrypt JUMIN
			map.put("juminNumber", k_sign.CryptoService.decrypt(map.get("juminNumber").toString(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
			// Decrypt Name if present
			if (map.containsKey("lastName")) {
				map.put("lastName", k_sign.CryptoService.decrypt(map.get("lastName").toString(), k_sign.CryptoService.P20, K_SIGN_NAME));
			}
			// Decrypt Birth Date if present
			if (map.containsKey("dayOfBirth")) {
				map.put("dayOfBirth", k_sign.CryptoService.decrypt(map.get("dayOfBirth").toString(), k_sign.CryptoService.P30, K_SIGN_DOB));
			}
		}
		return data;
	}
	public List<Map<String, Object>> getPer() {
		// TODO Auto-generated method stub
		List<Map<String, Object>> per = employeeMapper.getPer();
		for (Map<String, Object> map : per) {
			// Decrypt JUMIN
			map.put("juminNumber", k_sign.CryptoService.decrypt(map.get("juminNumber").toString(), k_sign.CryptoService.P10, K_SIGN_JUMIN));
			// Decrypt Name if present
			if (map.containsKey("lastName")) {
				map.put("lastName", k_sign.CryptoService.decrypt(map.get("lastName").toString(), k_sign.CryptoService.P20, K_SIGN_NAME));
			}
			// Decrypt Birth Date if present
			if (map.containsKey("dayOfBirth")) {
				map.put("dayOfBirth", k_sign.CryptoService.decrypt(map.get("dayOfBirth").toString(), k_sign.CryptoService.P30, K_SIGN_DOB));
			}
		}
		return per;
	}

	public User login(User user) {
		User u = employeeMapper.login(user.getUserName(),user.getPassword());
		return u;
	}
	public User getUserInfo(User user) {
		User u = employeeMapper.getUserInfo(user.getUserName(),user.getPassword());
		return u;
	}
}