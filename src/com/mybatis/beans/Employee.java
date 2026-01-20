package com.mybatis.beans;

import java.io.Serializable;

public class Employee implements Serializable{

	/**
	 *
	 */
	private static final long serialVersionUID = 1L;
	private Integer id;
	private String lastName;
	private int sex;
	private String email;
	private String dayOfBirth;
	private String juminNumber;
	private Department dept;


	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}

	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getLastName() {
		// Return the stored name directly; decryption is handled in the service layer
		return lastName;
	}
	public void setLastName(String lastName) {
		// Store the name directly; encryption is handled in the service layer
		this.lastName = lastName;
	}


	public int getSex() {
		return sex;
	}
	public void setSex(int sex) {
		this.sex = sex;
	}

	public String getDayOfBirth() {
		// Return the stored birth date directly; decryption is handled in the service layer
		return dayOfBirth;
	}

	public void setDayOfBirth(String dayOfBirth) {
		// Store the birth date directly; encryption is handled in the service layer
		this.dayOfBirth = dayOfBirth;
	}

	public String getJuminNumber() {
		return juminNumber;
	}

	public void setJuminNumber(String juminNumber) {
		this.juminNumber = juminNumber;
	}

	@Override
	public String toString() {
		return "Employee [id=" + id + ", lastName=" + lastName + ", sex=" + sex + ", email=" + email + ", dayOfBirth=" + dayOfBirth + ", juminNumber=" + juminNumber + ", dept=" + dept
				+ "]";
	}
	public Employee(Integer id, String lastName, int sex, String email, String dayOfBirth, String juminNumber, Department dept) {
		super();
		this.id = id;
		this.lastName = lastName;
		this.sex = sex;
		this.email = email;
		this.dayOfBirth = dayOfBirth;
		this.juminNumber = juminNumber;
		this.dept = dept;
	}
	public Department getDept() {
		return dept;
	}
	public void setDept(Department dept) {
		this.dept = dept;
	}
	public Employee(Integer id, String lastName, int sex, String email, String dayOfBirth, String juminNumber) {
		super();
		this.id = id;
		this.lastName = lastName;
		this.sex = sex;
		this.email = email;
		this.dayOfBirth = dayOfBirth;
		this.juminNumber = juminNumber;
	}
	public Employee() {
		super();
	}

}