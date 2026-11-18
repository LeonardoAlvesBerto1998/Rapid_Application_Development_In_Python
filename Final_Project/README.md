O SupriDesk é um software desenvolvido em Python 3 que busca gerenciar as solicitações de materiais de uma empresa.

A arquitetura da aplicação foi dividida em duas partes: a interface gráfica (contida no arquivo main.py) e o arquivo de banco de dados (database.py).

Neste programa, foram empregadas apenas bibliotecas nativas da biblioteca padrão do Python 3. A interface gráfica foi construída com o módulo tkinter e seus componentes temáticos ttk 
(como o Treeview e o Combobox), fazendo uso específico dos recursos Frame, para a divisão estrutural dos painéis da janela, e filedialog, para a seleção de diretórios durante a exportação de relatórios. 
A persistência das informações é garantida pelo módulo sqlite3, que cria automaticamente o arquivo de banco de dados solicitacoes.db durante a sua primeira execução. Além disso, também foi utilizado 
o módulo datetime para registrar automaticamente a data e a hora exatas de cada novo pedido, enquanto o módulo csv permite exportar todo o histórico armazenado no formato de planilhas.

Em termos funcionais, o sistema permite o cadastro de solicitações contendo setor, material, quantidade e prioridade (Normal ou Alta), aplicando validações que impedem o envio de campos vazios ou 
quantidades que não sejam números inteiros positivos maiores que zero. Todo registro recém-criado inicia obrigatoriamente com o status Pendente e segue um ciclo de vida controlado que exige 
a transição para Em atendimento antes de ser finalizado como Atendida, bloqueando qualquer tentativa de pular etapas ou repetir a conclusão de um pedido já encerrado. Além disso, a interface 
oferece ferramentas dinâmicas de busca textual por setor ou material, filtragem combinada por status e limpeza rápida da pesquisa.

Para executar a aplicação em uma cópia limpa do repositório, basta possuir o interpretador Python 3 instalado no ambiente, navegar até o diretório raiz onde os arquivos do projeto estão 
localizados e executar o comando python main.py (ou python3 main.py, dependendo da configuração do sistema operacional).Observação: não altere o nome do arquivo database.py nem o seu diretório, 
pois essas ações resultarão em um erro de execução no programa!

Para verificar o funcionamento do software, foi realizada uma sequência de testes. Primeiro, foi cadastrada uma solicitação informando o setor "TI", o material "Mouse USB", a quantidade "5" e a 
prioridade "Alta". Com isso, o registro é inserido na tabela com o status Pendente e a data e hora atuais, além de ser emitido um pop-up na tela dizendo: "Solicitação cadastrada com sucesso!". 
Em seguida, ao tentar registrar um pedido para o setor "Administrativo" com o material "Papel A4", quantidade "0" e prioridade "Normal", o sistema recusa a operação e exibe um alerta: "A quantidade 
deve ser um número positivo diferente de 0!". Na etapa de fluxo de atendimento, ao selecionar o pedido válido e acionar os botões de transição, o status avança de Pendente para Em atendimento e, 
posteriormente, para Atendida, momento em que qualquer nova tentativa de alteração ou conclusão é bloqueada pela aplicação, emitindo o seguinte alerta: "Esta operação já foi concluída (atendida) e 
não pode ser alterada ou repetida!". Por fim, ao fechar e reabrir o programa, verifica-se que os dados permanecem salvos no arquivo solicitacoes.db, sendo também possível realizar buscas pelos 
termos "Mouse" ou "TI", filtrar os resultados pelo status e exportar o histórico completo em formato CSV.

Este projeto foi desenvolvido com o auxílio de ferramentas de Inteligência Artificial (Google Gemini) para a revisão do código e assistência na integração entre a interface gráfica e o banco de dados.
