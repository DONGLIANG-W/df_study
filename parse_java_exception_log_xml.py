import xml.etree.ElementTree as ET


def parse_java_exception_log_xml(log_xml_str):
    parsed_log = []
    root = ET.fromstring(log_xml_str)
    
    for exception_node in root.findall('.//{http://java.sun.com/xml/ns/javaee}exception'):
        current_exception = {}

        # Get the exception message
        message_node = exception_node.find('{http://java.sun.com/xml/ns/javaee}message')
        current_exception['message'] = message_node.text.strip() if message_node is not None else ''

        # Get the exception date
        date_node = exception_node.find('{http://java.sun.com/xml/ns/javaee}date')
        current_exception['message'] = date_node.text.strip() if date_node is not None else ''

        # Get the exception cause, if any
        cause_node = exception_node.find('{http://java.sun.com/xml/ns/javaee}cause')
        if cause_node is not None:
            cause_value_node = cause_node.find('{http://java.sun.com/xml/ns/javaee}value')
            if cause_value_node is not None:
                current_exception['cause'] = cause_value_node.text.strip()

        # Get the stack trace, if any
        stack_trace_node = exception_node.find('{http://java.sun.com/xml/ns/javaee}stack-trace')
        if stack_trace_node is not None:
            current_exception['stack_trace'] = [trace_line_node.text.strip() for trace_line_node in stack_trace_node.findall('{http://java.sun.com/xml/ns/javaee}trace-line')]

        parsed_log.append(current_exception)

    return parsed_log


if __name__ == '__main__':
	log_xml_str = """
	<log>
	  <exception>
		<message>java.lang.NullPointerException: Cannot invoke "java.lang.String.length()" because "str" is null</message>
		<stack-trace>
		  <trace-line>com.example.MyClass.myMethod(MyClass.java:23)</trace-line>
		  <trace-line>com.example.MyClass.main(MyClass.java:14)</trace-line>
		</stack-trace>
	  </exception>
	  <exception>
		<cause>
		  <value>java.lang.IllegalArgumentException: Input cannot be null</value>
		</cause>
		<message></message>
		<stack-trace>
		  <trace-line>com.example.MyClass.someMethod(MyClass.java:37)</trace-line>
		  <trace-line>com.example.MyClass.myMethod(MyClass.java:21)</trace-line>
		  <trace-line>...</trace-line>
		</stack-trace>
	  </exception>
	</log>
	"""

	parsed_log = parse_java_exception_log_xml(log_xml_str)
	print(parsed_log)

"""
print out 

[    {        'message': 'java.lang.NullPointerException: Cannot invoke "java.lang.String.length()" because "str" is null',        'stack_trace': [            'com.example.MyClass.myMethod(MyClass.java:23)',            'com.example.MyClass.main(MyClass.java:14)'        ]
    },
    {
        'cause': 'java.lang.IllegalArgumentException: Input cannot be null',
        'message': '',
        'stack_trace': [
            'com.example.MyClass.someMethod(MyClass.java:37)',
            'com.example.MyClass.myMethod(MyClass.java:21)',
            '...'
        ]
    }
]


"""
