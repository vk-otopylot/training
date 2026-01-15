from bs4 import BeautifulSoup

# Reading from file

# with open('books.xml', 'r') as file:
#     data = file.read()
#
# bs_data = BeautifulSoup(data, 'xml')
# b_title = bs_data.find_all('title')
# b_name = bs_data.find('author', {'cat': 'old'})
# print(b_name.get('test'))


# Writing to file

# with open('books.xml', 'r') as file:
#     data = file.read()
#
# bs_data = BeautifulSoup(data, 'xml')
#
# for tag in bs_data.find_all('author', {'cat': 'old'}):
#     tag['test'] = 'WHAT !!'
#
# print(bs_data.prettify())


# Using ElementTree

# Reading from file

import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print(root[0][0].text)

# Writing to file

# root = ET.Element('Books')
# book = ET.SubElement(root, 'book')
# title = ET.SubElement(book, 'title')
# author = ET.SubElement(book, 'author')
# book.set('id', '101')
# title.text = 'Never Give Up'
# author.text = 'vivek k'
#
# xml_data = ET.tostring(root)
#
# with open('b_data.xml', 'wb') as file:
#     file.write(xml_data)


# Write a Python program to create students.xml with 3 students.
#
# import xml.etree.ElementTree as ET
#
# root = ET.Element('students')
# stu1 = ET.SubElement(root,'student')
# stu2 = ET.SubElement(root,'student')
# stu3 = ET.SubElement(root,'student')
# stu1.set('id', '101')
# stu2.set('id', '102')
# stu3.set('id', '103')
# stu1.text = 'student1_data'
# stu2.text = 'student2_data'
# stu3.text = 'student3_data'
#
# tree = ET.ElementTree(root)
# tree.write("students.xml", encoding="utf-8", xml_declaration=True)
#


# Add a new element to an existing XML file using Python.

# data = ET.parse('students.xml')
# root = data.getroot()
# main = root[0]
# ele = ET.SubElement(main, 'name')
# ele.text = 'vivek kakadia'
#
# data.write('students.xml', encoding="utf-8", xml_declaration=True)


# Read an XML file and print all tag names.

data = ET.parse('books.xml')
root = data.getroot()
for val in root.iter():
    print(val.tag)