from cx_Freeze import setup, Executable

setup(name='esriEnable',
	  version='0.1',
	  description='Esri Enable ArcGIS Online Accounts',
	  executables=[Executable("esriEnable.py")])