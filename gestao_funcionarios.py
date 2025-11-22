import sqlite3 as sql

conn = sql.connect('funcionarios.DevTest')
cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS Funcionarios(
     ID INTEGER PRIMARY KEY,
     nome TEXT,
     cargo TEXT,
     salario FLOAT
   )
''')

while True:
    try:
        id_novo = int(input('Insira o ID do novo funcionário (ou digite 0 para sair): '))
        if id_novo == 0:
            break
        nome_novo = input('Insira o nome do novo funcionário: ').title()
        cargo_novo = input('Insira o cargo do novo funcionário: ').title()
        salario_novo = float(input('Insira o salário do novo funcionário: '))

        novo_funcionario = (id_novo, nome_novo, cargo_novo, salario_novo)
        cursor.execute('INSERT INTO Funcionarios VALUES (?, ?, ?, ?)', novo_funcionario)
        conn.commit()
        print(f"Funcionário \033[34m{nome_novo}\033[m inserido com sucesso!")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número para o ID e salário.")
    except sql.IntegrityError:
        print(f"Erro: Funcionário com ID \033[31m{id_novo}\033[m já existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Code for updating employee salary, moved outside the insertion loop
atualizacao = input('Deseja atualizar o sálario de algum funcionario ? (S/N)').upper()
if atualizacao == 'S':
    try:
        id_atualizacao = int(input('Insira o ID do funcionário que deseja atualizar o salário: '))
        novo_salario = float(input('Insira o novo salário do funcionário: '))
        cursor.execute('UPDATE Funcionarios SET salario = ? WHERE ID = ?', (novo_salario, id_atualizacao))
        conn.commit()
        print(f"Salário do funcionário com ID \033[34m{id_atualizacao}\033[m atualizado com sucesso!")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número para o ID e salário.")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o salário: {e}")


cursor.execute('SELECT * FROM Funcionarios')
funcionarios = cursor.fetchall()
print('\n--- Funcionários Cadastrados: ---')
for funcionario in funcionarios:
    print(funcionario)

conn.close()

#FAZER O MENU DE ACESSO
