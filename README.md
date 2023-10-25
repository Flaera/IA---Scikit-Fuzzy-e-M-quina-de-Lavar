# IA_Scikit_Fuzzy_e_Maquina_de_Lavar


Repositório feito para armazenar as implementações relativas a Lista de Exercícios 2 da disciplina de IA (Inteligência Artificial) da Ufal (Universidade Federal de Alagoas) no período de 2023.1


## Prerequisitos e execução

É preciso instalar o Python 3, o Pip, Matplotlib e Scikit Fuzzy. Os comandos a seguir executados um a um instalam Matplotlib e o Scikit Fuzzy, mas a instalação do Python e do Pip devem ser executadas primeiro e são essenciais:

```bash
python -m pip install -U matplotlib
```
```bash
pip install -U scikit-fuzzy
```

Para executar as respostas digite:

```bash
python3 question1.py
```

## Questão 1

A resposta para a primeira questão esta no script "question1.py".
A questão 1 foi a única respondida e não foi completada, mas ela se encontra respondida parcialmente.
É importante enfatizar que foram criadas arbitrariarmente três regras para gerir a máquina de lavar, que são: 1ª: "se a água é pouca, então a eletricidade é média", 2ª: "se a água é pouca e detergente é pouco, então a eletricidade é baixa" e 3ª: "se detergente é alta, então a eletricidade é alta".
Outro fato importante de se enfatizar é que a eletricidadde foi escolhida como output e consequente, pois dos recursos que a máquina de lavar gere, a eletricidade tem procedência duvidosa quanto a sua origem ser sustentável, sendo assim o componente mais poluidor, segundo arbitrariedade do desenvolvedor.
Ao final dos cálculos é atribuída uma valor de 0 a 10 para cada input ou antecedente. Para água foi atribuído o valor 6 e para detergente foi atribuído o valor 2. A saída após computação das regras foi um gráfico com os intervalos respectivos de cada regra, mas não foi visto nenhum delimitador ou marcação de quanto de eletricidade foi gasta. Porém o interessante é notar que o valor impresso no comando "output" do scikit-fuzzy, que vale cerca de 348.254619, o que pode indicar que dentro do conjunto de domínio de eletricidade, entre 0 e 1000, ela trabalha com esse valor de potência.
Respostas:

### Item 1.1

O universo de discurso das variáveis gira em torno das regras criadas arbitrariarmente para o problema.

### Item 1.2

Os subconjuntos fuzzy são "pouca", "media" e "alta" para as variaveis água e detergente. Já em eletricidade é "baixa", "media" e "alta".



