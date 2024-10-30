# iris-classifier-api

Escolhi o FastAPI como framework porque é a ferramenta com a qual tenho mais familiaridade e também porque é amplamente utilizada para o deploy de modelos de machine learning atualmente.

*OBS: SUBI PARA O REPOSITÓRIO O .env e o BANCO DE DADOS PROPOSITALMENTE PARA FACILITAR O TESTE DA API!*

### Explicação da Arquitetura
Usei uma arquitetura bem simples, parecida com o padrão MVC, tentando aplicar alguns dos princípios do SOLID para deixar o código mais organizado. Sei que alguns endpoints, como os de autenticação (auth) e usuários (user), ainda têm algumas responsabilidades que poderiam ser separadas em serviços específicos. Mas, como a aplicação é simples, achei que não precisava.

Para a segurança, usei JWT, o que ajuda a controlar o acesso às rotas protegidas da API. Também utilizei o Pydantic para validar os dados de entrada, garantindo que só valores corretos sejam processados. No endpoint de POST de user, não apliquei validação para saber se o email é válido e a senha ser segura ou não.

Criei alguns teste unitários e de integração para a verificação da corretude dos casos de uso.

### Melhorias
- Integração com MLflow: Poderia ter usado o MLflow para carregar o modelo de machine learning, assim não precisaria ter o arquivo .pkl diretamente na API. Isso também ajudaria no versionamento e gerenciamento do modelo em produção.

- Monitoramento e Logging: Criei uma tabela usando o SQLAlchemy para salvar o ID do usuário e as respostas do modelo. Isso permite monitorar como a aplicação está sendo usada e pode ajudar em futuras análises ou melhorias do modelo e também serve para utilizar ferramentas como Prometheus e Grafana para o monitoramento em tempo-real da aplicação.

- Implementar um pipeline de CI/CD para teste e deploy automático(caso fosse fazer isso).

- Caso fosse uma api mais complexa poderia usar um outro padrão arquitetural como Clean Architecture, mas não vi necessidade ia apenas dificultar a api.

- Poderia ser usado Kubernetes para orquestrar os containers, facilitando o escalonamento e gerenciamento da aplicação em um ambiente de produção.

### Considerações Finais
No geral, o projeto funciona bem para demonstrar como integrar um modelo de machine learning em uma API usando FastAPI. Mesmo com as melhorias que poderiam ser implementadas, a aplicação cumpre o que se propõe de forma simples e eficiente.

Estou aberto a sugestões e feedbacks para melhorar ainda mais o projeto!
