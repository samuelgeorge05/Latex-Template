import jinja2
import os
import requests
import shutil
import subprocess


from jinja2 import Template, FileSystemLoader
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = FileSystemLoader(os.path.abspath('.'))
)

# getting pictures from unsplash for the query "White car"
URL = "https://api.unsplash.com/search/photos/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Param = {"query": "White Car"}
p = requests.get(url=URL, params=Param)
data = p.json()



# Getting picture and data for table

# picture 1
Id1 = data['results'][0]['id']
Pic1 = f"https://api.unsplash.com/photos/{Id1}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex1 = requests.get(url=Pic1)
Exif1 = Ex1.json()
TabDat1 = Exif1['exif']
pic1 = data['results'][0]['links']['download']
response = requests.get(pic1)
file = open("Image1.png", "wb")
file.write(response.content)
file.close()
original = r'C:\Users\samue\PycharmProjects\LaTex Template\Image1.png'
target = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image1.png'
shutil.move(original, target)



# picture 2
Id2 = data['results'][1]['id']
Pic2 = f"https://api.unsplash.com/photos/{Id2}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex2 = requests.get(url=Pic2)
Exif2 = Ex2.json()
TabDat2 = Exif2['exif']
pic2 = data['results'][1]['links']['download']
response1 = requests.get(pic2)
file1 = open("Image2.png", "wb")
file1.write(response1.content)
file1.close()
original1 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image2.png'
target1 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image2.png'
shutil.move(original1, target1)

# picture 3
Id3 = data['results'][2]['id']
Pic3 = f"https://api.unsplash.com/photos/{Id3}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex3 = requests.get(url=Pic3)
Exif3 = Ex3.json()
TabDat3 = Exif3['exif']
pic3 = data['results'][2]['links']['download']
response2 = requests.get(pic3)
file2 = open("Image3.png", "wb")
file2.write(response2.content)
file2.close()
original2 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image3.png'
target2 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image3.png'
shutil.move(original2, target2)


# picture 4
Id4 = data['results'][3]['id']
Pic4 = f"https://api.unsplash.com/photos/{Id4}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex4 = requests.get(url=Pic4)
Exif4 = Ex4.json()
TabDat4 = Exif4['exif']
pic4 = data['results'][3]['links']['download']
response3 = requests.get(pic4)
file3 = open("Image4.png", "wb")
file3.write(response3.content)
file3.close()
original3 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image4.png'
target3 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image4.png'
shutil.move(original3, target3)


# picture 5
Id5 = data['results'][4]['id']
Pic5 = f"https://api.unsplash.com/photos/{Id5}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex5 = requests.get(url=Pic5)
Exif5 = Ex5.json()
TabDat5 = Exif5['exif']
pic5 = data['results'][4]['links']['download']
response4 = requests.get(pic5)
file4 = open("Image5.png", "wb")
file4.write(response4.content)
file4.close()
original4 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image5.png'
target4 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image5.png'
shutil.move(original4, target4)


# picture 6
Id6 = data['results'][5]['id']
Pic6 = f"https://api.unsplash.com/photos/{Id6}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex6 = requests.get(url=Pic6)
Exif6 = Ex6.json()
TabDat6 = Exif6['exif']
pic6 = data['results'][5]['links']['download']
response5 = requests.get(pic6)
file5 = open("Image6.png", "wb")
file5.write(response5.content)
file5.close()
original5 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image6.png'
target5 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image6.png'
shutil.move(original5, target5)


# picture 7
Id7 = data['results'][6]['id']
Pic7 = f"https://api.unsplash.com/photos/{Id7}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex7 = requests.get(url=Pic7)
Exif7 = Ex7.json()
TabDat7 = Exif7['exif']
pic7 = data['results'][6]['links']['download']
response6 = requests.get(pic7)
file6 = open("Image7.png", "wb")
file6.write(response6.content)
file6.close()
original6 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image7.png'
target6 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image7.png'
shutil.move(original6, target6)


# picture 8
Id8 = data['results'][7]['id']
Pic8 = f"https://api.unsplash.com/photos/{Id8}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex8 = requests.get(url=Pic8)
Exif8 = Ex8.json()
TabDat8 = Exif8['exif']
pic8 = data['results'][7]['links']['download']
response7 = requests.get(pic8)
file7 = open("Image8.png", "wb")
file7.write(response7.content)
file7.close()
original7 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image8.png'
target7 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image8.png'
shutil.move(original7, target7)



# picture 9
Id9 = data['results'][8]['id']
Pic9 = f"https://api.unsplash.com/photos/{Id9}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex9 = requests.get(url=Pic9)
Exif9 = Ex9.json()
TabDat9 = Exif9['exif']
pic9 = data['results'][8]['links']['download']
response8 = requests.get(pic9)
file8 = open("Image9.png", "wb")
file8.write(response8.content)
file8.close()
original8 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image9.png'
target8 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image9.png'
shutil.move(original8, target8)



# picture 10
Id10 = data['results'][9]['id']
Pic10 = f"https://api.unsplash.com/photos/{Id10}/?client_id=fnI4D01gpZ6ws1tW6nJI4bxxc4ebOMvCHkcv6FqO9O0"
Ex10 = requests.get(url=Pic10)
Exif10 = Ex10.json()
TabDat10 = Exif10['exif']
pic10 = data['results'][9]['links']['download']
response9 = requests.get(pic10)
file9 = open("Image10.png", "wb")
file9.write(response9.content)
file9.close()
original9 = r'C:\Users\samue\PycharmProjects\LaTex Template\Image10.png'
target9 = r'C:\Users\samue\PycharmProjects\LaTex Template\images\Image10.png'
shutil.move(original9, target9)




# pass tabdatas to template
template = latex_jinja_env.get_template('1x2_template.tex')
finTemplate = template.render(make1=TabDat1['make'], model1=TabDat1['model'], exposure_time1=TabDat1['exposure_time'], aperture1=TabDat1['aperture'],
					  make2=TabDat2['make'], model2=TabDat2['model'], exposure_time2=TabDat2['exposure_time'], aperture2=TabDat2['aperture'],
					  make3=TabDat3['make'], model3=TabDat3['model'], exposure_time3=TabDat3['exposure_time'], aperture3=TabDat3['aperture'],
					  make4=TabDat4['make'], model4=TabDat4['model'], exposure_time4=TabDat4['exposure_time'], aperture4=TabDat4['aperture'],
					  make5=TabDat5['make'], model5=TabDat5['model'], exposure_time5=TabDat5['exposure_time'], aperture5=TabDat5['aperture'],
					  make6=TabDat6['make'], model6=TabDat6['model'], exposure_time6=TabDat6['exposure_time'], aperture6=TabDat6['aperture'],
					  make7=TabDat7['make'], model7=TabDat7['model'], exposure_time7=TabDat7['exposure_time'], aperture7=TabDat7['aperture'],
					  make8=TabDat8['make'], model8=TabDat8['model'], exposure_time8=TabDat8['exposure_time'], aperture8=TabDat8['aperture'],
					  make9=TabDat9['make'], model9=TabDat9['model'], exposure_time9=TabDat9['exposure_time'], aperture9=TabDat9['aperture'],
					  make10=TabDat10['make'], model10=TabDat10['model'], exposure_time10=TabDat10['exposure_time'], aperture10=TabDat10['aperture'],)

LatexFile = open("PdfTemplate.tex", "w")
LatexFile.write(finTemplate)
LatexFile.close()
proc = subprocess.Popen(['pdflatex', 'PdfTemplate.tex'])
proc.communicate()
