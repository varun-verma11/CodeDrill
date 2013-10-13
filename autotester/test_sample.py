# input: program that prints first 5 numbers
# output: "1\r\n2\r\n3\r\n4\r\n5\r\n"
# it creates a subprocess that runs student_prog.py, which has code to print out numbers 1 to 5
# it gets this output from the subprocess and matches/tests it

class Tester:
    def test_one(expected_output):
        import subprocess
        student_output = subprocess.Popen(["python", "student_prog.py"], stdout=subprocess.PIPE).communicate()[0]
        ascii_output = student_output.decode('ascii')
        assert ascii_output == "1\r\n2\r\n3\r\n4\r\n5\r\n" #change with expected_output when we link everything
    
    

        
