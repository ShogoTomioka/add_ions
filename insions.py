#!/usr/bin/python3
# coding: utf-8

import sys
from Num import Nums

class ChargedResidues:
	#荷電アミノ酸と、計算に使う原子の名前のインデックス
	Lys_atoms = ["NZ","HZ1","HZ2","HZ3"]
	Glu_atoms = ["CD","OE1","OE2"]
	Asp_atoms = ["CG","OD1","OD2"]
	Arg_atoms = ["CZ","2HH1","2HH2"]
	Arg_atoms2 = ["CZ","HH12","HH22"]
	Atmo_length = [21,25,25,22,22]



def inquire_user_on_commandline():
	print(tt)


def calculate_cordinate_of_counter_ions(i):
	#カウンターイオンを付加する荷電アミノ酸の座標から、各カウンターイオンの座標を計算する
	print(tt)


def addlines(filename):
	#計算したカウンターイオンの座標をテキストファイルに出力する
	print(tt)


argv=sys.argv
#入力、d出力ファイル名
input_file=""
output_file= "ions.txt"

#入力された系の電荷や家電アミノ酸のリスト等を持つクラス
class ParamOfSystem:

	"""
	length_of_pdb　　　      　：  PDBファイルの列の大きさ
	total_charge              :  系全体の電荷
	list_of_number            :  アミノ酸番号の配列
	list_of_acid_name         :  アミノ酸名の配列
	dict_number_and_name      :  アミノ酸の番号と名前の辞書
	charged_aminoacids        :  系内の荷電アミノ酸のリスト（番号）
	chosen_aminoacids         :  カウンターイオンを付加する荷電アミノ酸（番号）
	start_position            :  座標を計算する時に使う
	location_of_charged_acids :  上に同じ
	"""

	length_of_pdb = 0
	total_charge = 0
	list_of_number = []
	list_of_acid_name = []
	dict_number_and_name ={}
	charged_aminoacids = []
	chosen_aminoacids = []
	start_position = []

	isMonomer_has_name = False


	def create_number_and_name_list(self,data):
		"""
		#各モノマーに識別市（A、B、...)が付いてるかどうかの判断と,アミノ酸の番号と名前のリスト作成
		ATOM      6  O   ACE     1     -27.336   3.451  24.195  1.00  0.00
		と
		ATOM      6  O   ACE  A  1     -27.336   3.451  24.195  1.00  0.00
		では”A”がある分リストの長さが違ってくるので識別子がついているかは確認しないといけない
		識別子があるかどうかはisMonomer_has_nameに入ってる
	"""
		for i in range(self.length_of_pdb):
			line=data[i].split()
			try:
				if line[3]!="WAT" and line[3]!="MOL" and line[0]!="TER" and line[0]!="HETATOM" and line[0]!="ACE" and line[0]!="NME" and line[0]!="HOH" and line[0]!="RES":
				#アミノ酸以外は無視する
					if line[4].isdigit():# モノマーの名前（Aとか）がない場合
						number_to_add = line[4]
					elif line[5].isdigit():
						number_to_add = line[5]
						self.isMonomer_has_name = True
				else:
					return()

				if (number_to_add in self.list_of_number)!=True:
					self.list_of_number.append(number_to_add)

				acid_name=line[3]+str(number_to_add)
				if (acid_name in self.list_of_acid_name)!=True:
					self.list_of_acid_name.append(acid_name)
					self.start_position.append(i)
			except IndexError:
				pass


	def joint_number_to_acidname(self):
	#アミノ酸の番号と名前から、（残基番号ーアミノ酸名）のインデックスを作成する
		self.dict_number_and_name = dict(zip(self.list_of_number, self.list_of_acid_name))


	def count_charge_and_create_charged_list(self):
	#アミノ酸のリストから荷電アミノ酸を見つけて電荷の計算＆系に含まれている荷電アミノ酸のリストを作成する
		for i in self.list_of_number:
			if "ARG" in self.dict_number_and_name[i]:
				self.total_charge+=1
				self.charged_aminoacids.append(i)
			elif "LYS" in self.dict_number_and_name[i]:
				self.total_charge+=1
				self.charged_aminoacids.append(i)
			elif "HIP" in self.dict_number_and_name[i]:
				self.total_charge+=1
				self.charged_aminoacids.append(i)
			elif "ASP" in self.dict_number_and_name[i]:
				self.total_charge-=1
				self.charged_aminoacids.append(i)
			elif "GLU" in self.dict_number_and_name[i]:
				self.total_charge-=1
				self.charged_aminoacids.append(i)



	def extract_charged_aminoacid(self):
		"""
		作成した家電アミノ酸のリストの中から、系の電荷に合わせて荷電アミノ酸を抽出する
		- 系の電荷が プラス => Asp,Gluのみが抽出
		- 系の電荷が マイナス  => Lys,Arg,Hipが抽出される
		"""
		if self.total_charge<0:
			for i in self.charged_aminoacids:
				if "LYS" in self.dict_number_and_name[i]:
					self.charged_aminoacids.remove(i)
				if "ARG" in self.dict_number_and_name[i]:
					self.charged_aminoacids.remove(i)
		if self.total_charge>0:
			for i in self.charged_aminoacids:
				if "GLU" in self.dict_number_and_name[i]:
					self.charged_aminoacids.remove(i)
				if "ASP" in self.dict_number_and_name[i]:
					self.charged_aminoacids.remove(i)


	def set_location_of_selected_aminoacid(self,data):
	#カウンターイオンの座標計算のためにユーザが選択した家電アミノ酸の各原子の座標をリストにセットする
		location=[]
		x=[]
		y=[]
		z=[]
		number=int(length)
		width=len(self.address_cal[number])

		for i in range(width):
			line=data[int(self.address_cal[length][i])]
			line=line.split()
			if self.frag==0:
				x.append(line[5])
				y.append(line[6])
				z.append(line[7])
			elif self.frag==1:
				x.append(line[6])
				y.append(line[7])
				z.append(line[8])
		self.xx.append(x)
		self.yy.append(y)
		self.zz.append(z)



#ユーザが電荷を指定した場合にがこの変数が０以外になる
Spacificated_number_of_charge = 0

if __name__ == "__main__":
	"""
	処理の流れ
	・入力されたPDBからアミノ酸の番号と、アミノ酸名のリストを作る、でもってその二つのリストからdictionaryを作る
	・アミノ酸のリストから系全体の電荷を求める（指定された場合はそちらの電荷を使う）
	・カウンターイオンを付加できる荷電アミノ酸をユーザに示して、付加する荷電アミノ酸を選択してもらう
	・選択されたアミノ酸の座標を取得し、付加するカウンターイオンの座標を計算する
	・計算した座標に、対応するカウンターイオン（プラスならCl-、マイナスならNa+を付加する）
	"""

	param_of_system = ParamOfSystem()
	chargef_residues = ChargedResidues()

	for i in range(len(argv)):
		if argv[i] == "-o":
			output_file = argv[i+1]
			if (".txt" not in output_file):
				output_file += ".txt"
		elif argv[i] == "-i":
			input_file = argv[i+1]
		elif argv[i] == "-n":
			header_file = argv[i+1]
		if argv[i] == "-h":
			print(  "\n------------------:help--------------------------\n"\
            "This program can add ions near the charged amino acids,\n and you can also specificate the charge of system.\"\n"\
			"if total charge of system is minus,this program will add Na+, if not, Cl-\n"\
        	"-------------------------------------------------\n"\
            "-i : input file | .pdb\"\n"\
            "-o : output file, | .pdb  ,default name is `ions.txt`\n"\
            "-n : option for specification of total charge\n"\
            "-h : show help\n"\
            )
			sys.exit()
	if(input_file==""):
		print("please, specify input file!!")
		sys.exit()

	#ファイルオープン
	with open(input_file) as data:
		pdb_data = data.readlines()


	param_of_system.length_of_pdb = len(pdb_data)
	param_of_system.create_number_and_name_list(pdb_data)
	param_of_system.joint_number_to_acidname()
	param_of_system.count_charge_and_create_charged_list()
	param_of_system.extract_charged_aminoacid()
	param_of_system.set_location_of_selected_aminoacid(data)







