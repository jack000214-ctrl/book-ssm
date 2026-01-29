package com.mybatis.dao;

import java.lang.reflect.Field;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;

import org.apache.commons.lang3.StringUtils;
import org.apache.ibatis.executor.parameter.ParameterHandler;
import org.apache.ibatis.executor.resultset.DefaultResultSetHandler;
import org.apache.ibatis.executor.resultset.ResultSetHandler;
import org.apache.ibatis.plugin.Interceptor;
import org.apache.ibatis.plugin.Intercepts;
import org.apache.ibatis.plugin.Invocation;
import org.apache.ibatis.plugin.Plugin;
import org.apache.ibatis.plugin.Signature;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.util.ReflectionUtils;

import com.mybatis.beans.MapParam;
import java.sql.Statement;

@Intercepts({@Signature(method="handleResultSets",type = ResultSetHandler.class, args={ Statement.class })})
public class MapInterceptor implements Interceptor {
	// Logger
	private static final Logger logger = LoggerFactory.getLogger(MapInterceptor.class);
	@Override
	public Object intercept(Invocation invocation) throws Throwable {
		// TODO Auto-generated method stub

		// Get the target object
		Object target = invocation.getTarget();
		if (target instanceof DefaultResultSetHandler) {
			DefaultResultSetHandler resultSetHandler = (DefaultResultSetHandler) target;
			// Use reflection to get parameter handler
			ParameterHandler parameterHandler = reflect(resultSetHandler);
			Object parameterObj = parameterHandler.getParameterObject();
			// If parameter is MapParam, execute custom logic
			if (parameterObj instanceof MapParam) {
				MapParam mapParam = (MapParam) parameterObj;
				// Get current statement
				Statement stmt = (Statement) invocation.getArgs()[0];
				// Process mapParam to return result
				return handleResultSet(stmt.getResultSet(), mapParam);
			}
		}
		return invocation.proceed();
	}

	@Override
	public Object plugin(Object target) {
		// TODO Auto-generated method stub
		return Plugin.wrap(target, this);
	}
	
	@Override
	public void setProperties(Properties arg0) {
		// TODO Auto-generated method stub
		
	} 
	private Object handleResultSet(ResultSet resultSet, MapParam mapParam) {
		if (null != resultSet) {
			// Get key field name
			String keyFieldName = (String) mapParam.get(MapParam.KEY_FIELD);
			// Get value field name
			String valueFieldName = (String) mapParam.get(MapParam.VALUE_FIELD);
			// Value class
			String valueClass = (String) mapParam.get(MapParam.VALUE_CLASS);
			List<Object> resultList = new ArrayList<Object>();
			Map<Object, Object> map = new HashMap<Object, Object>();
			try {
				while (resultSet.next()) {
					Object key = resultSet.getObject(keyFieldName);
					Object value;
					// Convert value based on class
					if (StringUtils.equals(valueClass, MapParam.ValueClass.INTEGER.getCode())) {
						value = resultSet.getInt(valueFieldName);
					} else if (StringUtils.equals(valueClass, MapParam.ValueClass.BIG_DECIMAL.getCode())) {
						value = resultSet.getBigDecimal(valueFieldName);
					} else {
						value = resultSet.getObject(valueFieldName);
					}
					map.put(key, value);
				}
			} catch (SQLException e) {
				logger.error("map interceptor conversion exception: {}", e.getMessage());
			} finally { // Close result set
				closeResultSet(resultSet);
			}
			resultList.add(map);
			return resultList;
		}
		return null;
	}

	private void closeResultSet(ResultSet resultSet) {
		try {
			if (resultSet != null) {
				resultSet.close();
			}
		} catch (SQLException e) {
			logger.error("Close result set exception, {}", e.getMessage());
		}
	}

	private ParameterHandler reflect(DefaultResultSetHandler resultSetHandler) {
		Field field = ReflectionUtils.findField(DefaultResultSetHandler.class, "parameterHandler");
		field.setAccessible(true);
		Object value = null;
		try {
			value = field.get(resultSetHandler);
		} catch (Exception e) {
			logger.error("Default result set handler reflection exception: {}", e.getMessage());
		}
		return (ParameterHandler) value;
	}

}


