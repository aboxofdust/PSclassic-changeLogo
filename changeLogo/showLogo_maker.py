#!/usr/bin/env python

import binascii
import os
import shutil
from hashlib import sha1
import re
import sys

changesMade = False

# imageLocs = {'58': {'y': 769734, 'x': 757352}, '30': {'y': 407434, 'x': 394264}, '54': {'y': 719604, 'x': 707080}, '42': {'y': 565118, 'x': 552264}, '48': {'y': 643010, 'x': 630176}, '45': {'y': 604198, 'x': 591192}, '43': {'y': 578198, 'x': 565128}, '60': {'y': 794442, 'x': 782144}, '61': {'y': 821608, 'x': 794456}, '62': {'y': 850408, 'x': 821616}, '57': {'y': 757344, 'x': 744752}, '64': {'y': 908822, 'x': 879264}, '49': {'y': 656068, 'x': 643024}, '66': {'y': 968586, 'x': 939032}, '67': {'y': 998680, 'x': 968600}, '68': {'y': 1028942, 'x': 998688}, '69': {'y': 1059096, 'x': 1028952}, '52': {'y': 694326, 'x': 681608}, '53': {'y': 707072, 'x': 694336}, '02': {'y': 44144, 'x': 32016}, '03': {'y': 56006, 'x': 44152}, '26': {'y': 354612, 'x': 340960}, '01': {'y': 32002, 'x': 20648}, '06': {'y': 93700, 'x': 81320}, '07': {'y': 106078, 'x': 93712}, '04': {'y': 68172, 'x': 56016}, '05': {'y': 81310, 'x': 68184}, '46': {'y': 617178, 'x': 604208}, '47': {'y': 630162, 'x': 617192}, '08': {'y': 119664, 'x': 106088}, '09': {'y': 132000, 'x': 119672}, '28': {'y': 380870, 'x': 367744}, '29': {'y': 394256, 'x': 380880}, '40': {'y': 539160, 'x': 526104}, '41': {'y': 552252, 'x': 539168}, '14': {'y': 196538, 'x': 182840}, '59': {'y': 782132, 'x': 769744}, '51': {'y': 681594, 'x': 668744}, '24': {'y': 327960, 'x': 314880}, '56': {'y': 744740, 'x': 732304}, 'bg': {'y': 20636, 'x': 18344}, '25': {'y': 340952, 'x': 327968}, '39': {'y': 526094, 'x': 513112}, '65': {'y': 939022, 'x': 908832}, '27': {'y': 367736, 'x': 354624}, '71': {'y': 1120384, 'x': 1089712}, '70': {'y': 1089698, 'x': 1059104}, '20': {'y': 275252, 'x': 261584}, '38': {'y': 513102, 'x': 499960}, '21': {'y': 288308, 'x': 275264}, '11': {'y': 157744, 'x': 144384}, '10': {'y': 144376, 'x': 132008}, '13': {'y': 182830, 'x': 170272}, '12': {'y': 170258, 'x': 157752}, '15': {'y': 209434, 'x': 196552}, '22': {'y': 301424, 'x': 288320}, '17': {'y': 235732, 'x': 222112}, '16': {'y': 222104, 'x': 209448}, '19': {'y': 261576, 'x': 248704}, '18': {'y': 248690, 'x': 235744}, '31': {'y': 420630, 'x': 407448}, '23': {'y': 314866, 'x': 301432}, '37': {'y': 499952, 'x': 486880}, '36': {'y': 486870, 'x': 473752}, '35': {'y': 473744, 'x': 460312}, '34': {'y': 460302, 'x': 447296}, '33': {'y': 447282, 'x': 434128}, '55': {'y': 732290, 'x': 719616}, '63': {'y': 879252, 'x': 850416}, '32': {'y': 434116, 'x': 420640}, '44': {'y': 591180, 'x': 578208}, '50': {'y': 668730, 'x': 656080}}
imageLocs = {'58': {'y': 769734, 'x': 757352, 'sha1': '8e4968727537238923548831a77705785071c9fd'}, '30': {'y': 407434, 'x': 394264, 'sha1': '24e664bbc415c39c55fd2d0387bdec19b0a9cec3'}, '54': {'y': 719604, 'x': 707080, 'sha1': '5830729cc6e5b35e27ab073e887f4448a54a4135'}, '42': {'y': 565118, 'x': 552264, 'sha1': '3917eaae6e8218309b50ecb9a8bd33b23fd4b60f'}, '48': {'y': 643010, 'x': 630176, 'sha1': '809230207ca1c33576dfce366ac4b42b4fc396a7'}, '45': {'y': 604198, 'x': 591192, 'sha1': 'a10a36daf92e355e5d3833e7f9cea8a96e668d68'}, '43': {'y': 578198, 'x': 565128, 'sha1': 'bd01ece7d36f0da431950b4f24b3ad0aa9ec7e04'}, '60': {'y': 794442, 'x': 782144, 'sha1': '4a099c8d2d28c6acee10128949323e25769dfd53'}, '61': {'y': 821608, 'x': 794456, 'sha1': '08317281cfb795b493803ecc522c4d5b1ef42faa'}, '62': {'y': 850408, 'x': 821616, 'sha1': 'bccc0b68a6ba74c9da428a2627bef59c99a12a02'}, '57': {'y': 757344, 'x': 744752, 'sha1': 'a89a5bb33d07e8fdb4500b3cf1ca145b5760ee77'}, '64': {'y': 908822, 'x': 879264, 'sha1': '5851fead0f0f7bdb473c8378bd413095f6c169f8'}, '49': {'y': 656068, 'x': 643024, 'sha1': 'b8e4a4d37b44116a591db843844368c7b1f74aa1'}, '66': {'y': 968586, 'x': 939032, 'sha1': '33bb06727189788b0b056789bb74b0f970c686b7'}, '67': {'y': 998680, 'x': 968600, 'sha1': '0bfeed6d39c16ffad0f2a266b7a140e7f0e4aa4b'}, '68': {'y': 1028942, 'x': 998688, 'sha1': 'a3be5500ac9c9168950cb6f1d874aaad3b671a71'}, '69': {'y': 1059096, 'x': 1028952, 'sha1': '8b28e35d57f52edd9e29e52592bc65eb8c638f07'}, '52': {'y': 694326, 'x': 681608, 'sha1': '9a593e6129bac4c1a7a2152797b607f3dcaf36e3'}, '53': {'y': 707072, 'x': 694336, 'sha1': '6d515a6ac68768459e203b602c93f8444d26cbe1'}, '02': {'y': 44144, 'x': 32016, 'sha1': 'eb43e123e85e0d4b1214c5ab7a354d2627a510fd'}, '03': {'y': 56006, 'x': 44152, 'sha1': 'ac95e8c9d01a445c18684348afefad519b587836'}, '26': {'y': 354612, 'x': 340960, 'sha1': '5331f64259f269e36fb3bb3801d28615030fef5b'}, '01': {'y': 32002, 'x': 20648, 'sha1': '6046fa4b6f6adafbbe4b10d6ca62e68e55fface8'}, '06': {'y': 93700, 'x': 81320, 'sha1': 'a40cfa93e1e13d092ee482d9841f2ff282371947'}, '07': {'y': 106078, 'x': 93712, 'sha1': '829e83bdd2afd3676b4b5c22b9cde7eaf51de988'}, '04': {'y': 68172, 'x': 56016, 'sha1': 'b3d4989a3f93971571e926b5f6d524a184fca3b4'}, '05': {'y': 81310, 'x': 68184, 'sha1': 'b4c3bd4dbff2cf5cbbfc8f3c4508e798ea76248e'}, '46': {'y': 617178, 'x': 604208, 'sha1': 'ae14274adb173d51b2562d052d48f4d5673758fb'}, '47': {'y': 630162, 'x': 617192, 'sha1': 'bd4b6aff13031aefdceb898747d0f558df3d3467'}, '08': {'y': 119664, 'x': 106088, 'sha1': 'df37a53c5d7e8d4a624fd9f38085d5a48559afd1'}, '09': {'y': 132000, 'x': 119672, 'sha1': '50c9c9228af98436d0af2f7d8d8e42b3e60d9346'}, '28': {'y': 380870, 'x': 367744, 'sha1': '0d2e7e7e64eebec16e5c55b650fb12ad95ea21cd'}, '29': {'y': 394256, 'x': 380880, 'sha1': '8412d5d7351a116b5a553b2ff81ae949f8c7cc67'}, '40': {'y': 539160, 'x': 526104, 'sha1': 'ebb711f747cf587564cc0b59826814bcf524cdd4'}, '41': {'y': 552252, 'x': 539168, 'sha1': '99a38f5c0306cbe172ab1e4223dfb256be39086d'}, '14': {'y': 196538, 'x': 182840, 'sha1': 'a877fb4953d86cefc64a08f4129848d37b07301d'}, '59': {'y': 782132, 'x': 769744, 'sha1': 'a0bfeb7db54e7ff5a2e8c79d2b8fd654a121d49f'}, '51': {'y': 681594, 'x': 668744, 'sha1': '71dff0816db322ceb33ce5aee467b49ab60052e5'}, '24': {'y': 327960, 'x': 314880, 'sha1': '868c17de21157f5774bff39e67a81db4773b5ce9'}, '56': {'y': 744740, 'x': 732304, 'sha1': 'e8b6b5eb4b384975b38875619096b1347a9f0028'}, 'bg': {'y': 20636, 'x': 18344, 'sha1': 'a63520c1c9152726ecd5ca586a037637175e9483'}, '25': {'y': 340952, 'x': 327968, 'sha1': '9ae1a86db13c292a2014dc8461cae7b6e9e6f12c'}, '39': {'y': 526094, 'x': 513112, 'sha1': 'f1a0091415dbcde14540f18875c4fe21727d897a'}, '65': {'y': 939022, 'x': 908832, 'sha1': 'eefbd557a3dbd3271b4fb15e35bd8a9143b2db6f'}, '27': {'y': 367736, 'x': 354624, 'sha1': 'e34bb52deef46d3b53d3d832c2a452f427093a23'}, '71': {'y': 1120384, 'x': 1089712, 'sha1': '10a58ec8aa59f46dc9231ac2fa0590475c10aa5a'}, '70': {'y': 1089698, 'x': 1059104, 'sha1': 'cbf9a6f42ef3ab76d10dba4c3021e8a220720d86'}, '20': {'y': 275252, 'x': 261584, 'sha1': 'f31f95f255410b6eca712d45960042fef4f39da0'}, '38': {'y': 513102, 'x': 499960, 'sha1': 'a1a7d6a110a3fb6d80c092d74280b396d079ce51'}, '21': {'y': 288308, 'x': 275264, 'sha1': '45ab5fad64f1e20c59e8b36132b29f0bf319a6dc'}, '11': {'y': 157744, 'x': 144384, 'sha1': '06cfb1372daea2e326fc45c2de13d3c0ee2bf7d4'}, '10': {'y': 144376, 'x': 132008, 'sha1': 'f5ccd4ffb58023759d231b4a5e36529ced8e36bf'}, '13': {'y': 182830, 'x': 170272, 'sha1': '66da747643a527db4dbe3851731224a3c1315da6'}, '12': {'y': 170258, 'x': 157752, 'sha1': 'a1c83adab3a41c47631fb181db645fea7331ddaa'}, '15': {'y': 209434, 'x': 196552, 'sha1': '9da7b81ee35dedbeebeb8687b5ada0bd4b90a4e3'}, '22': {'y': 301424, 'x': 288320, 'sha1': '82f9d07586a2cf27015f0aecb8f72a2af6955c51'}, '17': {'y': 235732, 'x': 222112, 'sha1': '76d5b0fd91eb50dd43f1985a403eeff0c7953463'}, '16': {'y': 222104, 'x': 209448, 'sha1': '299b54b6a0c0829d08dffafbcc5bb0bf6857ae21'}, '19': {'y': 261576, 'x': 248704, 'sha1': 'c5d6562dce1a8660bed14d8885e073a5a8263a25'}, '18': {'y': 248690, 'x': 235744, 'sha1': '250818ca8d4dbfcee0d907e2e21a3fc77d079a8d'}, '31': {'y': 420630, 'x': 407448, 'sha1': '5734f6c64d27b8aaa14af91beb0359eb2c8dc114'}, '23': {'y': 314866, 'x': 301432, 'sha1': '3513052d064842671ee20c24a575610e96a9c5b2'}, '37': {'y': 499952, 'x': 486880, 'sha1': '814a03136541701db5b7e759304a6d6635135ae0'}, '36': {'y': 486870, 'x': 473752, 'sha1': 'b7498ddd2dbed579c9d615d0ca47640e35bbd4ee'}, '35': {'y': 473744, 'x': 460312, 'sha1': '3c56b24836498b2128d5e17cd36c604399e449af'}, '34': {'y': 460302, 'x': 447296, 'sha1': '9981a0f2bc1aac78e992de2ae348cfea654de3e4'}, '33': {'y': 447282, 'x': 434128, 'sha1': '718addf4d264b00eb64cdc7b5953c97498b00864'}, '55': {'y': 732290, 'x': 719616, 'sha1': 'a086d05c136b8f79672c93e3c4e066791b9124f0'}, '63': {'y': 879252, 'x': 850416, 'sha1': '0f54ff34f4554b21c5fb6e4934c698d50cd6aceb'}, '32': {'y': 434116, 'x': 420640, 'sha1': '500353d2b6d79e79d19f8aa58ba3fa0054e6d770'}, '44': {'y': 591180, 'x': 578208, 'sha1': '7af6836e1f37ffa1ee4e92c075d32f4e1f23f1d3'}, '50': {'y': 668730, 'x': 656080, 'sha1': '7d983df83b6cd4644f671962e38d991b92551119'}}
soundLoc = {'y': 3503016,'x': 1120392,'sha1': '754a3403357067e6da919a0286e2b8b26fd10194'}

if os.path.exists('./showLogo.orig') is not True:
	print('Missing showLogo file!')
	print('Exiting...')
	exit()

# print("showLogo found!")

showLogoHex = binascii.hexlify(open('./showLogo.orig','rb').read())

if os.path.exists('./new_animation') is not True:
	print("Extracting orginal frames...")
	os.makedirs('./new_animation')
	for i in range(1,72):
		i = str(i).zfill(2)
		with open('./new_animation/SIE_Logo-' + i + '.png', 'wb') as f:
			f.write(binascii.unhexlify(showLogoHex[imageLocs[i]['x']:imageLocs[i]['y']]))
	with open('./new_animation/SIE_Logo-bg.png', 'wb') as f:
		f.write(binascii.unhexlify(showLogoHex[imageLocs['bg']['x']:imageLocs['bg']['y']]))
	print("Extracting wav file")
	with open('./SIE_Logo.wav', 'wb') as f:
		f.write(binascii.unhexlify(showLogoHex[soundLoc['x']:soundLoc['y']]))
	print("*****************************************************************")
	print("** Now Edit/Replace frames or audio then run this script again **")
	print("******** Make sure to keep the same file name & location ********")
	print("*****************************************************************")
	exit()

if os.path.exists('./showLogo.new') is not True:
	if os.path.exists('./SIE_Logo.wav') and sha1(binascii.hexlify(open('./SIE_Logo.wav','rb').read())).hexdigest() == soundLoc['sha1']:
		pass
	elif os.path.exists('./SIE_Logo.wav'):
	# 	print("Edited")
		changesMade = True
	# 	print(file + " has been altered")
		print("Changing audio: " + file)
		newAudio = binascii.hexlify(open('./SIE_Logo.wav' + file,'rb').read())
	# 	print(len(newFrame))
		origAudio = showLogoHex[soundLoc['x']:soundLoc['y']]
		diff = len(origAudio) - len(newAudio)
		if diff > 0:
			for i in range(1,diff+1):
				newAudio += '0'
		elif diff == 0:
			pass
		else:
			print("SIE_Logo.wav is too big.")
			exit()	
	# 	print(len(origFrame))
		showLogoHex = str(showLogoHex).replace(str(origAudio),str(newAudio))


	newAnimation = os.listdir("./new_animation")

	for file in sorted(newAnimation):
	# 	print(file)
		if '.png' in file and 'bg' not in file and not file.startswith('.'):
			if sha1(binascii.hexlify(open('./new_animation/' + file,'rb').read())).hexdigest() == imageLocs[re.search('\d\d',str(file)).group(0)]['sha1']:
				pass
			else:
				changesMade = True
	# 			print(file + " has been altered")
				print("Changing frame: " + file)
				newFrame = binascii.hexlify(open('./new_animation/' + file,'rb').read())
	# 			print(len(newFrame))
				origFrame = showLogoHex[imageLocs[re.search('\d\d',str(file)).group(0)]['x']:imageLocs[re.search('\d\d',str(file)).group(0)]['y']]
	# 			print(len(origFrame))
				diff = len(origFrame) - len(newFrame)
				if diff > 0:
					for i in range(1,diff+1):
						newFrame += '0'
				elif diff == 0:
					pass
				else:
					print(file + " is too big.")
					exit()
				showLogoHex = str(showLogoHex).replace(str(origFrame),str(newFrame))
			
		if 'SIE_Logo-bg.png' in file and not file.startswith('.'):	
			if sha1(binascii.hexlify(open('./new_animation/' + file,'rb').read())).hexdigest() == imageLocs['bg']['sha1']:
				pass
			else:
				changesMade = True
	# 			print(file + " has been altered")
				print("Changing frame: " + file)
				newFrame = binascii.hexlify(open('./new_animation/' + file,'rb').read())
	# 			print(len(newFrame))
				origFrame = showLogoHex[imageLocs['bg']['x']:imageLocs['bg']['y']]
	# 			print(len(origFrame))
				diff = len(origFrame) - len(newFrame)
				if diff > 0:
					for i in range(1,diff+1):
						newFrame += '0'
				elif diff == 0:
					pass
				else:
					print(file + " is too big.")
					exit()
				showLogoHex = str(showLogoHex).replace(str(origFrame),str(newFrame))

if changesMade == True:
	with open('showLogo.new', 'wb') as f:
# 		print(sys.version_info[0])
		if sys.version_info[0] == 3:
			showLogoHex = showLogoHex.replace('^b\'','')
			showLogoHex = showLogoHex.replace('\'','')
			showLogoHex = showLogoHex[1:]
		f.write(binascii.unhexlify(showLogoHex))

	print("Successfully created \'showLogo.new\'")
else:
	print("Nothing to do. Maybe you're just dropping by to say \"hi\"?")