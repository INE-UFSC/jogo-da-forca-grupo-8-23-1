while erro < 6:
	desenho(erro)
	for i in range (0, tamanho):
        	print(espaço[i], end=" ")
        print("")
    	print("")
	print("não tem: " + " / ".join(str(num) for num in descarte))
	print("")
	print("insira uma letra:")
	chute = input()
	if chute in palavra:
		for i in range (0, tamanho):
			if chute == palavra[i]:
				espaço[i] = chute
	elif chute in descarte:
		pass
	else:
		erro += 1
		descarte.append(chute)
	os.system("clear")
	if espaço == palavra:
		break
