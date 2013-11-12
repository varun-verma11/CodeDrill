from django.template import Context
from django.template.loader import get_template

def get_header_navbar(acc_type, name, title):
	header = get_template("header.html").render(
					Context( {
						'type': acc_type, 
						'name': name, 
						'title': title, 
						'loggedIn':True  } ))
	navbar = get_template("navbar.html").render(
                    Context( {
                            'loggedIn':True,
                            'type': acc_type,
                            'name': name
                        })
                )
	return {'header':header, 'navbar':navbar}