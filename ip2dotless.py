import sys
def ip2dotless(IP):
	ip_sections = [int(i) for i in IP.split(".")]
	a = ip_sections[0]
	b = ip_sections[1]
	c = ip_sections[2]
	d = ip_sections[3]
	step_1 = a * 256
	step_2 = step_1 + b
	step_3 = step_2 * 256
	step_4 = step_3 + c
	step_5 = step_4 * 256
	step_6 = step_5 + d
	print(f"Your dotless IP is: {step_6}")
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Invalid usage!\nExample: python ip2dotless.py 127.0.0.1")
		sys.exit()
	else:
		IP = sys.argv[1]
		ip_check = [int(i) for i in IP.split(".")]
		if len(ip_check) != 4:
			print("Invalid IP!\nMake sure you entered it correctly")
		else:
			ip2dotless(f"{sys.argv[1]}")
