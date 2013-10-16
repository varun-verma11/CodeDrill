#!/usr/bin/env python

from django.http import HttpResponse


def get_grades_page(request):
	student_id = "vv311"
	student_name = __get_student_name(student_id)

	page = "<!DOCTYPE html>\n <html lang=\"en\">"
	page += __get_page_header(student_name)
	page += __get_page_body(student_id)
	page += "</html>"
	return HttpResponse(page)


def __get_student_grades(student_id):
	return [["Variable Assignment", "Addition", 40] ,
			["Conditionals", "If-then-else", 70]
			]

def __get_student_name(student_id):
	if student_id=="vv311":
		return "Varun Verma"
	if student_id=="mmj11":
		return "Mihai Jiplea"

def __get_page_header(student_name):
	header = " <head>\n <title>" + student_name + " Grades</title>"
	header += '''
		 	<meta charset="utf-8">
		 	<meta name="viewport" content="width=device-width, initial-scale=1.0">	
		 	<link href="css/bootstrap.min.css" rel="stylesheet">
		  	<link href="css/bootstrap-responsive.min.css" rel="stylesheet">
			<link href="css/style.css" rel="stylesheet">

			<script type="text/javascript" src="js/jquery.min.js"></script>
			<script type="text/javascript" src="js/bootstrap.min.js"></script>
			<script type="text/javascript" src="js/scripts.js"></script>
	 	'''
	header += "\n</head> \n"
	return header

def __get_foot_page_navigation_menu():
	return '''
				<div class="pagination">
			        <ul>
			          <li><a href="#">Last term</a></li>
			          <li><a href="#">1</a></li>
			          <li><a href="#">2</a></li>
			          <li><a href="#">3</a></li>
			          <li><a href="#">4</a></li>
			          <li><a href="#">5</a></li>
			          <li><a href="#">Next term</a></li>
			        </ul>
			    </div>
			'''

def __get_student_grade_table(student_id):
	table = "<table class=\"table\">"
	table += '''
				<thead>
		            <tr>
		              <th>
		                #
		              </th>
		              <th>
		                Chapter
		              </th>
		              <th>
		                Problem name
		              </th>
		              <th>
		                Grade
		              </th>
		            </tr>
		        </thead>
			 '''
	table += "<tbody>"
	i = 1
	for result in __get_student_grades(student_id):
		table += "<tr>"
		table += "<td>" + str(i) + "</td>"
		i += 1
		for value in result:
			table += "<td>" + str(value) + "</td>"
		table += "</tr>"

	table += "</tbody>"
	table += "</table>\n"
	return table;

def __get_page_body(student_id):
	body = "<body>\n"
	body += "<div class=\"container-fluid\">"
	body += '''
				<div class="row-fluid">
			    <h3>
			    A Framework for Setting and Assessing Programming Exercises </h3>
			    <div class="span3">
			      <div id="menu">
			        <script>
			           $(document).ready(function () {
				            $('ul.menu-list').toggle();
				            $('label.tree-toggler').click(function () {
				             $(this).parent().children('ul.tree').toggle(200);
				           });
			          	});
			         </script>
			        <ul class="nav nav-list">
			          <li class="nav-header"> Menu </li>
			          <li>
			            <a href="index.html">Code</a>
			            <ul class="nav nav-list">
			              <li>
			                <label class="tree-toggler nav-header">Variable Assignment</label>
			                <ul class="nav nav-list tree menu-list">
			                  <li><a href="#">Subtraction</a></li>
			                </ul>
			              </li>
			            </ul>
			            <ul class="nav nav-list">
			              <li>
			                <label class="tree-toggler nav-header">Conditionals</label>
			                <ul class="nav nav-list tree menu-list">
			                  <li><a href="#">If</a></li>
			                </ul>
			              </li>
			            </ul>
			            <ul class="nav nav-list">
			              <li>
			                <label class="tree-toggler nav-header">For loop</label>
			                <ul class="nav nav-list tree menu-list">
			                  <li><a href="#">Print 10 numbers</a></li>
			                  <li><a href="#">Sum</a></li>
			                </ul>
			              </li>
			            </ul>
			          </li>
			          <li class="active">
			          <a href="#">Grades</a>
			          </li>
			        </ul>
			      </div>
			    </div>
			'''
	body += "</div>" #closing tag for the container-fluid class

	body += '''
			 <div class="span6">
			    <div id="page-content">
			      	<div class="well">
			'''

	body += __get_student_grade_table(student_id)
	body += "</div>"
	body += __get_foot_page_navigation_menu()
	body += '''
				 		 </div>
			 		 </div>
				</div>
			</body>
			'''

	return body

