def test_1():
	print("1")

def test_2():
	assert False, "test doesn't pass"
	
if __name__=="__main__":
	test_1()
	test_2()
