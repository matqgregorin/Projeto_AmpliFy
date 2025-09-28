# Projeto_AmpliFy
1.1  Visão Geral

O AmpliFy é um sistema inovador de recomendação de músicas que se destaca por utilizar teoria dos grafos e ciência de dados para criar conexões inteligentes e não-óbvias entre faixas musicais. Este projeto surge como uma resposta direta às limitações dos serviços de streaming tradicionais, que frequentemente oferecem recomendações genéricas, repetitivas e baseadas em popularidade. O objetivo é quebrar os ciclos musicais limitados e permitir que os usuários explorem a rica e vasta diversidade musical disponível.
O sistema será desenvolvido como uma plataforma web intuitiva e acessível, combinando facilidade de uso com tecnologias avançadas de processamento e análise de similaridade musical. Ele utiliza a modelagem de grafos para representar de maneira eficiente e intuitiva as interações e relações complexas entre diferentes elementos musicais. Cada música, gênero e artista é representado por um vértice do grafo, enquanto as arestas estabelecem as relações entre esses vértices. 
O objetivo principal é otimizar a experiência do usuário, oferecendo uma recomendação mais precisa e personalizada que vai além das sugestões tradicionais. O sistema permitirá que os usuários descubram novas músicas e artistas com base em sua afinidade musical, favorecendo a descoberta de gêneros menos conhecidos e promovendo uma experiência de escuta mais rica e diversificada. O AmpliFy se ajustará ao comportamento do usuário ao longo do tempo, aprendendo suas preferências e adaptando as recomendações de forma dinâmica.
O sistema funcionará através de um grafo ponderado, onde as arestas podem ter um peso que indica a intensidade da relação. Essa tecnologia de grafos permite explorar tanto as conexões diretas quanto os caminhos indiretos, identificando semelhanças e afinidades musicais menos óbvias.

1.2  Foco Educacional e Cultural

O projeto AmpliFy vai além da melhoria da experiência do usuário em plataformas de streaming. Ele assume um papel estratégico na preservação e promoção da cultura musical brasileira. O sistema será adaptado para gerar playlists focadas em gêneros culturais do Brasil, transformando-se em uma ferramenta pedagógica valiosa para engajar crianças e adolescentes com o patrimônio cultural nacional.
Em ambientes educacionais, os estudantes serão os usuários primários, interagindo diretamente com o sistema para descobrir a diversidade musical brasileira. Os professores atuarão como clientes-chave, integrando o AmpliFy em suas atividades pedagógicas e utilizando-o como um recurso didático para explorar diferentes estilos e tradições musicais do país, tornando o aprendizado mais dinâmico e interativo.
Ao incluir músicas de artistas locais e de gêneros menos conhecidos, o sistema ajuda a valorizar a diversidade cultural e preservar o patrimônio musical, o que está em conformidade com a Meta 11.4 do ODS 11, que visa proteger e salvar o patrimônio cultural imaterial. O sistema de recomendação promove a inclusão cultural, oferecendo visibilidade para artistas locais e uma maior representatividade de diferentes estilos musicais nas plataformas de streaming.
O objetivo final é criar não apenas uma ferramenta tecnológica, mas um instrumento de preservação cultural que incentive a descoberta de novos horizontes musicais, respeitando as preferências individuais enquanto expande o repertório cultural dos usuários.

2. Estrutura do Grafo

O grafo é construído com base em um arquivo de texto (Grafo.txt), que define os vértices e as arestas do sistema. A estrutura do arquivo é a seguinte:
Tipo do Grafo: O valor 0 indica um grafo não-orientado sem peso.
Vértices: Os 66 vértices do grafo são numerados de 0 a 65 e representam músicas, artistas e gêneros.
Arestas: São 260 arestas que conectam os vértices, representando as relações entre eles. Por exemplo, uma aresta conecta a música "Aquarela do Brasil" (vértice 0) ao seu artista "Ary Barroso" (vértice 20) e ao seu gênero "Samba" (vértice 43).

3. Funcionalidades da Aplicação

A aplicação é executada a partir do arquivo main.py e oferece um menu interativo com as seguintes opções:
a) Ler dados do arquivo grafo.txt: Carrega o grafo do arquivo de texto para a memória, utilizando a classe TGrafoND.
b) Gravar dados no arquivo grafo.txt: Salva o grafo atualmente em memória no arquivo de texto.
c) Inserir vértice: Permite adicionar uma nova música, artista ou gênero ao grafo.
d) Inserir aresta: Adiciona uma nova conexão entre dois vértices.
e) Remover vértice: Exclui um vértice e todas as arestas conectadas a ele.
f) Remover aresta: Remove uma conexão específica entre dois vértices.
g) Mostrar conteúdo do arquivo: Exibe o conteúdo do arquivo Grafo.txt de forma organizada.
h) Mostrar grafo: Visualiza a matriz de adjacência do grafo, paginada para facilitar a leitura.
i) Apresentar conexidade: Analisa e informa se o grafo é conexo ou desconexo.
j) Encerrar a aplicação: Finaliza a execução do programa.

4. Como Executar

Certifique-se de ter o Python instalado.
Clone este repositório para a sua máquina local.
Abra um terminal na pasta do projeto.
Execute o arquivo principal com o comando:
  Bash
    python main.py

5. Contribuições

Este projeto foi desenvolvido por:

Bernardo de Souza Pereira - RA: 10312871 
Matheus Queiroz Gregorin - RA: 10418143 
Pedro Henrique Cagnoni Guimaraes - RA: 10417477
