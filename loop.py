import distance_to_camera as d


print "GOod idea"

instruction = d.check_image('images/two.jpg')

for x in range(0, 100):
	print "We're on time %d" % (x)
	instruction = d.check_image('images/two.jpg')
	
	
exit()
