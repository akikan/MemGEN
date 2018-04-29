from MemGEN import MemGEN

model = MemGEN()

data=[
	["onore gu-guru"],
	["kon na ron bun"],
	["tuk uri yag atte yur usa nn"],
	["zett ai ni yur usann"],
	["nande kon na mono wo tukutte "],
	["simatta nn da"]]

# learn model 
model.learn(data)

# generate
output = model.generate()
print(output)