package com.mybatis.test;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

@Controller
public class TestController {

    @RequestMapping(value = "/api/hello", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> hello() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "success");
        response.put("message", "Hello from Spring MVC!");
        response.put("timestamp", System.currentTimeMillis());
        return response;
    }

    @RequestMapping(value = "/api/login", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> login(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("user")) {
            Map<String, Object> user = (Map<String, Object>) request.get("user");
            String name = user != null ? (String) user.get("name") : null;
            
            if (name != null && !name.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("message", "Login successful");
                response.put("user", request.get("user"));
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid user name");
                return response;
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/api/getUserInfo", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> getUserInfo(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("user")) {
            Map<String, Object> user = (Map<String, Object>) request.get("user");
            String name = user != null ? (String) user.get("name") : null;
            
            if (name != null && !name.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("data", request.get("user"));
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid user name");
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/api/emps", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getEmps() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> emps = new ArrayList<>();
        
        Map<String, Object> emp1 = new HashMap<>();
        emp1.put("id", 1);
        emp1.put("firstName", "John");
        emp1.put("lastName", "Doe");
        emps.add(emp1);
        
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", emps);
        return response;
    }

    @RequestMapping(value = "/api/emps/init", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> init() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("message", "Initialized");
        return response;
    }

    @RequestMapping(value = "/api/emps/getLength", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getLength() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("length", 10);
        return response;
    }

    @RequestMapping(value = "/api/emps/delEmpByBatch", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> delEmpByBatch() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("message", "Deleted");
        return response;
    }

    @RequestMapping(value = "/api/emps/addEmpByGet", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> addEmpByGet() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("message", "Employee added");
        return response;
    }

    @RequestMapping(value = "/api/emps/addEmpByPost", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> addEmpByPost(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("emp")) {
            Map<String, Object> emp = (Map<String, Object>) request.get("emp");
            String firstName = emp != null ? (String) emp.get("firstName") : null;
            
            if (firstName != null && !firstName.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("message", "Employee added");
                response.put("data", emp);
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid employee data");
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/api/emps/editEmpByPost", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> editEmpByPost(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("emp")) {
            Map<String, Object> emp = (Map<String, Object>) request.get("emp");
            String firstName = emp != null ? (String) emp.get("firstName") : null;
            
            if (firstName != null && !firstName.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("message", "Employee updated");
                response.put("data", emp);
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid employee data");
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/api/emps/query", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> query() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> results = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", results);
        return response;
    }

    @RequestMapping(value = "/api/emps/getDatas", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getDatas() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> datas = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", datas);
        return response;
    }

    @RequestMapping(value = "/emps", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getEmpsV2() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> emps = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", emps);
        return response;
    }

    @RequestMapping(value = "/emps/getLength", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getLengthV2() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("length", 5);
        return response;
    }

    @RequestMapping(value = "/emps/delEmp", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> delEmp() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("message", "Employee deleted");
        return response;
    }

    @RequestMapping(value = "/emps/delEmpByBatch", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> delEmpByBatchV2() {
        Map<String, Object> response = new HashMap<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("message", "Employees deleted");
        return response;
    }

    @RequestMapping(value = "/emps/query", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> queryV2() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> results = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", results);
        return response;
    }

    @RequestMapping(value = "/emps/addEmp", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> addEmp(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("emp")) {
            Map<String, Object> emp = (Map<String, Object>) request.get("emp");
            String firstName = emp != null ? (String) emp.get("firstName") : null;
            
            if (firstName != null && !firstName.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("message", "Employee added");
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid employee data");
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/emps/edit", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, Object> edit(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = new HashMap<>();
        
        if (request != null && request.containsKey("emp")) {
            Map<String, Object> emp = (Map<String, Object>) request.get("emp");
            String firstName = emp != null ? (String) emp.get("firstName") : null;
            
            if (firstName != null && !firstName.trim().isEmpty()) {
                response.put("code", 200);
                response.put("status", "success");
                response.put("message", "Employee updated");
            } else {
                response.put("code", 400);
                response.put("status", "error");
                response.put("message", "Invalid employee data");
            }
        } else {
            response.put("code", 400);
            response.put("status", "error");
            response.put("message", "Invalid request");
        }
        
        return response;
    }

    @RequestMapping(value = "/record/getData", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getData() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> data = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", data);
        return response;
    }

    @RequestMapping(value = "/record/getChart", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getChart() {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> chartData = new ArrayList<>();
        response.put("code", 200);
        response.put("status", "success");
        response.put("data", chartData);
        return response;
    }

    @RequestMapping(value = "/api/status", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> status() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "online");
        response.put("server", "Spring MVC");
        response.put("port", 8000);
        return response;
    }
}
