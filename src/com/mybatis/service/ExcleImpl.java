package com.mybatis.service;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletOutputStream;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFCellStyle;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.HorizontalAlignment;

import com.mybatis.beans.Employee;

public class ExcleImpl {

	public ExcleImpl()
	{

	}
	public void export(List<Employee> list,String[] titles, ServletOutputStream out) throws Exception {
		try {
			// ��һ��������һ��workbook����Ӧһ��Excel�ļ�
			HSSFWorkbook workbook = new HSSFWorkbook();

			// �ڶ�������webbook������һ��sheet,��ӦExcel�ļ��е�sheet
			HSSFSheet hssfSheet = workbook.createSheet("sheet1");

			// ����������sheet�����ӱ�ͷ��0��,ע���ϰ汾poi��Excel����������������short

			HSSFRow row = hssfSheet.createRow(0);
			// ���Ĳ���������Ԫ�񣬲�����ֵ��ͷ ���ñ�ͷ����
			HSSFCellStyle hssfCellStyle = workbook.createCellStyle();

			// ������ʽ
			hssfCellStyle.setAlignment(HorizontalAlignment.CENTER);

			HSSFCell hssfCell = null;
			for (int i = 0; i < titles.length; i++) {
				hssfCell = row.createCell(i);// ��������0��ʼ
				hssfCell.setCellValue(titles[i]);// ����1
				hssfCell.setCellStyle(hssfCellStyle);// �о�����ʾ
			}

			// ���岽��д��ʵ������
//			Person person1 = new Person("1", "����", "123", "26");
//			Person person2 = new Person("2", "����", "123", "18");
//			Person person3 = new Person("3", "����", "123", "77");
//			Person person4 = new Person("4", "��С��", "123", "1");


			// �����Ұ�list�������ݿ���
//			ArrayList<Person> list = new ArrayList<Person>();
//			list.add(person1);
//			list.add(person2);
//			list.add(person3);
//			list.add(person4);

			for (int i = 0; i < list.size(); i++) {
				row = hssfSheet.createRow(i + 1);
				Employee employee = list.get(i);

				// ��������������Ԫ�񣬲�����ֵ
				Integer id = null;
				if (employee.getId() != null) {
					id = employee.getId();
				}
				String name = "";
				if (employee.getLastName() != null) {
					name = employee.getLastName();
				}
//				String sex = null;
//				if (employee.getSex().) {
//					String sex_str = employee.getSex();
//					if (sex_str == "1"||sex_str.equals("1"))
//						sex = "��";
//					else {
//						sex = "Ů";
//					}
//				}
				int sex = employee.getSex();
				String email = "";
				if (employee.getEmail() != null) {
					email = employee.getEmail();
				}
				row.createCell(0).setCellValue(id);
				row.createCell(1).setCellValue(name);
				row.createCell(2).setCellValue(sex);
				row.createCell(3).setCellValue(email);
			}

			// ���߲������ļ�������ͻ��������
			try {
				workbook.write(out);
				out.flush();
				out.close();

			} catch (Exception e) {
				e.printStackTrace();
			}
		} catch (Exception e) {
			e.printStackTrace();
			throw new Exception("������Ϣʧ�ܣ�");

		}
	}
}
